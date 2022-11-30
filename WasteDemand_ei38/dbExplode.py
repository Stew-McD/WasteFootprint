#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dbExplode returns a single level list of all exchanges in a given Brightway2 database

uses wurst to open up the ecoinvent database, explode to a list of all exchanges, and save in a DataFrame as a .pickle binary file.
The default is that the database is called "cutoff38" in the project "default".  
This function will copy 'default' to a new project called 'WasteDemand'. If 'WasteDemand'  exists, it will be deleted and re-made each time. 

GIVE PROJECT AND DB NAMES AS STRINGS OR LEAVE BLANK TO USE DEFAULTS
(default is to copy "default" to project "WasteDemand", EI is "cutoff38")

Created on Wed Nov 16 11:31:38 2022 
@author: SC-McD
based on the work of LL
"""

def dbExplode(project_base, project_waste, db):
    
    import bw2data as bd
    import wurst as w
    import pandas as pd
    import os
    
# Introduction and project/db choice (if not given in function call)
    
    print("** dbExplode uses wurst to open a bw2 data base, \nexplodes the exchanges for each process, \nthen returns a pickle file with a DataFrame list of all activities **")
    print("\n * Using packages: ", 
          "\n\t bw2data" ,bd.__version__,
          "\n\t wurst" , w.__version__)
    
              
    if project_waste in bd.projects:
        bd.projects.delete_project(project_waste, delete_dir=True)
    
    print("\n**Project {} will be copied to a new project: {}".format(project_base, project_waste))
    bd.projects.set_current(project_base)
    bd.projects.copy_project(project_waste)
    

# Explode database
    db = bd.Database(db)
    print("\n* db:", db.name, "in project:", bd.projects.current, "will be processed")
    print("\n** Opening the sausage... \n")
    guts = w.extract_brightway2_databases(db.name)
    
    print("\n*** Extracting activities from db...")
    df = pd.DataFrame(guts, columns =['code', 'exchanges'])
    
    print("\n*** Exploding exchanges from activities...")
    df = df.explode("exchanges", ignore_index=False)
    
    print("\n*** Pickling...")
    tmp = os.getcwd() + "/tmp"
    if not os.path.isdir(tmp): os.mkdir(tmp)
    pickle_path = os.path.join(tmp, db.name +"_exploded.pickle")
    df.to_pickle(pickle_path)
    print("\n Pickle is:", "%1.0f" %(os.path.getsize(pickle_path)/1024**2), "MB")
    print("\n*** The sausage <"+db.name+"> was exploded and pickled.\n\n Rejoice!")
    
        # make log file
    log_entry = (db.name + "," + bd.projects.current) 
    log_file = os.path.join(tmp, 'dbExplode.log')
    with open(log_file, 'a+') as l:
        l.write(str(log_entry))
        
    return 
        
        
    






