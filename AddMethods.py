#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AddMethods() : Takes each entry in the custom biosphere database 'waste_db' and creates a new method from it.
Eg., ('Waste Footprint', 'waste_dumped_combined', waste_dumped_liquid)

Created on Sat Nov 19 12:21:04 2022

@author: SC-McD
based of the work of LL
"""
# project = "WasteDemand"
# db_waste = "db_waste"
#AddMethods(project, db_waste)

def AddMethods(project, db_waste_name):

    import bw2data as bd

    bd.projects.set_current(project)
    db_waste = bd.Database(db_waste_name)
    dic = db_waste.load()

    method_count = len(bd.methods)

    for key, value in dic.items():
        unit = value["unit"]
        code = value["code"]
        name = value["name"]
        # name = name.replace("kilogram", "solid")
        # name = name.replace("cubicmeter", "liquid")

        ch_factor = 1.0
        # if unit == "cubic meter":  # to get m^3 into kg (rough, but so are most CFs)
        #     ch_factor = 1000.0

        name_combined = "_".join((name.split("_")[0:2])) + "_combined"
        method_key = ('Waste Footprint', name_combined, name)
        method_entry = [((db_waste.name, code), ch_factor)]

        m = bd.Method(method_key)
        m.register(description=("For estimating the waste demand of an activity: ",name))
        m.write(method_entry)

        print('* Added: {}\t'.format(str(method_key)))

    methods_added = len(bd.methods) - method_count
    print("\n*** Added", methods_added, " new methods")


def DeleteMethods(project_waste) :

    import bw2data as bd
    bd.projects.set_current(project_waste)

    start = len(bd.methods)
    print("\n# of methods:", start,"\n")
    for m in list(bd.methods):
        if "Waste Footprint" in m:
            del bd.methods[m]
            print("deleted:\t", m)

    finish = len(bd.methods)
    print("\n# of methods :", finish)
    print("\n** Deleted {} methods".format(str(start - finish)))
