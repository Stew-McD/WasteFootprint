#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ExchangeEditor():
For every activity found by WasteSearch(), this function will add the relevant exchange from the db_waste.
This function takes the longest time to run (~10 min for me).

Created on Thu Nov 17 15:30:24 2022

@author: stew
"""

# project_waste='WasteFootprint_38_cutoff'
# db_name="cutoff38"
# db_waste_name="db_waste_cutoff38"

def ExchangeEditor(project_waste, db_name, db_waste_name):

    import os
    import pandas as pd
    import bw2data as bd
    from datetime import datetime

    tmp = os.path.join(os.getcwd(), "data/tmp")
    search_results_path = os.path.join(os.getcwd(), "data/WasteSearchResults", db_name)


    bd.projects.set_current(project_waste)
    db = bd.Database(db_name)
    db_waste = bd.Database(db_waste_name)

    # find files produced by WasteSearch(), make df for each, add to dict
    file_dict = {}
    for f in os.listdir(search_results_path):
        f_path = os.path.join(search_results_path, f)
        if os.path.isfile(f_path) and f_path.endswith('.csv'):
            NAME = f.replace(".csv",'').replace(" ","")
            df = pd.read_csv(f_path, sep=';', header=0, index_col=0)

            df.reset_index(inplace=True)
            df = df[["code","name", "location", "ex_name", "ex_amount", "ex_unit", "ex_location"]]
            file_dict.update({ NAME : df})

 #%% Appending all processes with waste exchanges with custom biosphere waste exchanges in same amount and unit as technosphere exchange
    countNAME = 0
    for NAME, df in file_dict.items():
        countNAME += 1
        start = datetime.now()
        progress_db = str(countNAME) + "/" + str(len(file_dict.items()))
        count = 0

        for r in df.to_dict('records'):
            code = r["code"] # get data from activity in search results
            name = r["name"]
            location = r["location"]
            ex_name = r["ex_name"]
            amount = r["ex_amount"]
            unit = r["ex_unit"]
            ex_location = r["ex_location"]
            process = db.get(code)
            waste_ex = db_waste.get(NAME)
            before = len(process.exchanges())

            process.new_exchange(input=waste_ex.key, amount=(-1*amount), unit=unit, type='biosphere').save()
            after = len(process.exchanges())

            if (after-before) == 1:
                count += 1
                progress_exc = '(' + str(count) + "/" + str(df.shape[0]) +')'
                print(db.name, progress_db, NAME, progress_exc, '-->', code, location, ex_location, name, ex_name)

        # log file entry
            end = datetime.now()
            duration = (end - start)
        log_entry = (db_name, NAME,"additions", count, "duration:", str(duration))
        print(log_entry)
        log_file = os.path.join(tmp, 'ExchangeEditor.log')
        with open(log_file, 'a+') as l:
            l.write(str(log_entry)+"\n")
