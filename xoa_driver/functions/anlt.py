from __future__ import annotations
from dataclasses import dataclass, field
import typing as t
from xoa_driver import enums
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v1.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v1.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericL23Port
from xoa_driver.lli import commands
from xoa_driver.internals.core import interfaces as itf
from xoa_driver.misc import Token
from .tools import (
    get_ctx,
    dictionize_autoneg_status,
    dictionize_lt_status,
    dictionize_txtap_get,
    dictionize_anlt_status,
)
import asyncio

PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL


@dataclass
class DoAnlt:
    port: GenericL23Port
    """port object"""
    should_do_an: bool
    """should the port do autoneg?"""
    should_do_lt: bool
    """should the port do link training?"""
    an_allow_loopback: bool
    """should the autoneg allow loopback?"""
    lt_preset0: enums.NRZPreset
    """out-of-sync tap values (preset 0): existing or standard"""
    lt_initial_modulations: dict[str, enums.LinkTrainEncoding]
    """the initial modulations of each serdes"""
    should_lt_interactive: bool
    """should perform link training manually?"""
    lt_algorithm: dict[str, enums.LinkTrainAlgorithm]
    """link training algorithm should be used?"""

    _group: tuple["itf.IConnection", int, int] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._group = get_ctx(self.port)

    def __pp_autoneg(self, on: bool) -> Token:
        state = enums.AutoNegMode.ANEG_ON if on else enums.AutoNegMode.ANEG_OFF
        return commands.PP_AUTONEG(*self._group).set(
            state,
            enums.AutoNegTecAbility.DEFAULT_TECH_MODE,
            enums.AutoNegFECOption.NO_FEC,
            enums.AutoNegFECOption.NO_FEC,
            enums.PauseMode.NO_PAUSE,
        )

    def __pp_link_train(
        self,
        mode: enums.LinkTrainingMode,
        nrz_preset: enums.NRZPreset,
        timeout_mode: enums.TimeoutMode,
    ) -> Token:
        return commands.PP_LINKTRAIN(*self._group).set(
            mode=mode,
            pam4_frame_size=enums.PAM4FrameSize.P16K_FRAME,
            nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT,
            nrz_preset=nrz_preset,
            timeout_mode=timeout_mode,
        )

    def __pl1_cfg_tmp(
        self, serdes: int, config_type: int, values: list[int]
    ) -> Token:
        return commands.PL1_CFG_TMP(*self._group, serdes, config_type).set(
            values=values
        )

    def __select_modes(self) -> tuple[enums.LinkTrainingMode, enums.TimeoutMode]:
        if self.should_do_an:
            lt_mode = enums.LinkTrainingMode.START_AFTER_AUTONEG
            timeout_mode = enums.TimeoutMode.DEFAULT
        elif self.should_lt_interactive:
            lt_mode = enums.LinkTrainingMode.INTERACTIVE
            timeout_mode = enums.TimeoutMode.DISABLED
        else:
            lt_mode = enums.LinkTrainingMode.STANDALONE
            timeout_mode = enums.TimeoutMode.DEFAULT
        return lt_mode, timeout_mode

    def __builder__(self) -> t.Generator[Token, None, None]:
        """Defining commands sequence"""
        nrz_preset = self.lt_preset0
        # # Set autoneg timeout
        yield self.__pp_link_train(
            enums.LinkTrainingMode.DISABLED,
            enums.NRZPreset.NRZ_NO_PRESET,
            enums.TimeoutMode.DEFAULT,
        )

        # # Set autoneg allow-loopback
        yield self.__pl1_cfg_tmp(
            0, enums.Layer1ConfigType.AN_LOOPBACK, [int(self.an_allow_loopback)]
        )

        # yield self.__pp_autoneg(self.should_do_an and not self.should_do_lt)
        if (not self.should_do_an) or self.should_do_lt:
            # Disable autoneg
            yield self.__pp_autoneg(False)

        if self.should_do_lt:
            for serdes_str, algorithm in self.lt_algorithm.items():
                # # Set the link train algorithm
                yield self.__pl1_cfg_tmp(
                    int(serdes_str), enums.Layer1ConfigType.LT_TRAINING_ALGORITHM, [algorithm.value]
                )

            for serdes_str, im in self.lt_initial_modulations.items():
                yield self.__pl1_cfg_tmp(
                    int(serdes_str), enums.Layer1ConfigType.LT_INITIAL_MODULATION, [im.value]
                )

            lt_mode, timeout_mode = self.__select_modes()
            yield self.__pp_link_train(
                enums.LinkTrainingMode.DISABLED, nrz_preset, timeout_mode
            )
            yield self.__pp_link_train(lt_mode, nrz_preset, timeout_mode)

        if self.should_do_an:
            yield self.__pp_autoneg(True)

    async def run(self) -> None:
        """Start anlt execution"""
        await apply(*self.__builder__())


