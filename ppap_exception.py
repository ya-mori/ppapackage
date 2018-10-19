

class PPAPException(Exception):
    """
    ProvidePythonAidPacker の基底Exceptionです。
    """


class EmptyCassetteException(PPAPException):
    """
    カセットがセットされていない場合にスローさせるExceptionです。
    """


class OverCassetteException(PPAPException):
    """
    すでにカセットがセットされている場合にスローさせるExceptionです。
    """


class CassetteValidateException(PPAPException):
    """
    カセットのバリデーションチェックでスローさせるExceptionです。
    """
