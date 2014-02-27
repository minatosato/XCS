#!/usr/local/bin python
# -*- coding:utf-8 -*-

import math
from XCSConfig import *

class XCSClassifier:
    def __init__(self,condition,actual_time):
        self.condition = condition[:]
        self.time_stamp = actual_time
        self.numerosity = 1
        self.action_set_size = 1
        self.action = 1
        """initialization parameters{p,e,f}
        should be taken very small"""
        self.prediction = 0.01
        self.error = 0.01
        self.fitness = 0.01
    def deep_copy(self,actual_time):
        cl = XCSClassifier(self.condition,actual_time)
        cl.action = self.action
        cl.prediction = self.prediction
        cl.error = self.error
        cl.fitness = self.fitness/self.numerosity
        cl.numerosity = self.numerosity
        cl.experience = self.experience
        cl.time_stamp = actual_time
        cl.action_set_size = self.action_set_size
        return cl
    def update_fitness(self,acc_sum):
        self.fitness += conf.beta*(self.get_kappa()*self.numerosity/acc_sum-self.fitness)
    def update_parameters(self,reward,num_sum):
        self.experience += 1
        if self.experience < (1/conf.beta):
            self.prediction += (reward-self.prediction)/self.experience
        else:
            self.prediction += conf.beta*(reward-self.prediction)
        if self.experience < (1/conf.beta):
            self.error += (math.fabs(reward-self.prediction)-self.error)/self.experience
        else:
            self.error += conf.beta*(math.fabs(reward-self.prediction)-self.error)
        if self.experience < (1/conf.beta):
            self.action_set_size += (num_sum-self.action_set_size)/self.experience
        else:
            self.action_set_size += conf.beta*(num_sum-self.action_set_size)
    def deletion_vote(self,ave_fitness):
        vote = self.action_set_size*self.numerosity
        if self.experience > conf.theta_del:
            if self.fitness/self.numerosity < conf.delta*ave_fitness:
                vote *= ave_fitness/(self.fitness/self.numerosity)
        return vote
    def equals(self,cl):
        if self.condition == cl.condition:
            if self.action == cl.action:
                return True
        return False
    def does_subsume(self,cl_tos):
        if self.action == cl_tos.action:
            if self.could_subsume() and self.is_more_general(cl_tos):
                return True
        return False
    def could_subsume(self):
        if self.experience > conf.theta_sub and self.error < conf.epsilon_0:
            return True
        return False
    def is_more_general(self,cl_spec):
        ret = False
        for i in range(len(self.condition)):
            if self.condition[i] != '#' and self.condition[i] != cl_spec.condition[i]:
                return False
            elif self.condition[i] != cl_spec.condition[i]:
                ret = True
        return ret
    def get_kappa(self):
        kappa = 0.0
        if self.error < conf.epsilon_0:
            kappa = 1.0
        else:
            kappa = conf.alpha*math.pow(self.error/conf.epsilon_0,-conf.nyu)
        return kappa

# for debug
# if __name__ == '__main__':
#     a = [XCSClassifier([0,0,1],0),XCSClassifier([0,1,0],1)]
#     for cl in a:
#         cl.action += 1
#         print cl.action
