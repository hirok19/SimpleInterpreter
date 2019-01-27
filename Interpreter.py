#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:14:46 2019

@author: supaul
"""
INTEGER, PLUS, EOF,cSUB ,DIV ,MUL = 'INT', 'PLUS', 'EOF','SUB','DIV','MUL'

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
        
    def getInteger(self):
        stringInt=''
        while(self.index<len(self.text) and self.text[self.index].isdigit()):
            stringInt+=self.text[self.index]
            self.index+=1
        return int(stringInt)
    
            
        
    def getNextToken(self):
        if(self.index>=len(self.text)):
            self.index+=1
            return Token(None,'EOF')
        ch=self.text[self.index]
        ###This part needs a change
        if(ch.isdigit()):
            return Token(self.getInteger(),'INT')
        elif(ch=='+'):
            self.index+=1
            return Token(ch,'PLUS')
        elif(ch=='-'):
            self.index+=1
            return Token(ch,'SUB')
        elif(ch=='*'):
            self.index+=1
            return Token(ch,'MUL')
        elif(ch=='/'):
            self.index+=1
            return Token(ch,'DIV')
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
        self.checkOp(operatorToken,['PLUS','SUB','MUL','DIV'])
        secondToken=self.getNextToken()
        self.check(secondToken,'INT')
        eofToken=self.getNextToken()
        self.check(eofToken,'EOF')
        if(operatorToken.type=='PLUS'):
            return (firstToken.val+secondToken.val)
        elif(operatorToken.type=='MUL'):
            return (firstToken.val*secondToken.val)
        elif(operatorToken.type=='DIV'):
            return (firstToken.val/secondToken.val)
        else:
            return (firstToken.val-secondToken.val)
        

        
    
        
        