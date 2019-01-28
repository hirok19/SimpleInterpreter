#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:09:59 2019

@author: supaul
"""
from Interpreter import *
from Purger import *
import os 
def main():
    while True:
        try:
            text = input('pascal> ')
            purger=Purger(text)
            text=purger.purge()
            if(text=="EXIT"):
                break
            if(text=="CLEAR"):
                os.system('clear')
                continue
            interpreter = Interpreter(text)
            result = interpreter.expr()
            print(result)
        except Exception as e:
            print(e)
            print("Unable to Parse Expression")
    
    
if __name__ == '__main__':
     main()