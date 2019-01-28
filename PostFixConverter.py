#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:03:48 2019

@author: supaul
"""
from stack import *
class PostFixConverter:
    def __init__(self,listOfToken):
         self.listOfToken=listOfToken
         
    def getPriority(self,tokenType):
        if(tokenType=='PLUS'):
            return 1
        if(tokenType=='SUB'):
            return 1
        if(tokenType=='MUL'):
            return 2
        if(tokenType=='DIV'):
            return 2
        
    def convertPostFix(self):
        postfix=[]
        stack=Stack()
        #print("I am here")
        for token in self.listOfToken:
            if(token.type=='INT'):
                postfix.append(token)
            else:
                '''
                while(st.top() != 'N' && prec(s[i]) <= prec(st.top())) 
            { 
                char c = st.top(); 
                st.pop(); 
                ns += c; 
            } 
            st.push(s[i]); 
                '''
                
                while((not stack.isEmpty()) and self.getPriority(token.type)<=self.getPriority(stack.top().type)):
                    tok=stack.pop()
                    postfix.append(tok)
                stack.push(token)
        while(not stack.isEmpty()):
            postfix.append(stack.pop())
          
                
        return postfix 