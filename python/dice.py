#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 21:49:22 2023

@author: dan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:11:23 2023

@author: dan
"""
# https://thefiddler.substack.com/p/can-you-flip-the-coins-exactly-as

import os
import time


# Clear the console or terminal (platform-dependent)
os.system('cls' if os.name == 'nt' else 'clear')


from scipy.stats import multinomial
import numpy as np

rv = multinomial(8, [1/8, 3/8,3/8,1/8])
outcomes = []
probabilities = []

for i in range(9):
    print(i);
    for j in range(9-i):
        for k in range(9-j-i):
           l=8-i-j-k;
           outcome = [i, j, k, l]
           probability = rv.pmf(outcome) 
           print(f'Outcome ({i}, {j}, {k}, {8 - i - j - k}): {probability}')
           outcomes.append(outcome)
           probabilities.append(probability)

# Get the indices that would sort the probabilities in descending order
sorted_indices = np.argsort(probabilities)[::-1]

# Print the sorted outcomes and probabilities
#for i in sorted_indices:
 # print(f'Outcome {outcomes}: Probability {probabilities}')
 
sorted_outcomes = [sorted(outcome,reverse=True) for outcome in outcomes]  
 
 
from collections import defaultdict

# Create a dictionary to store indices for each unique value
indices_by_value = defaultdict(list)

# Populate the dictionary
for i, sorted_outcome in enumerate(sorted_outcomes):
    indices_by_value[tuple(sorted_outcome)].append(i)
    
    
# Create a dictionary to store the sum of probabilities for each key
sum_probabilities_by_key = {}

# Calculate the sum of probabilities for each key
for key, indices in indices_by_value.items():
    sum_probabilities = sum(probabilities[i] for i in indices)
    sum_probabilities_by_key[key] = sum_probabilities
    
sorted_sum_probabilities = dict(sorted(sum_probabilities_by_key.items(), key=lambda item: item[1], reverse=False))

s=sum_probabilities_by_key

sortedp=sorted(sum_probabilities_by_key.items(),key=lambda x:x[1],reverse=True)


print(type(s[0,0,0,8]))

rv = multinomial(16, [1/16,4/16,6/16,4/16,1/16])
outcomes = []
probabilities = []

for i in range(17):
    for j in range(17-i):
        for k in range(17-j-i):
            for s in range(17-i-j-k):
             l=16-i-j-k-s;
             outcome = [i, j, k, s,l]
             probability = rv.pmf(outcome) 
             print(f'Outcome ({i}, {j}, {k}, {s},{l}): {probability}')
             outcomes.append(outcome)
             probabilities.append(probability)
             
my_dict = {(0, 0, 0, 8): 0.0007822513580322283,
           (0, 0, 1, 7): 0.010435104370117205,
           (0, 0, 2, 6): 0.02682971954345706,
           (0, 0, 3, 5): 0.047410964965820354,
           (0, 0, 4, 4): 0.028730630874633838,
           (0, 1, 1, 6): 0.034166336059570326}

# Sort the dictionary by values
a = sorted(my_dict.items(), key=lambda x: x[1])    
# Print the sorted dictionary
print(sorted_dict_by_values)
for index, value in enumerate(my_dict.values()):
    print(f"Index: {index}, Value: {value}")


