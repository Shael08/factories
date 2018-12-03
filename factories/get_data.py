#!/usr/bin/env python3

import sqlite3
import pulp

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect('db.sqlite3')
conn.row_factory = dict_factory
cursor=conn.cursor()

cursor.execute('select * from app_factory')
factories = [ record for record in cursor ]

cursor.execute('select * from app_depot')
depots = [ record for record in cursor ]

cursor.execute('select * from app_factory_to_depots_shipping')
factory_to_depot_raw = [ record for record in cursor ]


def factoryid(name):
    withthisname = [ r for r in filter(lambda x: x['name'] == name, factories)]
    if len(withthisname)>0:
        return(withthisname[0]['id'])
    else:
        return(None)

def depotid(name):
    withthisname = [ r for r in filter(lambda x: x['name'] == name, depots)]
    if len(withthisname)>0:
        return(withthisname[0]['id'])
    else:
        return(None)

big_number=999999999999
factory_names = [ f['name'] for f in factories ]
depot_names = [ f['name'] for f in depots ]
#valahogy igy kene: factory_to_depot_cost[factoryname][depotname]
factory_to_depot_cost={}
for f in factory_names:
    factory_to_depot_cost[f]={}
    for d in depot_names:
        result = [r for r in filter(lambda x: x['depot_fk_id'] == depotid(d) and x['factory_fk_id'] == factoryid(f), factory_to_depot_raw)]
        if len(result)>0:
            factory_to_depot_cost[f][d] = result[0]['cost']
        else:
            factory_to_depot_cost[f][d] = big_number
        
problem = pulp.LpProblem("DistributionProblem", pulp.LpMinimize)

transp_F_D = pulp.LpVariable.dicts("F_D", (factory_names, depot_names), 0)

print(transp_F_D)
