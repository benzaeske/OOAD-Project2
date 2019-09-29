#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:43:50 2019

@author: Ben
"""
from Wolf import Wolf
from Dog import Dog
from Cat import Cat
from Lion import Lion
from Tiger import Tiger
from Elephant import Elephant
from Hippo import Hippo
from Rhino import Rhino
from Zookeeper import Zookeeper
from Observer import ZookeeperAnnouncer
import sys

#Create the animals:
    
#Create the cats
cersei = Cat("Cersei");
cameron = Cat("Cameron");
#Create the Tigers
tim = Tiger("Tim");
tammy = Tiger("Tammy");
#Create the lions
leo = Lion("Leo");
lenny = Lion("Lenny");
#Create the Elephants
ella = Elephant("Ella");
ed = Elephant("Ed");
#Create the Rhinos
rea = Rhino("Rea");
rob = Rhino("Rob");
#Create the hippos
homer = Hippo("Homer");
haley = Hippo("Haley");
#Create the dogs
doug = Dog("Doug");
daniel = Dog("Daniel");
#Create the wolves
wesley = Wolf("Wesley");
wanda = Wolf("Wanda");

#Make a list of animals
zoo = [cersei, cameron, tim, tammy, leo, lenny, ella, ed, rea, rob, homer, haley, doug, daniel, wesley, wanda]


#Initialize the zookeeper, Bob
ron = Zookeeper("Ron")


#Initialize the zookeeper observer:
tammy = ZookeeperAnnouncer()

#Register the observer:
ron.addObserver(tammy)


#Redirect output to "dayatthezoo.out" (https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python)
orig_stdout = sys.stdout
f = open('dayatthezoo.out', 'w')
#sys.stdout = f

#Start a day at the zoo!
ron.dayAtTheZoo(zoo)

#Restore stdout to console
sys.stdout = orig_stdout

