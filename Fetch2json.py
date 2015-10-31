__author__ = 'sambhav'


import sqlite3
import json
import queryBuilder as qb

DB = "db.sqlite3"

def gethotels(val,json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    db = conn.cursor()
    print "inside Fetch2Json\n\n"
    print val

    try :
        rows = db.execute(qb.funcQueryBuilder(val)).fetchall()
    except:
        return json.dumps([{'Message':'Sorry!! Didnt get that!! why dont you try something else like ,hotels in Bali with Halal or hotels in singpore without gym'}])

    conn.commit()
    conn.close()

    if json_str:
       return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON


def writeTojson(val):

	with open("fetch.json","w") as target:
		target.write(gethotels(val,json_str = True ))
       
   


