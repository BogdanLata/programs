#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:51:44 2023

@author: dan
"""
import locale
import re

# initialize the locale module with the user's preferred locale
locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')

with open('/home/dan/Desktop/Unified small files/python/ptext', 'r') as file:
    text = file.read()
text_array = text.split("///")



def delete_non_alphabetical(item):
    # Delete the first non-alphabetical characters using regular expression
    return re.sub(r'^[^a-zA-Z]+', '', item)

modified_items = [delete_non_alphabetical(item) for item in text_array]


sorted_array = sorted(modified_items, key=lambda x: x.lower())
sorted_text = "///".join(sorted_array)

with open('/home/dan/Desktop/Unified small files/python/ptext', 'w') as file:
    file.write(sorted_text)

print(sorted_text)
