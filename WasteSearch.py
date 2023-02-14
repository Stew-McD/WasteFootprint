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

def WasteSearch(queries):
    import os
    import pandas as pd

    db_name = queries[0]["db_name"]
    search_results_path = os.path.join(os.getcwd(), 'data/WasteSearchResults', db_name)
    if not os.path.exists(search_results_path): os.makedirs(search_results_path)

            # load exchanges into df from the DBexplode pickle file
    tmp = os.path.join(os.getcwd(),"data/tmp")


    pickle_path = os.path.join(tmp, db_name+"_exploded.pickle")
    print("*** Loading pickle to dataframe...")
    df = pd.read_pickle(pickle_path)
    print("*** Searching for waste exchanges...")

    def search(query):
    # for readability
        db_name = query["db_name"]
        NAME_BASE = query["name"]
        UNIT = query["unit"]
        NAME = NAME_BASE + "_" + UNIT
        CODE = NAME.replace(" ", "")
        query.update({"code" : NAME})
        AND = query["AND"]
        OR = query["OR"]
        NOT = query["NOT"]

        df_results = df[
                        (df["ex_name"].apply(lambda x: True if all(i in x for i in AND) else False))
                        & (df["ex_unit"] == UNIT)
                        & (df['ex_amount'] < 0)
                        & (df["ex_amount"] != -1)
                        ]

        if OR != None:
            df_results = df_results[(df_results["ex_name"].apply(lambda x: True if any(i in x for i in OR) else False))]

        if NOT != None:
            df_results = df_results[(df_results["ex_name"].apply(lambda x: False if any(i in x for i in NOT) else True))]

                # html file for each query


                 # csv file for each query
        #df.set_index('code', inplace=True)
        waste_file_name = NAME.replace(" ", "")
        waste_file = os.path.join(search_results_path, waste_file_name)

        if df_results.shape[0] != 0:
            df_results.to_csv(waste_file+".csv", sep=";", )
            df_results.to_html(waste_file+".html")

        log_entry = (
                " DB="+ query["db_name"] +
                " RESULTS="+str(df_results.shape[0]) +
                " NAME: " + query["name"] +
                ", Search parameters: AND=" + str(query["AND"]) +
                " OR=" + str(query["OR"]) +
                " NOT="+str(query["NOT"]) +
                " UNIT=" +str(query['unit']) +
                " CODE=" +str(CODE)
                )

        print("\n"+str(log_entry))
        log_file = os.path.join(tmp, 'WasteSearch.log')
        with open(log_file, 'a+') as l:
            l.write(str(log_entry)+"\n")

    for query in queries:
        search(query)
