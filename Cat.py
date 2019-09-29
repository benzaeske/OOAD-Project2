#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:28:13 2019

@author: Ben
"""

from Feline import Feline
from EatBehavior import EatsTuna

class Cat(Feline):
    
    def __init__(self, name):
        #Cats eat tuna. This will set the eatBehavior for cats to be EatsTuna
        eatBehavior = EatsTuna()
        super().__init__(name, eatBehavior)
        self._type = "Cat"
    
    #Cat overrides makeNoise inherited from Feline
    def makeNoise(self):
        print(self.name + " the " + self._type + " meowed enthusiastically.")