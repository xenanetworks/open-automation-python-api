from __future__ import annotations
from dataclasses import dataclass, field
import typing as t
from xoa_driver import enums
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v1.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v1.ports.port_l23.family_l1 import FamilyFreya
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
    dictionize_lt_im_status,
    dictionize_lt_algorithm_status,
    dictionize_anlt_log_ctrl_status
)
import asyncio

PcsPmaSupported = (FamilyL, FamilyFreya)
AutoNegSupported = (FamilyL, FamilyFreya)
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
    lt_preset0: enums.FreyaOutOfSyncPreset
    """out-of-sync tap values (preset 0): existing or standard"""
    lt_initial_modulations: dict[str, enums.LinkTrainEncoding]
    """the initial modulations of each serdes"""
    should_lt_interactive: bool
    """should perform link training manually?"""
    lt_algorithm: dict[str, enums.LinkTrainAlgorithm]
    """link training algorithm should be used?"""
    should_enable_lt_timeout: bool
    """should the port do link training with timeout enabled?"""

    _group: tuple["itf.IConnection", int, int] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._group = get_ctx(self.port)

    # def __pp_autoneg(self, on: bool) -> Token:
    #     state = enums.FreyaAutonegMode.ENABLED if on else enums.FreyaAutonegMode.DISABLED
    #     return commands.PL1_AUTONEG_CONFIG(*self._group).set(

    #     )
    #     return commands.PP_AUTONEG(*self._group).set(
    #         state,
    #         enums.AutoNegTecAbility.DEFAULT_TECH_MODE,
    #         enums.AutoNegFECOption.DEFAULT_FEC,
    #         enums.AutoNegFECOption.DEFAULT_FEC,
    #         enums.PauseMode.NO_PAUSE,
    #     )

    def __pl1_linktrain_config(
        self,
        ooo_preset: enums.FreyaOutOfSyncPreset,
        timeout_mode: enums.TimeoutMode,
    ) -> Token:
        return commands.PL1_LINKTRAIN_CONFIG(*self._group).set(
            oos_preset=ooo_preset,
            timeout_mode=timeout_mode,
        )

    def __pl1_cfg_tmp(
        self, serdes: int, config_type: enums.Layer1ConfigType, values: list[int]
    ) -> Token:
        return commands.PL1_CFG_TMP(*self._group, serdes, config_type).set(
            values=values
        )
    
    def __pl1_anlt(
        self,
        an_mode: enums.FreyaAutonegMode,
        lt_mode: enums.FreyaLinkTrainingMode,
    ) -> Token:
        return commands.PL1_ANLT(*self._group).set(
            an_mode=an_mode,
            lt_mode=lt_mode,
        )

    def __select_modes(self) -> tuple[enums.FreyaAutonegMode, enums.FreyaLinkTrainingMode, enums.TimeoutMode]:
        if self.should_do_an == True:
            _an_mode = enums.FreyaAutonegMode.ENABLED
        else:
            _an_mode = enums.FreyaAutonegMode.DISABLED
        if self.should_do_lt == True:
            # LT interactive must always disable LT timeout
            if self.should_lt_interactive == True:
                _lt_mode = enums.FreyaLinkTrainingMode.ENABLED_INTERACTIVE
                _timeout_mode = enums.TimeoutMode.DISABLED
            # For LT auto, you can either enable LT timeout or disable LT timeout
            elif self.should_enable_lt_timeout == True:
                _lt_mode = enums.FreyaLinkTrainingMode.ENABLED_AUTO
                _timeout_mode = enums.TimeoutMode.DEFAULT
            else:
                _lt_mode = enums.FreyaLinkTrainingMode.ENABLED_AUTO
                _timeout_mode = enums.TimeoutMode.DISABLED
        else:
            _lt_mode = enums.FreyaLinkTrainingMode.DISABLED
            _timeout_mode = enums.TimeoutMode.DISABLED

        return _an_mode, _lt_mode, _timeout_mode

    def __builder__(self) -> t.Generator[Token, None, None]:
        """Defining commands sequence"""
        
        # # Set autoneg timeout
        # yield self.__pl1_linktrain_config(
        #     enums.LinkTrainingMode.DISABLED,
        #     enums.NRZPreset.NRZ_NO_PRESET,
        #     enums.TimeoutMode.DEFAULT,
        # )

        # # Set autoneg allow-loopback
        yield self.__pl1_cfg_tmp(
            0, enums.Layer1ConfigType.AN_LOOPBACK, [int(self.an_allow_loopback)]
        )

        # yield self.__pp_autoneg(self.should_do_an and not self.should_do_lt)
        # if (not self.should_do_an) or self.should_do_lt:
        # Disable autoneg
        # yield self.__pp_autoneg(False)

        # Set the link train algorithm
        for serdes_str, algorithm in self.lt_algorithm.items():
            yield self.__pl1_cfg_tmp(
                int(serdes_str), enums.Layer1ConfigType.LT_TRAINING_ALGORITHM, [algorithm.value]
            )
        # Set the link train initial modulation
        for serdes_str, im in self.lt_initial_modulations.items():
            yield self.__pl1_cfg_tmp(
                int(serdes_str), enums.Layer1ConfigType.LT_INITIAL_MODULATION, [im.value]
            )

        # Get the mode
        _an_mode, _lt_mode, _timeout_mode = self.__select_modes()

        # Set link train config
        _ooo_preset = self.lt_preset0
        yield self.__pl1_linktrain_config(
            _ooo_preset, _timeout_mode
        )

        # Start AN/LT
        yield self.__pl1_anlt(
            _an_mode, _lt_mode
        )


    async def run(self) -> None:
        """Start anlt execution"""
        await apply(*self.__builder__())


