#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:09:59 2019

@author: Ben
"""

from Canine import Canine
from EatBehavior import EatsRabbit

class Wolf(Canine):
    
    def __init__(self, name):
        #Wolves eat rabbit. This will set the eatBehavior for lions to be EatsRabbit
        eatBehavior = EatsRabbit()
        super().__init__(name, eatBehavior)
        self._type = "Wolf"
    
    #Wolf implements its own roam method    
    def roam(self):
        print(self.name + " the " + self._type + " inspected their territory.")
        
        