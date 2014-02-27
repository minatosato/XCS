#!/usr/local/bin python
# -*- coding:utf-8 -*-

import random
from XCSConfig import *
from XCSEnvironment import *
from XCSClassifier import *
from XCSClassifierSet import *
from XCSMatchSet import *

class XCSActionSet(XCSClassifierSet):
    def __init__(self,match_set,action,env,actual_time):
        XCSClassifierSet.__init__(self,env,actual_time)
        self.action = action
        for cl in match_set.cls:
            if cl.action == self.action:
                self.cls.append(cl)
    def do_action(self):
        if self.env.is_true(self.action):
            self.reward = 1000
        else:
            self.reward = 0
    def update_action_set(self):
        num_sum = self.numerosity_sum()
        for cl in self.cls:
            cl.update_parameters(self.reward,num_sum)
        acc_sum = self.accuracy_sum()
        for cl in self.cls:
            cl.update_fitness(acc_sum)
    def do_action_set_subsumption(self,pop):
        if conf.doActionSetSubsumtion:
            subsumber = None
            for cl in self.cls:
                if cl.could_subsume():
                    if subsumber==None or cl.is_more_general(subsumber):
                        subsumber = cl
            if subsumber!=None:
                i=0
                while i<len(self.cls):
                    if subsumber.is_more_general(self.cls[i]):
                        subsumber.numerosity += self.cls[i].numerosity
                        pop.remove_classifier_by_instance(self.cls[i])
                        self.remove_classifier(i)
                        i -= 1
                    i += 1

# if __name__ == '__main__':
#     random.seed(3)
#     env = XCSEnvironment()
#     env.set_state()
#     x = XCSClassifierSet(env,1)
#     y = XCSMatchSet(x,env,1)
#     print env.state
#     for cl in y.cls:
#         print cl.condition
#     print "\n"
#     a = XCSActionSet(y,1,env,1)
#     for cl in a.cls:
#         print cl.condition
