#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
*** This is the main function of the WasteFootprint tool ***

* To use the defaults, just run the whole script (but this will only work if you have the same format of project and database names)
* The terms of the search query can be edited in section 1.3 of this script
* The names of the projects and databases can be edited in section 2 of this script

DEFAULTS:

EI database is of form 'cutoff38' or 'con39'
* versions = ["35", "38", "39", "391]
* models = ["cutoff", 'con', 'apos']

The script will copy the project "default"+<db_name> to project "WasteFootprint"+<db_name>
* 'project_base': "default_"+dbase,
* 'project_waste': "WasteFootprint_"+dbase,


Created on Sat Nov 19 11:24:06 2022
@author: SC-McD
Based on the work of LL

"""
# %%% Imports
import shutil
from datetime import datetime
# custom modules
from dbExplode import dbExplode
from WasteSearch import WasteSearch
from dbMakeCustom import dbWriteExcel, dbExcel2BW
from ExchangeEditor import ExchangeEditor
from MethodEditor import AddMethods
# %% 1. DEFINE MAIN FUNCTION (EDIT YOUR SEARCH QUERY IN 1.3)


def WasteFootprint(args):

    print("\n*** Starting WasteFootprint ***\n")
    start = datetime.now()

# %%% 1.1 Define the project names and database names based on the arguments given
    project_base = args['project_base']
    project_waste = args['project_waste']
    db_name = args['db_name']
    db_waste_name = args['db_waste_name']

# %%% XX Delete files from previous runs if you want
    # #%%%% Clear program output directory: "tmp"
    # try:
    #     shutil.rmtree("data")
    #     print("tmp directory deleted\n")
    # except:
    #     print("tmp directory doesn't exist\n")

    # #%%%% Clear program output directory "WasteSearchResults"
    # try:
    #     shutil.rmtree("WasteSearchResults")
    #     print("WasteSearchResults directory deleted\n")
    # except:
    #     print("WasteSearchResults directory doesn't exist\n")

# %%% 1.2 dbExplode.py -
# Open up EcoInvent db with wurst and save results as .pickle
    print("\n*** Running dbExplode...")
    dbExplode(project_base, project_waste, db_name)

# %%% 1.3 WasteSearch.py -
# Define the search parameters here and run WasteSearch for each query (needs # to have .pickle already there from dbExplode)
# the terms should be either a string or a list of strings, as you find them

# set the names of the waste flow categories you want to search for
    names = ['digestion', 'hazardous', 'non_hazardous', "incineration",
             "open_burning", "recycling", "landfill", "composting", "total", 'radioactive']

# setup the dictionary of search terms for each waste flow category
    queries_kg = []
    for name in names:
        query = {
            "db_name": db_name,
            "db_custom": db_waste_name,
            "name": "",
            "code": "",
            "unit": "kilogram",
            "AND": ["waste"],
            # if you replace "None" below, it must be with a with a
            # list of strings, like the other keywords have
            "OR": None,
            "NOT":  None
        }

# define here what the search parameters mean for each waste flow category
# if you want to customize the search parameters, you will
# likely need some trial and error to make sure you get what you want

        query.update({"name": "waste_"+name})
        if 'landfill' in name:
            query.update({"OR": ["landfill", "dumped", "deposit"]})
        if 'hazardous' == name:
            query.update({"OR": ["hazardous", "radioactive"]})
        if 'non_hazardous' == name:
            query.update({"NOT": ["hazardous", "radioactive"]})
        if 'incineration' in name:
            query["AND"] += ["incineration"]
        if 'open_burning' in name:
            query["AND"] += ["burning"]
        if 'recycling' in name:
            query["AND"] += ["recycling"]
        if 'composting' in name:
            query["AND"] += ["composting"]
        if 'digestion' in name:
            query["AND"] += ["digestion"]
        if 'radioactive' in name:
            query["AND"] += ["radioactive"]

# add the query to the list of queries
        queries_kg.append(query)

# add same queries defined above, now for liquid waste
    queries_m3 = []
    for q in queries_kg:
        q = q.copy()
        q.update({'unit': "cubic meter"})
        queries_m3.append(q)

    queries = queries_kg + queries_m3

# run WasteSearch for the list of queries
    WasteSearch(queries)

# %%% 1.4 The rest of the custom functions:
# calls from dbMakeCustom.py, ExchangeEditor.py, MethodEditor.py
# They do pretty much what their names suggest...

# makes an xlsx file from WasteSearch results in the database format needed for brightway2
    xl_filename = dbWriteExcel(project_waste, db_name, db_waste_name)

# imports the db_waste to the brightway project "WasteFootprint_<db_name>"
    dbExcel2BW(project_waste, db_waste_name, xl_filename)

# adds waste flows as elementary exchanges to each of the activities found
    ExchangeEditor(project_waste, db_name, db_waste_name)

# adds LCIA methods to for each of the waste categories defined above
    AddMethods(project_waste, db_waste_name)

    duration = (datetime.now() - start)
    print("\n*** Finished running WasteFootprint.\n\tDuration: " +
          str(duration).split(".")[0])
    print('*** Woah woah wee waa, great success!!')


# %% 2. RUN MAIN FUNCTION
if __name__ == '__main__':

    versions = ["35"]#, "38", "39"]
    models = ["cutoff"]#, 'con', 'apos']
    dbases = ["{}{}".format(x, y) for x in models for y in versions]

    args_list = []
    for dbase in dbases:
        args = {'project_base': "default_"+dbase,
                'project_waste': "WasteFootprint_"+dbase,
                'db_name': dbase,
                'db_waste_name': "db_waste_"+dbase}
        args_list.append(args)

    for args in args_list:
        try:
            WasteFootprint(args)
        except:
            print("Something went terribly wrong :( .....skipping:"+args["db_name"])
