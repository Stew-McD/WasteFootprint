#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
*** This script will run the whole WasteFootprint mapping thing ***

* To use the defaults, just run the whole script

* The terms of the search query can be edited in section 1.5 of this script

DEFAULTS:
    project_base='default_38' : db="cutoff38"
    project_waste='WasteFootprint_cutoff38' : db_waste="db_waste"

Created on Sat Nov 19 11:24:06 2022
@author: SC-McD
Based on the work of LL

"""
# project_base='default_cutoff38'
# project_waste='WasteFootprint_cutoff38'
# db_name="cutoff38"
# db_waste_name="db_waste_cutoff38"

#%% 1. DEFINE MAIN FUNCTION (EDIT YOUR SEARCH QUERY HERE)
def WasteFootprint(args):

    #%%% 1.1 Imports

    import shutil
    from datetime import datetime


    from dbExplode import dbExplode
    from WasteSearch import WasteSearch
    from dbMakeCustom import dbWriteExcel, dbExcel2BW
    from ExchangeEditor import ExchangeEditor
    from MethodEditor import AddMethods

    #%%% 1.2 Start
    print("\n*** Starting WasteFootprint ***\n")
    start = datetime.now()

    project_base = args['project_base']
    project_waste = args['project_waste']
    db_name = args['db_name']
    db_waste_name = args['db_waste_name']


    #%%% 1.3 Delete files from previous runs if you want
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

    #%%% 1.4 dbExplode.py - Open up EcoInvent db with wurst and save results as .pickle
    # (default is to copy "default" to project "WasteFootprint", EI database is of form "cutoff38" or 'con39')

    print("\n*** Running dbExplode...")
    dbExplode(project_base, project_waste, db_name)

    #%%% 1.5 WasteSearch.py - Define the search parameters here and run WasteSearch for each query (needs to have .pickle already there from dbExplode)
    #     terms should be either a string or a list of strings, as you find them
    names = ['digestion','hazardous', 'non_hazardous', "incineration", "open_burning", "recycling", "landfill", "composting", "total" , 'radioactive']
    queries_kg = []
    for name in names:
        query = {
                "db_name": db_name,
                "db_custom" : db_waste_name,
                "name" : "",
                "code" : "",
                "unit" : "kilogram",
                "AND" : ["waste"],
                "OR" : None, # # replace with a list of strings, like the other keywords
                "NOT" :  None # replace with a list of strings, like the other keywords
                }

        query.update({"name" : "waste_"+name})
        if 'landfill' in name: query.update({"OR" : ["landfill","dumped","deposit"]})
        if 'hazardous' == name: query.update({"OR" : ["hazardous", "radioactive"]})
        if 'non_hazardous' == name: query.update({"NOT" : ["hazardous", "radioactive"]})
        if 'incineration' in name: query["AND"] += ["incineration"]
        if 'open_burning' in name: query["AND"] += ["burning"]
        if 'recycling' in name: query["AND"] += ["recycling"]
        if 'composting' in name: query["AND"] += ["composting"]
        if 'digestion' in name: query["AND"] += ["digestion"]
        if 'radioactive' in name: query["AND"] += ["radioactive"]

        queries_kg.append(query)

    queries_m3 = []
    for q in queries_kg:
        q = q.copy()
        q.update({'unit' : "cubic meter"})
        queries_m3.append(q)

    queries = queries_kg + queries_m3
    WasteSearch(queries)

    #%%% 1.6 The rest: dbMakeCustom.py, ExchangeEditor.py, AddMethods.py - Pretty much do what their names suggest...

    xl_filename = dbWriteExcel(project_waste, db_name, db_waste_name)                      # make xlsx from WasteSearch results in bw2 db format
    dbExcel2BW(project_waste, db_waste_name, xl_filename)            # import db_waste to brightway project "WasteFootprint"

    ExchangeEditor(project_waste, db_name, db_waste_name)        # add waste flows to activities in "ei38cutoff"
    AddMethods(project_waste, db_waste_name)            # add LCIA methods to "db_waste"

    duration = (datetime.now() - start)
    print("\n*** Finished running WasteFootprint!!\n\tDuration: " + str(duration).split(".")[0])
    print('*** Woah woah wee waa, great success!!')

#%% 2. RUN MAIN FUNCTION

if __name__ == '__main__':

    versions = ["35" ,"38", "39"]
    models = ["cutoff", 'con', 'apos']
    dbases = ["{}{}".format(x,y) for x in models for y in versions]

    args_list = []
    for dbase in dbases:
        args = {'project_base':"default_"+dbase,
                'project_waste':"WasteFootprint_"+dbase,
                'db_name':dbase,
                'db_waste_name':"db_waste_"+dbase}
        args_list.append(args)

    for args in args_list:

        try:
            WasteFootprint(args)
        except:
            print("Skipping:"+args["db_name"])
