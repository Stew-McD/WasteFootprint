#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AddMethods() : Takes each entry in the custom biosphere database 'waste_db' and creates a new method from it.
Eg., ('Waste Footprint', 'waste_dumped_combined', waste_dumped_liquid)

Created on Sat Nov 19 12:21:04 2022

@author: SC-McD
based of the work of LL
"""
# project_waste = "WasteFootprint_cutoff39"
# db_waste_name = "db_waste_cutoff39"

# DeleteMethods(project_waste)
# AddMethods(project_waste, db_waste_name)


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
            AddMethods(args)
        except:
            print("Skipping:"+args["db_name"])

def AddMethods(project_waste, db_waste_name):
    print("\n\n*** Adding new methods\n")
    import bw2data as bd

    bd.projects.set_current(project_waste)
    db_waste = bd.Database(db_waste_name)
    dic = db_waste.load()

    method_count = len(bd.methods)

    for key, value in dic.items():
        m_unit = value["unit"]
        m_code = value["code"]
        m_name = value["name"]
        m_name = m_name.replace("kilogram", "solid")
        m_name = m_name.replace("cubicmeter", "liquid")

        ch_factor = -1.0
        # if unit == "cubic meter":  #
        #     ch_factor = -1

        name_combined = "_".join((m_name.split("_")[0:2])) + "_combined"
        method_key = ('Waste Footprint', name_combined, m_name)
        method_entry = [((db_waste.name, m_code), ch_factor)]

        m = bd.Method(method_key)
        m.register(description="For estimating the waste footprint of an activity (kg): ", unit=m_unit)
        m.write(method_entry)

        print('* Added: {}\t'.format(str(method_key)))

    methods_added = len(bd.methods) - method_count
    print("\n*** Added", methods_added, " new methods")

#DeleteMethods(project_waste)
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


def CheckMethods(project_waste):
    import bw2data as bd
    bd.projects.set_current(project_waste)
    methods_waste = []
    for x in list(bd.methods):
        if "Waste Footprint" == x[0]:
            m = bd.Method(x)
            methods_waste.append(m)
            print(m.load())
            print(m.metadata)
    print(len(methods_waste))
