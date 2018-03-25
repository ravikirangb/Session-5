# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:33:06 2018

@author: 1000091
"""
import os

try :
    a = 5/0
    
except ZeroDivisionError as err:
    print ("5 is not divisible by 0")