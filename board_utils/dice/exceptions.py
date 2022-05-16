from ..exceptions import BoardException


class DiceError(BoardException):
    pass


class DiceParseError(DiceError, ValueError):
    pass