async def anlt_start(
    port: GenericL23Port,
    should_do_an: bool,
    should_do_lt: bool,
    an_allow_loopback: bool,
    lt_preset0: enums.NRZPreset,
    lt_initial_modulations: dict[str, enums.LinkTrainEncoding],
    should_lt_interactive: bool,
    lt_algorithm: dict[str, enums.LinkTrainAlgorithm],
) -> None:
    """Start ANLT on a port

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param should_do_an: should the port do autoneg?
    :type should_do_an: bool
    :param should_do_lt: should the port do link training?
    :type should_do_lt: bool
    :param an_allow_loopback: should the autoneg allow loopback?
    :type an_allow_loopback: bool
    :param lt_preset0: out-of-sync tap values (preset 0): existing or standard
    :type lt_preset0: enums.NRZPreset
    :param lt_initial_modulations: the initial modulations of each serdes
    :type lt_initial_modulations: typing.Dict[str, enums.LinkTrainEncoding]
    :param should_lt_interactive: should perform link training manually?
    :type should_lt_interactive: bool
    :param lt_algorithm: Link training algorithm to use
    :type lt_algorithm: Dict[str, enums.LinkTrainAlgorithm]
    """

    anlt = DoAnlt(
        port,
        should_do_an,
        should_do_lt,
        an_allow_loopback,
        lt_preset0,
        lt_initial_modulations,
        should_lt_interactive,
        lt_algorithm,
    )
    await anlt.run()


async def autoneg_status(port: GenericL23Port) -> dict[str, t.Any]:
    """Get the auto-negotiation status

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return:
    :rtype: typing.Dict[str, typing.Any]
    """
    conn, mid, pid = get_ctx(port)
    loopback, auto_neg_info = await apply(
        commands.PL1_CFG_TMP(
            conn, mid, pid, 0, enums.Layer1ConfigType.AN_LOOPBACK
        ).get(),
        commands.PL1_AUTONEGINFO(conn, mid, pid, 0).get(),
    )
    return dictionize_autoneg_status(loopback, auto_neg_info)


LinkTrainType = t.Union[
    enums.LinkTrainCoeffs,
    enums.LinkTrainPresets,
    enums.LinkTrainEncoding,
    enums.LinkTrainAnnounce,
]


async def __lt_coeff(
    port: GenericL23Port,
    serdes: int,
    arg: LinkTrainType,
    *,
    cmd: enums.LinkTrainCmd,
) -> enums.LinkTrainCmdResults:
    conn, mid, pid = get_ctx(port)
    cmd_ = commands.PL1_LINKTRAIN_CMD(conn, mid, pid, serdes)
    await cmd_.set(cmd=cmd, arg=arg.value)
    for _ in range(1000):
        resp = await cmd_.get()
        status = resp.result
        if (resp.flags & enums.LinkTrainCmdFlags.DONE.value):
            return enums.LinkTrainCmdResults(status)
        await asyncio.sleep(0.01)
    return enums.LinkTrainCmdResults.UNKNOWN