async def anlt_start(
    port: GenericL23Port,
    should_do_an: bool,
    should_do_lt: bool,
    an_allow_loopback: bool,
    lt_preset0: enums.FreyaOutOfSyncPreset,
    lt_initial_modulations: dict[str, enums.LinkTrainEncoding],
    should_lt_interactive: bool,
    lt_algorithm: dict[str, enums.LinkTrainAlgorithm],
    should_enable_lt_timeout: bool,
) -> None:
    """
    .. versionchanged:: 2.5

    Start ANLT on a port

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param should_do_an: should the port do autoneg?
    :type should_do_an: bool
    :param should_do_lt: should the port do link training?
    :type should_do_lt: bool
    :param an_allow_loopback: should the autoneg allow loopback?
    :type an_allow_loopback: bool
    :param lt_preset0: out-of-sync tap values (preset 0): existing or standard
    :type lt_preset0: enums.FreyaOutOfSyncPreset
    :param lt_initial_modulations: the initial modulations of each serdes
    :type lt_initial_modulations: typing.Dict[str, enums.LinkTrainEncoding]
    :param should_lt_interactive: should perform link training manually?
    :type should_lt_interactive: bool
    :param lt_algorithm: Link training algorithm to use
    :type lt_algorithm: Dict[str, enums.LinkTrainAlgorithm]
    :param should_enable_lt_timeout: should run link training with timeout?
    :type should_enable_lt_timeout: bool
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
        should_enable_lt_timeout,
    )
    await anlt.run()


async def autoneg_status(port: GenericL23Port) -> dict[str, t.Any]:
    """
    .. versionchanged:: 2.5

    Get the auto-negotiation status

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return:
    :rtype: typing.Dict[str, typing.Any]
    """
    conn, mid, pid = get_ctx(port)
    loopback, auto_neg_info, status = await apply(
        commands.PL1_CFG_TMP(
            conn, mid, pid, 0, enums.Layer1ConfigType.AN_LOOPBACK
        ).get(),
        commands.PL1_AUTONEGINFO(conn, mid, pid, 0).get(),
        commands.PL1_AUTONEG_STATUS(conn, mid, pid).get(),
    )
    return dictionize_autoneg_status(loopback, auto_neg_info, status)


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
    port: GenericL23Port,
    serdes: int,
    emphasis: enums.LinkTrainCoeffs
) -> enums.LinkTrainCmdResults:
    """
    .. versionadded:: 1.1

    Ask the remote port to increase coeff of the specified serdes.

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
    port: GenericL23Port,
    serdes: int,
    emphasis: enums.LinkTrainCoeffs
) -> enums.LinkTrainCmdResults:
    """
    .. versionadded:: 1.1

    Ask the remote port to decrease coeff of the specified serdes.

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


async def lt_coeff_no_eq(
    port: GenericL23Port,
    serdes: int,
    emphasis: enums.LinkTrainCoeffs
) -> enums.LinkTrainCmdResults:

    """
    .. versionadded:: 2.0

    Ask the remote port to set the coeff to NO_EQ on the specified serdes.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :param emphasis: the emphasis to set to NO_EQ
    :type emphasis: enums.LinkTrainCoeffs
    :return:
    :rtype: None
    """
    return await __lt_coeff(port, serdes, emphasis, cmd=enums.LinkTrainCmd.CMD_NO_EQ)


async def lt_preset(
    port: GenericL23Port,
    serdes: int,
    preset: enums.LinkTrainPresets
) -> enums.LinkTrainCmdResults:
    """
    .. versionadded:: 1.1

    Ask the remote port to use the preset of the specified serdes.

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
    port: GenericL23Port,
    serdes: int,
    encoding: enums.LinkTrainEncoding
) -> enums.LinkTrainCmdResults:
    """
    .. versionadded:: 1.1

    Ask the remote port to use the encoding of the specified serdes.

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
    """
    .. versionadded:: 1.1

    Tell the remote port that the current serdes is trained.

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
    """
    .. versionchanged:: 2.5

    Show the link training status.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :return: LT status of the serdes
    :rtype: typing.Dict[str, typing.Any]
    """
    conn, mid, pid = get_ctx(port)
    status, info, ltconf, cfg = await apply(
        commands.PL1_LINKTRAIN_STATUS(conn, mid, pid, serdes).get(),
        commands.PL1_LINKTRAININFO(conn, mid, pid, serdes, 0).get(),
        commands.PL1_LINKTRAIN_CONFIG(conn, mid, pid).get(),
        commands.PL1_CFG_TMP(
            conn, mid, pid, serdes, enums.Layer1ConfigType.LT_INITIAL_MODULATION
        ).get(),
    )
    total_bit_count = (info.prbs_total_bits_high << 32) + info.prbs_total_bits_low
    total_error_bit_count = (
        info.prbs_total_error_bits_high << 32
    ) + info.prbs_total_error_bits_low
    ber = total_error_bit_count / total_bit_count if total_bit_count > 0 else float("nan")
    return dictionize_lt_status(
        status, info, ltconf, cfg, ber, total_bit_count, total_error_bit_count
    )


