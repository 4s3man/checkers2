class BoardException(Exception):
    pass


class NoCoinException(BoardException):
    pass


class OutOfBoardException(BoardException):
    pass


class InvalidUsageException(Exception):
    pass
