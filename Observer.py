#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:15:58 2019

@author: Ben

I referenced this article for the "isinstance()" method: https://www.programiz.com/python-programming/methods/built-in/isinstance

The article I read to learn the observer pattern in python:
-  https://sourcemaking.com/design_patterns/observer/python/1
"""

import abc

#Abstract observer class
class Observer(metaclass=abc.ABCMeta):
    
    def __init__(self):
        self._subject = None
        self._observerState = None
        
    @abc.abstractmethod
    def update(self, arg):
        pass
  
#Concrete observer implementations below:
    
#ZookeeperObserver definition:
class ZookeeperAnnouncer(Observer):
    
    def update(self, zookeeperState):
        self._observerState = zookeeperState
        if self._observerState == "waking":
            print("---------------\nThis is the Zookeeper Announcer!\n" 
                  + self._subject.name + " the Zookeeper is waking the animals!\n---------------")
        elif self._observerState == "roll call":
            print("---------------\nThis is the Zookeeper Announcer!\n" 
                  + self._subject.name + " the Zookeeper is roll calling the animals!\n---------------")
        elif self._observerState == "feeding":
            print("---------------\nThis is the Zookeeper Announcer!\n" 
                  + self._subject.name + " the Zookeeper is feeding the animals!\n---------------")
        elif self._observerState == "exercising":
            print("---------------\nThis is the Zookeeper Announcer!\n" 
                  + self._subject.name + " the Zookeeper is exercising the animals!\n---------------")
        else:
            print("---------------\nThis is the Zookeeper Announcer!\n" 
                  + self._subject.name + " the Zookeeper is shutting down the zoo and the animals are falling asleep!\n---------------")
        