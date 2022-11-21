#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AddMethods() : Takes each entry in the custom biosphere database 'waste_db' and creates a new method from it. Eg., ('Waste Footprint', 'Total Waste Demand', waste_hazardous_cubicmeter)

Created on Sat Nov 19 12:21:04 2022

@author: SC-McD
based of the work of LL
"""


def AddMethods(project="WasteDemand", db_waste='db_waste'):

    import bw2data as bd
    
    bd.projects.set_current(project)
    db_waste_name = db_waste
    db_waste = bd.Database(db_waste_name)
    dic = db_waste.load()
    
    method = {'number':"",
               'category':"Emission",
               'localCategory':"",
               'localSubCategory':"",
               'CASNumber':"",
               'name':"",
               'unit':"",
               'meanValue': 1.0,
               'formula':"",
               'infrastructureProcess':"FALSE"
               }
                    
    
    for key, value in dic.items():
        UNIT = value["unit"]
        NAME = value["name"]
        method.update({"unit": UNIT})
        method.update({"name": NAME})
        method_name = ('Waste Footprint', 'Total Waste Demand', NAME)
        method_entry = [((db_waste.name, NAME), method["meanValue"])]
        m = bd.Method(method_name)
        m.register(description="For Estimating Total Waste Demand of a Process", unit=UNIT, name=NAME)
        m.write(method_entry)
        print('*** Great success!')
        print('* The impact category was added with the name: {}'.format(str(method_name)))


