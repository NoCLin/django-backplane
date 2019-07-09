# -*- coding: utf-8 -*-
from abc import ABCMeta


class BaseError(Exception):
    __metaclass__ = ABCMeta
    code = 999999
    status = 500
    message = "未知错误"

    def __init__(self, data):
        self.data = data


class UnknownError(BaseError):
    pass
