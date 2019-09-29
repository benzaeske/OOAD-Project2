#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:21:45 2019

@author: Ben
"""
from Pachyderm import Pachyderm

class Rhino(Pachyderm):
    
    def __init__(self, name):
        super().__init__(name)
        self._type = "Rhino"
    
    #Rhino implements its own makeNoise method
    def makeNoise(self):
        print(self.name + " the " + self._type + " snorted!")