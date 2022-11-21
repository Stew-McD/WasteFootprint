#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WasteSearch() loads '<db name>_exploded.pickle', runs the search query, and produces a .csv to store the results (and a log entry). 
The query is a dictionary that holds the variables NAME, CODE, and the search terms keywords_AND keywords_OR and keywords_NOT. 
The format of the query dictionary is in main.py. Edit the query with query.update[{ '<parameter>' : '<value>'}]
The function will iterate over UNIT = 'kilogram' and UNIT = 'cubic meter'.

Created on Wed Nov 16 15:09:03 2022

@author: SC-McD
based on the work of LL
"""

#%%% Define waste search function

def WasteSearch(query):
 
    import os
    import pandas as pd
    from datetime import datetime

        # for readability
    NAME_BASE = query["name"]
    AND = query["keywords_AND"]
    OR = query["keywords_OR"]
    NOT = query["keywords_NOT"]

    print("\n\n*** Running WasteSearch for:", NAME_BASE, "AND:", AND, "OR:", OR, "NOT:", NOT)
        # make new folder to store results    
    search_results_path = os.path.join(os.getcwd(), 'WasteSearchResults')    
    if not os.path.exists(search_results_path): os.mkdir(search_results_path)
    
    
        # repeat each search for kg and m3
    units = ["kilogram","cubic meter"]
    for UNIT in units:
        NAME = NAME_BASE + "_" + UNIT
        CODE = NAME.replace(" ", "")
        query.update({"name" : NAME})
        query.update({"code" : NAME})
        query.update({'unit' : UNIT})
        
        
            # time, etc
        start = datetime.now()
        time = start.strftime("%y%m%d-%H%M")
                
            # csv file for each query
        waste_file_name = NAME.replace(" ", "") + ".csv"
        waste_file = os.path.join(search_results_path, waste_file_name) 
   
            # load exchanges into df from the DBexplode pickle file
        tmp = os.path.join(os.getcwd(),"tmp")
        for f in os.listdir(tmp): 
            if "exploded.pickle" in f : 
                pickle_path = os.path.join(tmp , f)
                db_name = f.split("_")[0]
        df = pd.read_pickle(pickle_path)
        
            # iterate through each exchange in the exploded df of EcoInvent
        count = 0
        for i in range(0, df.shape[0]):
            
            rowSeries = df.iloc[i, 1]     # get row contents as series using iloc{]
            rowSeries['process code']= df.iloc[i,0]     # and index position of row
            
                # to increase readability
            ex_name = str(rowSeries['name'])
            ex_unit = str(rowSeries['unit'])
            ex_amount = str(rowSeries['amount'])
            ex_code = str(rowSeries['process code'])
            ex_loc = str(rowSeries['location'])
            
                # test the exchanges against the search parameters
            if (
                all(x in ex_name for x in AND) 
                and any(x in ex_name for x in OR) 
                and all(x in ex_unit for x in UNIT)
                and '-' in ex_amount 
                and ex_amount != '-1.0'
                and not any(x in ex_name for x in NOT)
                ):
                            
                    # write to csv file
                count+=1
                x = (ex_code + ';' + ex_name + ';' + ex_loc + ';' + ex_amount + ';' + ex_unit + ";" + db_name)
                print(count, ex_name,":", ex_loc, ":" "%.3g" % float(ex_amount), ex_unit)
                with open(waste_file, 'a+') as f:
                    f.write(x + '\n')
                           

                # writes a log file about the search
            end = datetime.now()
            search_time = (end - start)
            
        log_entry = (
                time + 
                " SEARCH COMPLETED. "
                " NAME: " + query["name"] + 
                ", Search parameters: AND=" + str(query["keywords_AND"]) + 
                " OR=" + str(query["keywords_OR"]) + 
                " NOT="+str(query["keywords_NOT"]) + 
                " UNIT=" +str(query['unit']) + 
                " RESULTS="+str(count) + 
                " SEARCH TIME="+str(search_time)
                )
        
        print("\n"+str(log_entry)+"\n")
        log_file = os.path.join(tmp, 'WasteSearch.log')
        with open(log_file, 'a+') as l:
            l.write(str(log_entry) + "\n")
