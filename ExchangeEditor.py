#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ExchangeEditor():
For every activity found by WasteSearch(), this function will add the relevant exchange from the db_waste. 
This function takes the longest time to run (~10 min for me).

Created on Thu Nov 17 15:30:24 2022

@author: stew
"""
def ExchangeEditor(project_waste, db, db_waste):

    import os
    import pandas as pd
    import bw2data as bd
    from datetime import datetime
    
    # I should pull these variables from the other functions and not define them here... (not sure how to do that)
    tmp = os.path.join(os.getcwd(), "tmp")
    search_results_path = os.path.join(os.getcwd(), "WasteSearchResults")
    
    
    bd.projects.set_current(project_waste)
    db = bd.Database(db)
    db_waste = bd.Database(db_waste)
    
    # find files produced by WasteSearch(), make df for each, add to dict 
    file_dict = {}
    for f in os.listdir(search_results_path):
        f_path = os.path.join(search_results_path, f)
        if os.path.isfile(f_path) and f_path.endswith('.csv'):
            NAME = f.removesuffix(".csv").replace(" ","")
            df = pd.read_csv(f_path, sep=';', header=None)
            df.columns = ['process code', 'name', 'location','amount', 'unit',"database"]
            file_dict.update({ NAME : df})
    
 #%% Appending all processes with waste exchanges with custom biosphere waste exchanges in same amount and unit as technosphere exchange
    countNAME = 0
    for NAME, df in file_dict.items():
        countNAME += 1
        start = datetime.now()
        progress_db = str(countNAME) + "/" + str(len(file_dict.items()))
        count = 0
        skip_count = 0
        for i in range(0, df.shape[0]):
            code = df.iloc[i,0] # get data from activity in search results
            name = df.iloc[i,1]
            location = df.iloc[i,2]
            amount = df.iloc[i,3]
            unit = df.iloc[i,4]
            process = db.get(code) 
            waste_ex = db_waste.get(NAME)
            before = len(process.exchanges())
            
        # check for existing entry (need to add a location factor to the "if" statement, since codes are not unique)
            # ex_list = []
            # for x in list(process.exchanges()):
            #     inp = x.as_dict()["input"]
            #     ex_list.append(inp)
                
    
            # if waste_ex.key in ex_list:
            #     print("Skipping", waste_ex.key, "already exists for process", str(process))
            #     skip_count += 1
            # else:
            process.new_exchange(input=waste_ex.key, amount=amount, unit=unit, type='biosphere').save()
            after = len(process.exchanges())
        
            if (after-before) == 1:
                count += 1
                progress_exc = '(' + str(count) + "/" + str(df.shape[0]) +')'
                print(progress_db, NAME, progress_exc , '-->', code, location, name)
        
        # log file entry
            end = datetime.now()
            duration = (end - start)
        log_entry = (NAME,"additions", count, "skipped", skip_count, "duration:", str(duration))
        print(log_entry)
        log_file = os.path.join(tmp, 'ExchangeEditor.log')
        with open(log_file, 'a+') as l:
            l.write(str(log_entry) + "\n")
