#!/usr/local/bin python
# -*- coding:utf-8 -*-

import math
import random
from XCSConfig import *

class XCSEnvironment:
    def __init__(self):
        self.__k = conf.k
        self.__length = int(self.__k+math.pow(2,self.__k))
    def set_state(self):
        self.__state = []
        for i in xrange(self.__length):
            if random.randrange(2)==0:
                self.__state.append(0)
            else:
                self.__state.append(1)
        addbit = self.__state[0:conf.k]
        refbit = self.__state[conf.k:]
        cal = ""
        for x in range(len(addbit)):
            cal += str(addbit[x])
        ans = int(cal,2)
        self._ans = refbit[ans]
    def is_true(self,ans):
        """入力された行動が正解かどうか"""
        if self._ans == ans:
            return True
        else:
            return False
    def get_state(self):
        return self.__state
    state = property(get_state)

# for debug
# if __name__ == '__main__':
#     env = XCSEnvironment()
#     env.set_state()
#     print env.state
#     print env.is_true(1)
