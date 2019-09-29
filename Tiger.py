#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:28:34 2019

@author: Ben
"""
from Feline import Feline
from EatBehavior import EatsMeat

class Tiger(Feline):
    
    #Tiger inherets everything except its type from its superclasses
    def __init__(self, name):
        #Tigers eat meat. This will set the eatBehavior for tigers to be EatsMeat
        eatBehavior = EatsMeat()
        super().__init__(name, eatBehavior)
        self._type = "Tiger"