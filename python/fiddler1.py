# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
def sum1(m,n):
    sum=0;
    for i in range(n+1):
        sum+=10**i*math.comb(m,i)
    return(sum)
print(sum1(221,110)*10/10**221)