async def lt_coeff_inc(
    port: GenericL23Port, serdes: int, emphasis: enums.LinkTrainCoeffs
) -> enums.LinkTrainCmdResults:
    """Ask the remote port to increase coeff of the specified serdes.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :param emphasis: the emphasis to increase
    :type emphasis: enums.LinkTrainCoeffs
    :return:
    :rtype: None
    """
    return await __lt_coeff(port, serdes, emphasis, cmd=enums.LinkTrainCmd.CMD_INC)


async def lt_coeff_dec(
    port: GenericL23Port, serdes: int, emphasis: enums.LinkTrainCoeffs
) -> enums.LinkTrainCmdResults:
    """Ask the remote port to decrease coeff of the specified serdes.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :param emphasis: the emphasis to decrease
    :type emphasis: enums.LinkTrainCoeffs
    :return:
    :rtype: None
    """
    return await __lt_coeff(port, serdes, emphasis, cmd=enums.LinkTrainCmd.CMD_DEC)


async def lt_preset(
    port: GenericL23Port, serdes: int, preset: enums.LinkTrainPresets
) -> enums.LinkTrainCmdResults:
    """Ask the remote port to use the preset of the specified serdes.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :param preset: preset index to select for the serdes, 0,1,2,3,4,
    :type preset: enums.LinkTrainPresets
    :return:
    :rtype: None
    """
    return await __lt_coeff(port, serdes, preset, cmd=enums.LinkTrainCmd.CMD_PRESET)


async def lt_encoding(
    port: GenericL23Port, serdes: int, encoding: enums.LinkTrainEncoding
) -> enums.LinkTrainCmdResults:
    """Ask the remote port to use the encoding of the specified serdes.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :param encoding: link training encoding
    :type encoding: enums.LinkTrainCoeffs
    :return:
    :rtype: None
    """
    return await __lt_coeff(port, serdes, encoding, cmd=enums.LinkTrainCmd.CMD_ENCODING)


async def lt_trained(port: GenericL23Port, serdes: int) -> enums.LinkTrainCmdResults:
    """Tell the remote port that the current serdes is trained.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :return:
    :rtype: None
    """
    return await __lt_coeff(
        port,
        serdes,
        arg=enums.LinkTrainAnnounce.TRAINED,
        cmd=enums.LinkTrainCmd.CMD_LOCAL_TRAINED,
    )


async def lt_status(port: GenericL23Port, serdes: int) -> dict[str, t.Any]:
    """Show the link training status.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :return: LT status of the serdes
    :rtype: typing.Dict[str, typing.Any]
    """
    conn, mid, pid = get_ctx(port)
    status, info, ltconf, cfg = await apply(
        commands.PP_LINKTRAINSTATUS(conn, mid, pid, serdes).get(),
        commands.PL1_LINKTRAININFO(conn, mid, pid, serdes, 0).get(),
        commands.PP_LINKTRAIN(conn, mid, pid).get(),
        commands.PL1_CFG_TMP(
            conn, mid, pid, serdes, enums.Layer1ConfigType.LT_INITIAL_MODULATION
        ).get(),
    )
    total_bit_count = (info.prbs_total_bits_high << 32) + info.prbs_total_bits_low
    total_error_bit_count = (
        info.prbs_total_error_bits_high << 32
    ) + info.prbs_total_error_bits_low
    ber = (
        total_error_bit_count / total_bit_count if total_bit_count > 0 else float("nan")
    )
    return dictionize_lt_status(
        status, info, ltconf, cfg, ber, total_bit_count, total_error_bit_count
    )


async def txtap_get(port: GenericL23Port, serdes: int) -> dict[str, int]:
    """Get the tap value of the local TX tap.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :return: tap values of the serdes
    :rtype: typing.Dict[str, int]
    """
    conn, mid, pid = get_ctx(port)
    r = await commands.PP_PHYTXEQ(conn, mid, pid, serdes).get()
    return dictionize_txtap_get(r)


