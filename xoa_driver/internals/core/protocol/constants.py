from enum import IntEnum
from typing import Final


NOTHING: Final = 0xFF
WILDCARD: Final = 0xFE
NOVALUE: Final = "N/A"
MAGIC_WORD: Final = b"XENA"
# MAGIC_WORD = 0x58454E41

class CommandType(IntEnum):
    """BXMP request type"""

    COMMAND_CHAIN = 1
    COMMAND_QUERY = 2
    COMMAND_VALUE = 3
    COMMAND_STATUS = 4


class CommandStatus(IntEnum):
    """Status codes in BXMP response message to request type <COMMAND_STATUS = 4>"""

    OK = 0  # OK
    NOCONNECTIONS = 1  # chassis has no available connection slots
    NOTLOGGEDON = 2  # no command can be submitted before logon
    NOTRESERVED = 3  # parameter cannot be set because containing resource not reserved
    NOTWRITABLE = 4  # parameter cannot be set because it is not in a writable state
    NOTREADABLE = 5  # parameter is write-only
    NOTVALID = 6  # operation not valid in current state
    BADHEADER = 7  # invalid magic word
    BADCOMMAND = 8  # invalid command
    BADPARAMETER = 9  # invalid parameter code
    BADMODULE = 10  # invalid module index
    BADPORT = 11  # invalid port index
    BADINDEX = 12  # invalid parameter index
    BADSIZE = 13  # invalid size of data
    BADVALUE = 14  # invalid value of data
    FAILED = 15  # failed to perform operation
    MEMORYFAILURE = 16  # failed to allocate memory
    NOLICPE = 17  # no free PE license
    NOLICPORT = 18  # no free Port license
    NOTSUPPORTED = 19  # feature not supported
    PENDING = 20  # status return will wait until command has been executed
    MODULE_OPERATION_NOT_SUPPORTED_BY_CHASSIS = 21  # module is not supported by chassis - e.g. because multi-image requires x64 OS.
    XLSFAILED = 22  # could not establish connection to Xena License Server
    XLSDENIED = 23  # request for resource rejected by Xena License Server
    XLSINVALID = 24 # Trying to run Valkyrie VE with VulcanVE-300 resource