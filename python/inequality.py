#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 15:07:40 2023

@author: dan
"""
import math;import random
a= random.uniform(0.001, 1);b= random.uniform(0.00001, 3/a);
c=(3-a*b)/(a+b);print(a);print(b);print(c)
#s=9/(a+b+c+math.sqrt(a*b)+math.sqrt(b*c)+math.sqrt(a*c));
#p=9*a*b*c/(1+math.sqrt(a*b)*c+math.sqrt(a*c)*b+math.sqrt(b*c)*a)
#r=s+p-1-4/(a+b+c);
v=a+b+c+3*(a*math.sqrt(b*c)+b*math.sqrt(a*c)+c*math.sqrt(a*b))

##print(v);print(w,u)
print(v);
