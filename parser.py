#from itertools import chain
#import re
#import json
#import requests
# (52+2)*8
import math

a=str(input())
b=""
result=0
sp_num = []
sp_oper = []
for elem in a:
#    if 
    
    if elem.isdigit():
        b+=elem
    else:
        if elem == "+":
            sp_oper.append(elem)
        if elem == "-":
            sp_oper.append(elem)   
            
        sp_num.append(int(b))
        b=""
sp_num.append(int(b))
for i in range(len(sp_oper)):
    if i==0:
        if sp_oper[i] == "+":
            result += sp_num[i]+sp_num[i+1]
        if sp_oper[i] == "-":
            result += sp_num[i]-sp_num[i+1]      
    else: 
        if sp_oper[i] == "+":
            result +=sp_num[i+1]
        if sp_oper[i] == "-":
            result -=sp_num[i+1]         
print(result)