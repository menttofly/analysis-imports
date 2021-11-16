#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "zhengqi"

from abc import ABC, abstractmethod, abstractproperty
from cocoapods.sandbox import PodsSandbox

class Plugin(ABC):
    """
    Pipeline 处理文件
    """
    @abstractmethod
    def __init__(self, sanbox: PodsSandbox):
        pass

    @abstractmethod
    def process(self, pod: str, input_file: str):
        """
        执行 import、module 替换等操作
        """
        pass

    @abstractproperty
    def ouput(self) -> str:
        """
        输出分析结果（如有）
        """
        pass