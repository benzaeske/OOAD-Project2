#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:34:58 2019

@author: Ben

I referenced this article for the "isinstance()" method: https://www.programiz.com/python-programming/methods/built-in/isinstance

I referenced this site for learning about Object oriented python: https://realpython.com/python3-object-oriented-programming/

I referenced this stack overflow for figuring out errors with protected attributes: https://stackoverflow.com/questions/797771/python-protected-attributes/21217121
"""

from EatBehavior import EatBehavior

#Base class for all animals. The eat behavior is implemented using the strategy pattern
class Animal():
    
    #Basic constructor 
    def __init__(self, name, eatBehavior):
        self.name = name
        self._type = None
        #The animal class is composed of an eatBehavior type. This is the first step of implementing the strategy pattern.
        self._eatBehavior = eatBehavior
    
    #Default wake up behavior for all animals
    def wake(self):
        print(self.name + " the " + self._type + " has woken up!")
    
    #Abstract makeNoise method to be implemented by subclasses
    def makeNoise(self):
        pass
    
    #Strategy pattern is used to define eat methods. Eat methods are called from the eatBehavior attribute
    def eat(self):
        self._eatBehavior.eat(self.name, self._type)
    
    #Dynamically change eatBehavior
    def changeDiet(self, eatBehavior):
        #Make sure it is a valid eating behavior
        if isinstance(eatBehavior, EatBehavior):
            self._eatBehavior = eatBehavior
    
     #Abstract roam method to be implemented by subclasses
    def roam(self):
        pass
    
    #Default sleep behavior for all animals
    def sleep(self):
        print(self.name + " the " + self._type + " has gone to bed.")
