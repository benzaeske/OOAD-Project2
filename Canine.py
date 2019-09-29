#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:31:42 2019

@author: Ben
"""

from Animal import Animal
import random

class Canine(Animal):
    
    def __init__(self, name, eatBehavior):
        super().__init__(name, eatBehavior)
    
    #Canine implements makeNoise but leaves eat and roam methods for subclass implementation
    def makeNoise(self):
        select = random.randint(0, 2)
        if select == 0:
            print(self.name + " the " + self._type + " let out a bark!")
        elif select == 1:
            print(self.name + " the " + self._type + " howled in the air!")
        else:
            print(self.name + " the " + self._type + " growled.")