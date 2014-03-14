#!/usr/local/bin python
# -*- coding:utf-8 -*-

import random
from XCSConfig import *
from XCSEnvironment import *
from XCSClassifier import *

class XCSClassifierSet:
    def __init__(self,env,actual_time):
        self.env = env
        self.actual_time = actual_time
        self.cls = []
    def deep_copy(self):
        clset = XCSClassifierSet(self.env,self.actual_time)
        clset.cls = self.cls
        return clset
    def accuracy_sum(self):
        return sum(cl.get_kappa()*cl.numerosity for cl in self.cls)
    def fitness_sum(self):
        return sum(cl.fitness for cl in self.cls)
    def numerosity_sum(self):
        return sum(cl.numerosity for cl in self.cls)
    def ts_num_sum(self):
        return sum(cl.time_stamp*cl.numerosity for cl in self.cls)
    def error_sum(self):
        return sum(cl.error for cl in self.cls)
    def delete_from_population(self):
        """ルーレット選択でdeletion_vote()の
        大きいClassifierを確率的に削除"""
        ave_fitness = self.fitness_sum()/float(self.numerosity_sum())
        vote_sum = sum(cl.deletion_vote(ave_fitness) for cl in self.cls)
        choice_point = vote_sum * random.random()
        vote_sum = 0.0
        i = 0
        for cl in self.cls:
            vote_sum += cl.deletion_vote(ave_fitness)
            if vote_sum > choice_point:
                cl.numerosity -= 1
                if cl.numerosity == 0:
                    self.remove_classifier(i)
                return cl
            i += 1
        return None
    def remove_classifier(self,num):
        try:
            del self.cls[num]
        except IndexError:
            raise
        return True
    def remove_classifier_by_instance(self,cl):
        try:
            self.cls.remove(cl)
            return True
        except ValueError:
            raise
    def insert_in_population(self,cl):
        for c in self.cls:
            if c.equals(cl):
                c.numerosity += 1
                return
        self.cls.append(cl)

# for debug
# if __name__ == '__main__':
#     env = XCSEnvironment()
#     env.set_state()
#     x = XCSClassifierSet(env,1)
#     x.insert_in_population(XCSClassifier([0,0,0],1))
#     x.insert_in_population(XCSClassifier([0,0,0],1))
#     x.insert_in_population(XCSClassifier([0,0,0],1))
#     x.insert_in_population(XCSClassifier([0,0,0],1))
#     x.insert_in_population(XCSClassifier([0,0,0],1))
#     print len(x.cls)

