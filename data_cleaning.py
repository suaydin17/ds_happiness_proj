# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:17:03 2023

@author: susum
"""

import pandas as pd

df= pd.read_csv("C:/Users/susum/Documents/ds_happiness_proj/world-happiness-report-2021.csv")
df.rename(columns={'Country name': 'Country'}, inplace=True)
df.rename(columns={'Regional indicator': 'Region'}, inplace=True)