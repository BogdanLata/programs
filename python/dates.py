#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:51:40 2023

@author: dan
"""
"""Checks the eldest and youngest data in Trade date column between data csv files
so that there are no redundancies"""
import pandas as pd
#from datetime import datetime
import pickle, io

#Use pickle to transfer dataframes to other scripts
fp.seek(0)    # necessary to start reading at the beginning of the "file"
dg = pickle.load(fp)
# Load your CSV file or data into a pandas DataFrame
# Replace 'your_data.csv' with the path to your CSV file

# Replace 'Date' with the name of the column containing dates
date_column = 'Trade date'

# Convert the date column to datetime objects
dg[date_column] = pd.to_datetime(dg[date_column], format='%d/%m/%Y')  # Adjust the date format as needed

# Find the oldest and youngest dates
oldest_date = dg[date_column].min()
youngest_date = dg[date_column].max()

print(f"Oldest Date in '{date_column}': {oldest_date.strftime('%Y-%m-%d')}")
print(f"Youngest Date in '{date_column}': {youngest_date.strftime('%Y-%m-%d')}")

