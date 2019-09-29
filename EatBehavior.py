#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:27:09 2019

@author: Ben

Articles I used for learning the strategy pattern in python: 
-  https://medium.com/@sheikhsajid/design-patterns-in-python-part-1-the-strategy-pattern-54b24897233e
-  https://refactoring.guru/design-patterns/strategy/python/example

This is where the Strategy pattern classes are created.
"""
#a library for python which allows creation of "abstract base classes" (abc's)
import abc

#This is the EatBehavior abstract class
class EatBehavior():
    
    #All EatBehaviors require an eat method
    @abc.abstractmethod
    def eat(self, name, animalType):
        pass
        
#Concrete EatBehavior implementations are below

#Eat behavior for pachyderms
class EatsVeggies(EatBehavior):
    
    def eat(self, name, animalType):
        print(name + " the " + animalType + " ate all their veggies!")

#Eat behavior for lions and tigers       
class EatsMeat(EatBehavior):
    
    def eat(self, name, animalType):
        print(name + " the " + animalType + " ate their meat.")
        
#Eat behavior for dogs      
class EatsKibble(EatBehavior):
    
    def eat(self, name, animalType):
        print(name + " the " + animalType + " ate their kibble.")
        
#Eat behavior for cats      
class EatsTuna(EatBehavior):
    
    def eat(self, name, animalType):
        print(name + " the " + animalType + " ate their tuna.")
        
#Eat behavior for wolves      
class EatsRabbit(EatBehavior):
    
    def eat(self, name, animalType):
        print(name + " the " + animalType + " ate their rabbit meat.")
    