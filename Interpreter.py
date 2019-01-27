#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:14:46 2019

@author: supaul
"""
INTEGER, PLUS, EOF,SUB = 'INT', 'PLUS', 'EOF','SUB'

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
        elif(ch=='-'):
            self.index+=1
            return Token(ch,'SUB')
        else:
            self.throwError()
            
            
        
        
    def check(self,token,tokentype):
        if(token.type!=tokentype):
            self.throwError()
    def checkOp(self,token,tokentypeArr):
        check=False
        for tokentype in tokentypeArr:
            if(token.type==tokentype):
                check=True
        if(check==False):
            self.throwError()
        
        
        
    def expr(self):
        firstToken=self.getNextToken()
        self.check(firstToken,'INT')
        operatorToken=self.getNextToken()
        self.checkOp(operatorToken,['PLUS','SUB'])
        secondToken=self.getNextToken()
        self.check(secondToken,'INT')
        eofToken=self.getNextToken()
        self.check(eofToken,'EOF')
        if(operatorToken.type=='PLUS'):
            return (firstToken.val+secondToken.val)
        else:
            return (firstToken.val-secondToken.val)
        

        
    
        
        