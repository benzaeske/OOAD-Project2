#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:28:23 2019

@author: Ben
"""

from Feline import Feline
from EatBehavior import EatsMeat

class Lion(Feline):
    
    #Lion inherets everything except its type from its super classes
    def __init__(self, name):
        #Lions eat meat. This will set the eatBehavior for lions to be EatsMeat
        eatBehavior = EatsMeat()
        super().__init__(name, eatBehavior)
        self._type = "Lion"