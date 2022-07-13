#!/usr/bin/python

import sqlite3

def draft_by_year(year):
    conn = sqlite3.connect('basketball.sqlite')

    print("Opened database successfully");
    cursor = conn.execute(f"""SELECT yeardraft, numberpickoverall, nameplayer, slugteam 
                             FROM draft 
                             WHERE yeardraft = {year}""")
    for row in cursor:
        print(row)

    conn.close()
