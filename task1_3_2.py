# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

string = 'black cat';
string = string.replace(" ","");
i=0;
result = True;

while(i < len(string)//2):
    if string[i] != string[len(string)-(i+1)] :
        result = False;
        break;
    i+= 1;
    
print(result);