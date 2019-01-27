#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 19:16:50 2019

@author: supaul
"""

class Purger:
    def __init__(self,text):
        self.text=text
    def purge(self):
        purgedtext=''
        for ch in self.text:
            if(ch==' '):
                continue
            else:
                purgedtext+=(ch)
        return purgedtext