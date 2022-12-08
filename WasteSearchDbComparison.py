#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:30:22 2022

@author: stew
"""

import pandas as pd
import os


path = os.getcwd() + "/WasteSearchResults"


files = []
for p, s, fs in os.walk("/home/stew/scripts/gh/WasteDemand/WasteSearchResults"):
        for f in fs:
            if ".csv" in f and "Waste" not in f:
                files.append(f)


files.sort(reverse=True)




col_names = ["ex_code", "ex_name" , "ex_loc" , "ex_amount", "ex_unit" , "db_name", "category"]
results = pd.DataFrame(columns=col_names)

for file in files:

    result = pd.read_csv((path +"/"+ file), sep=";", header=None)
    col_names = ["ex_code", "ex_name" , "ex_loc" , "ex_amount", "ex_unit" , "db_name"]
    result = result.set_axis(col_names, axis=1)
    result.insert(0, "category", file.split("_")[1])
    results = pd.concat([results, result])





unique = results.drop_duplicates(subset=['ex_name'], keep='last')


results.to_csv((path+ "/WasteSearchCombined.csv"), sep=";", header=True)
unique.to_csv((path+ "/WasteSearchCombined_UniqueName.csv"), sep=";", header=True)


#%% Compare with ei3.8

# file ='/home/stew/scripts/gh/WasteDemand/WasteSearchResults/WasteSearchUniqueNames.csv'
# unique38 = pd.read_csv((file), sep=";", index_col=0)

# print("Unique names in cutoff38:", len(unique38), ",in cutoff39:", len(unique))
# unique_combined = results = pd.concat([unique, unique38])
# unique_difference = unique_combined.drop_duplicates(subset=['ex_name'], keep='first')
# unique_difference.to_csv((path+ "/WasteSearchUnique38vs39.csv"), sep=";", header=True)
# print(unique_difference.ex_name)
