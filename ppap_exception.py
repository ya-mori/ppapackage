

class PPAPError(Exception):
    """
    ProvidePythonAidPacker の基底Exceptionです。
    """


class EmptyCassetteError(PPAPError):
    """
    カセットがセットされていない場合にスローさせるExceptionです。
    """


class OverCassetteError(PPAPError):
    """
    すでにカセットがセットされている場合にスローさせるExceptionです。
    """


class CassetteValidateError(PPAPError):
    """
    カセットのバリデーションチェックでスローさせるExceptionです。
    """
