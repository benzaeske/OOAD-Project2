#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:09:45 2019

@author: Ben
"""

from Canine import Canine
from EatBehavior import EatsKibble

class Dog(Canine):
    
    def __init__(self, name):
        #Dogs eat kibble. This will set the eatBehavior for dogs to be EatsKibble
        eatBehavior = EatsKibble()
        super().__init__(name, eatBehavior)
        self._type = "Dog"

     
    #Dog implements its own roam method
    def roam(self):
        print(self.name + " the " + self._type + " played with their new toy!")