async def txtap_get(port: GenericL23Port, serdes: int) -> dict[str, int]:
    """
    .. versionadded:: 1.1

    Get the tap value of the local TX tap.

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
    """
    .. versionadded:: 1.1

    Set the tap value of the local TX tap.

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
        pre=pre,
        main=main,
        post=post1,
        pre2=pre2,
        pre3_post2=pre3,
        post3=0,
    )


async def anlt_link_recovery(port: GenericL23Port, restart_link_down: bool, restart_lt_failure: bool) -> None:
    """
    This command manages the auto-restart features.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param restart_link_down: enable AN+LT auto-restart when a link down condition is detected. A "link down" state signifies the loss of a valid input signal, which can occur due to events such as cable unplugging and re-plugging, TX disable, or link flap on the link partner's end. The auto-restart process will continue until the link is re-established. Please note that this setting is only effective when AN and/or LT are enabled.
    :type restart_link_down: bool
    :param restart_lt_failure: if LT is enabled and experiences a failure on either side, the port will initiate the AN+LT restart process repeatedly until LT succeeds. This functionality is only applicable when LT is enabled.
    :type restart_lt_failure: bool
    :return:
    :rtype:  None
    """
    conn, mid, pid = get_ctx(port)
    param = 0
    if restart_link_down == True:
        param += 1
    if restart_lt_failure == True:
        param += 2
    cmd_ = commands.PL1_CFG_TMP(
        conn, mid, pid, 0, enums.Layer1ConfigType.AUTO_LINK_RECOVERY
    )
    await cmd_.set(values=[param])


async def anlt_status(port: GenericL23Port) -> dict[str, t.Any]:
    """
    .. versionchanged:: 2.5

    Get the overview of ANLT status

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return: AN/LT status of the port
    :rtype: typing.Dict[str, typing.Any]
    """

    # if not isinstance(port, LinkTrainingSupported):
    #     raise NotSupportLinkTrainError(port)
    conn, mid, pid = get_ctx(port)
    _link_recovery, _anlt_op, _linktrain_cfg, _capabilities, _allow_loopback = await apply(
        commands.PL1_CFG_TMP(
            conn, mid, pid, 0, enums.Layer1ConfigType.AUTO_LINK_RECOVERY
        ).get(),
        commands.PL1_ANLT(conn, mid, pid).get(),
        commands.PL1_LINKTRAIN_CONFIG(conn, mid, pid).get(),
        commands.P_CAPABILITIES(conn, mid, pid).get(),
        commands.PL1_CFG_TMP(conn, mid, pid, 0, enums.Layer1ConfigType.AN_LOOPBACK).get(),
    )

    return dictionize_anlt_status(_link_recovery, _anlt_op, _linktrain_cfg, _capabilities, _allow_loopback)


async def anlt_log(port: GenericL23Port) -> str:
    """
    .. versionadded:: 1.1

    Get the anlt log messages

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return: AN/LT protocol log traces of the port
    :rtype: str
    """
    conn, mid, pid = get_ctx(port)
    log = await commands.PL1_LOG(conn, mid, pid).get()
    return log.log_string


async def anlt_stop(port: GenericL23Port) -> None:
    """
    .. versionchanged:: 2.5

    Stop AN & LT

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    """
    conn, mid, pid = get_ctx(port)

    await commands.PL1_ANLT(conn, mid, pid).set(
        an_mode=enums.FreyaAutonegMode.DISABLED,
        lt_mode=enums.FreyaLinkTrainingMode.DISABLED
        )


