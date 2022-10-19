# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

string = 'taco cat';
i=0;
result = True;

while(i < len(string)//2):
    if string[i] != string[len(string)-(1+i)] :
        result = False;
        break;
    i+= 1;
