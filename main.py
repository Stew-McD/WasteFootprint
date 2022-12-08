#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
*** This script will run the whole WasteDemand mapping thing ***

* To use the defaults, just run the whole script

* The terms of the search query can be edited in section 1.5 of this script

DEFAULTS:
    project_base='default_38' : db="cutoff38"
    project_waste='WasteDemand_38' : db_waste="db_waste"

Created on Sat Nov 19 11:24:06 2022
@author: SC-McD
Based on the work of LL

"""
# project_base='default_38'
# project_waste='WasteDemand_38'
# db_name="cutoff38"
# db_waste_name="db_waste_cutoff38"

#%% 1. DEFINE MAIN FUNCTION (EDIT YOUR SEARCH QUERY HERE)
def WasteDemand(project_base='default_38', project_waste='WasteDemand_38', db_name="cutoff38", db_waste_name="db_waste_cutoff38"):

    #%%% 1.1 Imports

    import shutil
    from datetime import datetime

    from dbExplode import dbExplode
    from WasteSearch import WasteSearch
    from dbMakeCustom import dbWriteExcel, dbExcel2BW
    from ExchangeEditor import ExchangeEditor
    from AddMethods import AddMethods


    #%%% 1.2 Start
    print("\n*** Starting WasteDemand ***\n")
    start = datetime.now()

    #%%% 1.3 Delete files from previous runs if you want
    # #%%%% Clear program output directory: "tmp"
    # try:
    #     shutil.rmtree("tmp")
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
    # (default is to copy "default" to project "WasteDemand", EI is "cutoff38")

    print("\n*** Running dbExplode...")
    dbExplode(project_base, project_waste, db_name)

    #%%% 1.5 WasteSearch.py - Define the search parameters here and run WasteSearch for each query (needs to have .pickle already there from dbExplode)
    #     terms should be either a string or a list of strings, as you find them


    names = ['digestion','hazardous', 'non-hazardous', "incineration", "open-burning", "recycled", "dumped", "compost", "total" ]
    args_search = []
    for name in names:
        query = {
                "db_custom" : db_waste_name,
                "name" : "",
                "code" : "",
                "keywords_AND" : ["waste"],
                "keywords_OR" : [""],
                "keywords_NOT" : ["placeholderforsomethingyoudontwant"] # replace with a list of strings, like the other keywords
                }

        query.update({"name" : "waste_"+name})
        if 'dumped' in name: query.update({"keywords_OR" : ["landfill","opendump","underground deposit"]})
        if 'hazardous' == name: query.update({"keywords_OR" : ["hazard", "radioactiv"]})
        if 'non-hazardous' == name: query.update({"keywords_NOT" : ["hazard", "radioactiv"]})
        if 'incineration' in name: query["keywords_AND"] += ["inciner"]
        if 'open-burning' in name: query["keywords_AND"] += ["burn"]
        if 'recycled' in name: query["keywords_AND"] += ["recycl"]
        if 'compost' in name: query["keywords_AND"] += ["compost"]
        if 'digest' in name: query["keywords_AND"] += ["digest"]

        arg_search = {"query":query, "db_name":db_name}
        args_search.append(arg_search)

    for a in args_search:
        WasteSearch(**a)


    #%%% 1.6 The rest: dbMakeCustom.py, ExchangeEditor.py, AddMethods.py - Pretty much do what their names suggest...

    xl_filename = dbWriteExcel(project_waste, db_name, db_waste_name)                      # make xlsx from WasteSearch results in bw2 db format
    dbExcel2BW(project_waste, db_waste_name, xl_filename)            # import db_waste to brightway project "WasteDemand"

    ExchangeEditor(project_waste, db_name, db_waste_name)        # add waste flows to activities in "ei38cutoff"
    AddMethods(project_waste, db_waste_name)            # add LCIA methods to "db_waste"

    duration = (datetime.now() - start)
    print("\n*** Finished running WasteDemand!!\n\tDuration: " + str(duration).split(".")[0])
    print('*** Woah woah wee waa, great success!!')

#%% 2. RUN MAIN FUNCTION

if __name__ == '__main__':

    versions = ["38", "39"]
    models = ["cutoff", 'con']
    dbases = ["{}{}".format(x,y) for x in models for y in versions]

    args = []
    for dbase in dbases:
        arg = {'project_base':"default_"+dbase[-2:], 'project_waste':"WasteDemand_"+dbase, 'db_name':dbase, 'db_waste_name':"db_waste_"+dbase}
        args.append(arg)

    #LCIAcalculations(project="WasteDemand_mp_"+dbase, db_name=dbase, method_key="waste_")
    WasteDemand(**args)


#%% Single jobs
# WasteDemand(project_base='default_38', project_waste='WasteDemand_38_cutoff', db_name="cutoff38", db_waste_name="db_waste_cutoff38")
# WasteDemand(project_base='default_38', project_waste='WasteDemand_38_con', db_name="con38", db_waste_name="db_waste_con38")
# WasteDemand(project_base='default_39', project_waste='WasteDemand_39_cutoff', db_name="cutoff39", db_waste_name="db_waste_cutoff39")
# WasteDemand(project_base='default_39', project_waste='WasteDemand_39_con', db_name="con39", db_waste_name="db_waste_con39")
