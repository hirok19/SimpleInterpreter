#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:09:59 2019

@author: supaul
"""
from Interpreter import *

def main():
    while True:
        text = input('pascal> ')
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)
    
    
if __name__ == '__main__':
    main()