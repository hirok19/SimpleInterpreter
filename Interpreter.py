#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:14:46 2019

@author: supaul
"""
INTEGER, PLUS, EOF = 'INT', 'PLUS', 'EOF'

class Token:
    def __init__(self,value,tokenType):
        self.val=value
        self.type=tokenType
    

class Interpreter:
    def __init__(self,text):
        self.text=text
        self.index=0
    def throwError(self):
        raise Exception("Error parsing Input")
    def getNextToken(self):
        if(self.index>=len(self.text)):
            self.index+=1
            return Token(None,'EOF')
        ch=self.text[self.index]
        if(ch.isdigit()):
            self.index+=1
            return Token(int(ch),'INT')
        elif(ch=='+'):
            self.index+=1
            return Token(ch,'PLUS')
        else:
            self.throwError()
            
            
        
        
    def check(self,token,tokentype):
        if(token.type!=tokentype):
            self.throwError()
        
        
        
        
    def expr(self):
        firstToken=self.getNextToken()
        self.check(firstToken,'INT')
        plusToken=self.getNextToken()
        self.check(plusToken,'PLUS')
        secondToken=self.getNextToken()
        self.check(secondToken,'INT')
        eofToken=self.getNextToken()
        self.check(eofToken,'EOF')
        return (firstToken.val+secondToken.val)
        

        
    
        
        