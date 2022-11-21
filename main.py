#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script will run the whole thing

Created on Sat Nov 19 11:24:06 2022

@author: SC-McD


"""

#%% Imports

import shutil
from datetime import datetime
from dbExplode import dbExplode
from WasteSearch import WasteSearch
from dbMakeCustom import dbWriteExcel, dbExcel2BW
from ExchangeEditor import ExchangeEditor
from AddMethods import AddMethods


#%% Start
print("\n*** Starting WasteDemand ***\n")
start = datetime.now()

#%% Delete files from previous runs
#%%% Clear program output directory: "tmp"
try:
    shutil.rmtree("tmp")
    print("tmp directory deleted\n")
except:
    print("tmp directory doesn't exist\n")

#%%% Clear program output directory "WasteSearchResults"
try:
    shutil.rmtree("WasteSearchResults")
    print("WasteSearchResults directory deleted\n")
except:
    print("WasteSearchResults directory doesn't exist\n")

#%% Open up EcoInvent db with wurst and save results as .pickle
# (default is to copy "default" to project "WasteDemand", EI is "cutoff38")

print("\n*** Running dbExplode...")
dbExplode()

#%% Define the search parameters here and run WasteSearch for each query (needs to have .pickle already there from dbExplode)

names = ['digestion','hazardous', 'non_hazardous', "incineration", "openburn", "recycled", "dump", "compost", "total" ]

for name in names:
    query = {
            "db_custom" : "db_waste",
            "name" : "",
            "code" : "",
            "keywords_AND" : ["waste"],
            "keywords_OR" : [""],
            "keywords_NOT" : ["somethingyoudontwant"] # It works as is, but I should to change this
            }

    query.update({"name" : "waste_"+name})
    if 'dump' in name: query.update({"keywords_OR" : ["landfill","opendump","underground deposit"]})
    if 'hazardous' == name: query.update({"keywords_OR" : ["hazard", "radioactiv"]})
    if 'non_hazardous' == name: query.update({"keywords_NOT" : ["hazard", "radioactiv"]})
    if 'incineration' in name: query["keywords_AND"] += ["inciner"]
    if 'openburn' in name: query["keywords_AND"] += ["burn"]
    if 'recycled' in name: query["keywords_AND"] += ["recycl"]
    if 'compost' in name: query["keywords_AND"] += ["compost"]
    if 'digest' in name: query["keywords_AND"] += ["digest"]

    WasteSearch(query)

#%% The rest...

dbWriteExcel()          # make xlsx from WasteSearch results in bw2 db format
dbExcel2BW()            # import db_waste to brightway project "WasteDemand"
ExchangeEditor()        # add waste flows to activities in "ei38cutoff"
AddMethods()            # add LCIA methods to "db_waste"

duration = (datetime.now() - start)
print("\n*** Finished running WasteDemand!!\nDuration: " + str(duration).split(".")[0])
