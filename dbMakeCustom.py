#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
There are two functions here:

* dbWriteExcel() : makes an xlsx file in the format of a Brightway2 database. For each .csv in the folder 'WasteSearchResults' a database entry will be added

* dbExcel2BW(): Takes the custom database produced by dbWriteExcel() and imports it into Brightway2. Defaults: project = 'WasteDemand', db = 'db_waste'  

Created on Sat Nov 19 10:11:02 2022
@author: SC-McD
"""
#%% 
def dbWriteExcel(db_waste="db_waste"):
    # setup xlsx file for custom database
    
    import os
    from openpyxl import Workbook
    
    search_results_path = os.path.join(os.getcwd(), "WasteSearchResults")
   
    xl_filename = os.path.join(search_results_path, "WasteSearchDatabase.xlsx")
    
    if os.path.isfile(xl_filename): os.remove(xl_filename)
    
    xl = Workbook()
    xl_db = xl.active
    xl_db['A1'] = "Database"
    xl_db["B1"] = db_waste
    xl_db['A2'] = ''
        
    
    count = 0
    print("Writing custom database file:", db_waste,"-->", xl_filename)
    for f in os.listdir(search_results_path):
        f_path = os.path.join(search_results_path, f)
        if os.path.isfile(f_path) and f_path.endswith('.csv'):
            count += 1
            NAME = f.removesuffix(".csv").replace(" ","")
            CODE = NAME # maybe change this sometime
            if "kilogram" in NAME: UNIT = "kilogram"
            if "cubicmeter" in NAME: UNIT = "cubic meter"
    
           # add new activity to custom database based on search query if there are hits
            db_entry = { 
                    "Activity": NAME, 
                    "categories" : "water, air, land",
                    "code" : CODE,
                    "type" : "emission" ,
                    "unit" : UNIT
                    }
            
            print("Appending:",NAME)
            for key, value in db_entry.items():
                row = [key , str(value)]
                xl_db.append(row)
                
        xl_db.append([""]) # BW2 ExcelImport requires an empty row between each activity
                
    xl.save(xl_filename)
    print("Added", count, "entries to an xlsx for the custom waste db:", db_waste)
    
    return xl_filename
    

#%% dbExcel2BW

def dbExcel2BW(project_waste, db_waste, xl_filename):
    print("Importing to brightway2 project {} the custom database  {} produced by WasteSearch() and dbWriteExcel".format(project_waste, db_waste))
    import os
    import bw2data as bd
    import bw2io as bi
    
    search_results_path = os.path.join(os.getcwd(), "WasteSearchResults") 
    xl_path = os.path.join(search_results_path, xl_filename)
    
    bd.projects.set_current(project_waste)
 
    print("\nRunning BW2io ExcelImporter...\n")
    db = bi.ExcelImporter(xl_path)
    db.apply_strategies()
    db.statistics()
    db.write_database()
    db.waste = bd.Database(db_waste)
    print(db.metadata)
        
    print("\nGreat success!")
