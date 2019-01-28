#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:52:02 2019

@author: supaul
"""

from stack import *

class PostFixEvaluator:
    def __init__(self,postfixexpr):
        self.postfixexpr=postfixexpr
    def evaluate(self):
        """
        1) Create a stack to store operands (or values).
        2) Scan the given expression and do following for every scanned element.
            …..a) If the element is a number, push it into the stack
            …..b) If the element is a operator, pop operands for the operator from stack. Evaluate the operator and push the result back to the stack
        3) When the expression is ended, the number in the stack is the final answer
        """
        stack=Stack()
        for token in self.postfixexpr:
            if(token.type=='INT'):
                stack.push(token.val)
            else:
                tok1=stack.pop()
                tok2=stack.pop()
                if(token.type=='PLUS'):
                    stack.push(tok1+tok2)
                if(token.type=='SUB'):
                    stack.push(tok2-tok1)
                if(token.type=='MUL'):
                    stack.push(tok1*tok2)
                if(token.type=='DIV'):
                    stack.push(tok2/tok1)
        return stack.top()