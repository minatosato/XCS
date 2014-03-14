#!/usr/local/bin python
# -*- coding:utf-8 -*-

import random
from XCSConfig import *
from XCSEnvironment import *
from XCSClassifier import *
from XCSClassifierSet import *

class XCSMatchSet(XCSClassifierSet):
    def __init__(self,pop,env,actual_time):
        XCSClassifierSet.__init__(self,env,actual_time)
        self.pop = pop
        for cl in self.pop.cls:
            if self.does_match(cl):
                self.cls.append(cl)
        """もし条件部の一致するClassifierで全体の行動部の種類が
        theta_mnaより小さかったらCoveringを実行し,
        env.stateと条件部の一致するClassifierを意図的に生成する."""
        while self.num_of_different_actions() < conf.theta_mna:
            cond = []
            clm = XCSClassifier(cond,actual_time)
            for i in range(len(self.env.state)):
                if random.random() < conf.p_sharp:
                    cond.append('#')
                else:
                    cond.append(self.env.state[i])
            clm.condition = cond
            clm.action = self.random_action()
            clm.experience = 0
            clm.time_stamp = actual_time
            clm.action_set_size = self.numerosity_sum() + 1
            clm.numerosity = 1
            self.pop.cls.append(clm)
            self.cls.append(clm)
            while self.pop.numerosity_sum() > conf.N:
                cl_del = pop.delete_from_population()
                if cl_del == None:
                    if cl_del in self.cls:
                        self.cls.remove(cl_del)
    def does_match(self,cl):
        """条件部が一致するか"""
        if len(cl.condition) != len(self.env.state):
            return False
        for i in range(len(cl.condition)):
            if cl.condition[i] != '#' and cl.condition[i] != self.env.state[i]:
                return False
        return True
    def num_of_different_actions(self):
        """MatchSet内のClassifierの行動部の種類数を返す"""
        a_list = []
        for cl in self.cls:
            a_list.append(cl.action)
        return len(set(a_list))
    def random_action(self):
        """MatchSetのClassifierにない行動部をランダムで返す"""
        if len(self.cls)==0:
            return random.randrange(2)
        else:
            if self.cls[0].action==1:
                return 0
            else:
                return 1
                
# for debug
# if __name__ == '__main__':
#     env = XCSEnvironment()
#     env.set_state()
#     x = XCSClassifierSet(env,1)
#     y = XCSMatchSet(x,env,1)
#     print env.state
#     for cl in y.cls:
#         print cl.condition