async def txtap_autotune(port: GenericL23Port, serdes: int) -> None:
    """
    .. versionadded:: 1.3

    Auto tune the tap value of the local TX tap.

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param serdes: the serdes index, starting from 0
    :type serdes: int
    :return:
    :rtype: None
    """
    conn, mid, pid = get_ctx(port)
    phy_autotune = commands.PP_PHYAUTOTUNE(conn, mid, pid, serdes)
    await phy_autotune.set(on_off=enums.OnOff.OFF)
    await phy_autotune.set(on_off=enums.OnOff.ON)


async def lt_im_status(port: GenericL23Port) -> dict[str, t.Any]:
    """
    .. versionadded:: 1.3

    Get LT initial modulation config

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return: LT initial modulation configuration of the port
    :rtype: typing.Dict[str, typing.Any]
    """

    # if not isinstance(port, LinkTrainingSupported):
    #     raise NotSupportLinkTrainError(port)
    conn, mid, pid = get_ctx(port)
    capabilities = await commands.P_CAPABILITIES(conn, mid, pid).get()
    initial_mods = {}
    for i in range(0, capabilities.serdes_count):
        im = await commands.PL1_CFG_TMP(conn, mid, pid, i, enums.Layer1ConfigType.LT_INITIAL_MODULATION).get()
        initial_mods[str(i)] = enums.LinkTrainEncoding(im.values[0]).name

    return dictionize_lt_im_status(capabilities, initial_mods)


async def lt_algorithm_status(port: GenericL23Port) -> dict[str, t.Any]:
    """
    .. versionadded:: 1.3

    Get LT initial modulation config

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return: LT initial modulation configuration of the port
    :rtype: typing.Dict[str, typing.Any]
    """

    # if not isinstance(port, LinkTrainingSupported):
    #     raise NotSupportLinkTrainError(port)
    conn, mid, pid = get_ctx(port)
    capabilities = await commands.P_CAPABILITIES(conn, mid, pid).get()
    algorithms = {}
    for i in range(0, capabilities.serdes_count):
        alg = await commands.PL1_CFG_TMP(conn, mid, pid, i, enums.Layer1ConfigType.LT_TRAINING_ALGORITHM).get()
        algorithms[str(i)] = enums.LinkTrainAlgorithm(alg.values[0]).name

    return dictionize_lt_algorithm_status(capabilities, algorithms)


async def anlt_strict(port: GenericL23Port, enable: bool) -> None:
    """
    .. versionadded:: 1.3

    Should ANLT strict mode be enabled

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param enable: should ANLT strict mode be enabled
    :type enable: bool
    :return:
    :rtype:  None
    """
    conn, mid, pid = get_ctx(port)
    capabilities = await commands.P_CAPABILITIES(conn, mid, pid).get()
    param = int(enable)
    for i in range(0, capabilities.serdes_count):
        await commands.PL1_CFG_TMP(
            conn,
            mid,
            pid,
            i,
            enums.Layer1ConfigType.ANLT_STRICT_MODE
        ).set(values=[param])


async def anlt_log_control(port: GenericL23Port, types: t.List[enums.AnLtLogControl]) -> None:
    """
    .. versionadded:: 1.3

    Control what should be logged for ANLT by xenaserver

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param types: control what should be logged for ANLT by xenaserver
    :type types: t.List[enums.AnLtLogControl]
    :return:
    :rtype:  None
    """
    conn, mid, pid = get_ctx(port)
    capabilities = await commands.P_CAPABILITIES(conn, mid, pid).get()
    type_ = 0
    for _t in types:
        type_ |= _t.value
    param = int(type_)
    for i in range(0, capabilities.serdes_count):
        await commands.PL1_CFG_TMP(
            conn,
            mid,
            pid,
            i,
            enums.Layer1ConfigType.ANLT_LOG_CONTROL
        ).set(values=[param])

async def anlt_log_control_get(port: GenericL23Port) -> dict[str, bool]:
    """
    .. versionadded:: 2.7

    Get ANLT log control config

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return: dict of log control status
    :rtype:  dict[str, bool]
    """
    conn, mid, pid = get_ctx(port)
    resp = await commands.PL1_CFG_TMP(
        conn,
        mid,
        pid,
        0,
        enums.Layer1ConfigType.ANLT_LOG_CONTROL
    ).get()

    return dictionize_anlt_log_ctrl_status(resp.values)


__all__ = (
    "anlt_link_recovery",
    "anlt_log",
    "anlt_start",
    "anlt_status",
    "anlt_stop",
    "autoneg_status",
    "lt_coeff_inc",
    "lt_coeff_dec",
    "lt_encoding",
    "lt_preset",
    "lt_status",
    "lt_trained",
    "txtap_get",
    "txtap_set",
    "txtap_autotune",
    "lt_im_status",
    "lt_algorithm_status",
    "anlt_strict",
    "anlt_log_control",
    "anlt_log_control_get",
)
