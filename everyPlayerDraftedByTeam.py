#!usr/bin/python

import sqlite3

from pprint import pprint

def everyPlayerDrafted(team_name):
	conn = sqlite3.connect('basketball.sqlite')
	pprint(team_name)
	query = f"""SELECT yearDraft, namePlayer FROM draft WHERE teamName = '{team_name}'
	ORDER BY yearDraft ASC"""
	cursor = conn.execute(query)
	for row in cursor:
		pprint(row)

	conn.close()