async def txtap_set(
    port: GenericL23Port,
    serdes: int,
    pre3: int,
    pre2: int,
    pre: int,
    main: int,
    post1: int,
) -> None:
    """Set the tap value of the local TX tap.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :param pre3: pre3 value
    :type pre3: int
    :param pre2: pre2 value
    :type pre2: int
    :param pre: pre value
    :type pre: int
    :param main: main value
    :type main: int
    :param post1: post1 value
    :type post1: int
    :return:
    :rtype: None
    """
    conn, mid, pid = get_ctx(port)
    cmd_ = commands.PP_PHYTXEQ(conn, mid, pid, serdes)
    await cmd_.set(
        pre1=pre,
        main=main,
        post1=post1,
        pre2=pre2,
        post2=pre3,
        post3=0,
    )


async def anlt_link_recovery(port: GenericL23Port, enable: bool) -> None:
    """Should xenaserver automatically do link recovery when detecting down signal.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param enable: should the port automatically do link recovery when link is down.
    :type enable: bool
    :return:
    :rtype:  None
    """
    conn, mid, pid = get_ctx(port)
    cmd_ = commands.PL1_CFG_TMP(
        conn, mid, pid, 0, enums.Layer1ConfigType.ANLT_INTERACTIVE
    )
    await cmd_.set(values=[int(enable)])


async def anlt_status(port: GenericL23Port) -> dict[str, t.Any]:
    """Get the overview of ANLT status

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return: AN/LT status of the port
    :rtype: typing.Dict[str, typing.Any]
    """

    # if not isinstance(port, LinkTrainingSupported):
    #     raise NotSupportLinkTrainError(port)
    conn, mid, pid = get_ctx(port)
    r = await apply(
        commands.PL1_CFG_TMP(
            conn, mid, pid, 0, enums.Layer1ConfigType.ANLT_INTERACTIVE
        ).get(),
        commands.PP_AUTONEGSTATUS(conn, mid, pid).get(),
        commands.PP_LINKTRAIN(conn, mid, pid).get(),
        commands.P_CAPABILITIES(conn, mid, pid).get(),
        commands.PL1_CFG_TMP(conn, mid, pid, 0, enums.Layer1ConfigType.AN_LOOPBACK).get(),
    )
    link_recovery, autoneg, linktrain, capabilities, allow_loopback= r
    initial_mods = {}
    algorithms={}
    for i in range(0, capabilities.serdes_count):
        resp = await apply(
            commands.PL1_CFG_TMP(conn, mid, pid, i, enums.Layer1ConfigType.LT_INITIAL_MODULATION).get(),
            commands.PL1_CFG_TMP(conn, mid, pid, i, enums.Layer1ConfigType.LT_TRAINING_ALGORITHM).get()
        )
        im, alg = resp
        initial_mods[str(i)] = enums.LinkTrainEncoding(im.values[0]).name
        algorithms[str(i)] = enums.LinkTrainEncoding(alg.values[0]).name

    return dictionize_anlt_status(link_recovery, autoneg, linktrain, capabilities, allow_loopback, initial_mods, algorithms)


async def anlt_log(port: GenericL23Port) -> str:
    """Get the anlt log messages

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return: AN/LT protocol log traces of the port
    :rtype: str
    """
    conn, mid, pid = get_ctx(port)
    log = await commands.PL1_LOG(conn, mid, pid).get()
    return log.log_string


__all__ = (
    "anlt_log",
    "anlt_start",
    "lt_coeff_inc",
    "lt_coeff_dec",
    "lt_encoding",
    "lt_preset",
    "lt_status",
    "lt_trained",
    "autoneg_status",
    "anlt_link_recovery",
    "anlt_status",
    "txtap_get",
    "txtap_set",
)
