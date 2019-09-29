#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:38:47 2019

@author: Ben

I referenced this article for the "isinstance()" method: https://www.programiz.com/python-programming/methods/built-in/isinstance

The article I read to learn the observer pattern in python:
-  https://sourcemaking.com/design_patterns/observer/python/1
"""
from Animal import Animal
from Observer import Observer
import abc

#Zookeeper is a subject and has zero-many observers
class Zookeeper:
    
    def __init__(self, name):
        self.name = name
        #list of observers monitoring this object
        self._observers = set()
        #state to send observers when notifying them of changes
        self._zookeeperState = None
      
    #public dayAtTheZoo method wakes, roll calls, feeds, exercises, and sleeps the animals in that order
    def dayAtTheZoo(self, animals):
        self.__wakeAnimals(animals)
        self.__rollCall(animals)
        self.__feed(animals)
        self.__exercise(animals)
        self.__shutDownZoo(animals)
    
    def __wakeAnimals(self, animals):
        #Change state and alert the observers
        self._zookeeperState = "waking"
        self._notify()
        for animal in animals:
            #Ensure no type errors occur
            if isinstance(animal, Animal):
                animal.wake()
        
    def __rollCall(self, animals):
        #Change state and alert the observers
        self._zookeeperState = "roll call"
        self._notify()
        for animal in animals:
            #Ensure no type errors occur
            if isinstance(animal, Animal):
                animal.makeNoise()
        
    def __feed(self, animals):
        #Change state and alert the observers
        self._zookeeperState = "feeding"
        self._notify()
        for animal in animals:
            #Ensure no type errors occur
            if isinstance(animal, Animal):
                animal.eat()
        
    def __exercise(self, animals):
        #Change state and alert the observers
        self._zookeeperState = "exercising"
        self._notify()
        for animal in animals:
            #Ensure no type errors occur
            if isinstance(animal, Animal):
                animal.roam()
        
    def __shutDownZoo(self, animals):
        #Change state and alert the observers
        self._zookeeperState = "shutting down"
        self._notify()
        for animal in animals:
            #Ensure no type errors occur
            if isinstance(animal, Animal):
                animal.sleep() 
                
#---------------- Subject Methods (Observer Pattern)  ------------------------

    #Add an observer to the list            
    def addObserver(self, observer):
        if isinstance(observer, Observer):
            observer._subject = self
            self._observers.add(observer)
    
    #Remove an observer from the list
    def removeObserver(self, observer):
        if isinstance(observer, Observer):
            observer._subject = None
            self._observers.remove(observer)
    
    def _notify(self):
        for observer in self._observers:
            if isinstance(observer, Observer):
                observer.update(self._zookeeperState)
                
                
                