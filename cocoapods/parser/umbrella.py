#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "zhengqi"

import os, re
from functools import cached_property

class Umbrella:
    """
    解析 umbrella header 头文件声明
    """
    def __init__(self, path: str) -> None:
        self.__umbrella_file = os.path.expanduser(path)

    @cached_property
    def imports(self) -> set[str]:
        """
        提取所有 import 语句
        """
        imports = set()
        with open(self.__umbrella_file) as file:
            for line in file.readlines():
                header = re.match(r'#import\s"(\S+)"', line)

                if not header: continue
                imports.add(header[1])

        return imports

    @property
    def module(self):
        """
        返回所属 module
        """
        return os.path.basename(
            os.path.dirname(self.__umbrella_file)
        )