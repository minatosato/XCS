#!/usr/local/bin python
# -*- coding:utf-8 -*-

import math
import random
from XCSConfig import *

class XCSEnvironment:
    def __init__(self):
        self._k = conf.k
        self._length = int(self._k+math.pow(2,self._k))
    def set_state(self):
        self._state = []
        for i in xrange(self._length):
            if random.randrange(2)==0:
                self.state.append(0)
            else:
                self.state.append(1)
        addbit = self.state[0:conf.k]
        refbit = self.state[conf.k:]
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
        return self._state
    state = property(get_state)

# if __name__ == '__main__':
#     env = XCSEnvironment()
#     env.set_state()
#     print env.state
#     print env.is_true(1)
