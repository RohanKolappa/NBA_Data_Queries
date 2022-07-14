#!usr/bin/python

import sqlite3

def everyTeamGame(teamName):
        conn = sqlite3.connect('basketball.sqlite')
        query = f"""SELECT game_date, matchup_home, team_name_home, pts_home, team_name_away, pts_away, wl_home FROM game WHERE team_name_home = '{teamName}'
        UNION ALL
        SELECT game_date, matchup_home, team_name_home, pts_home, team_name_away, pts_away, wl_away FROM game WHERE team_name_away = '{teamName}'
        ORDER BY game_date"""


        cursor = conn.execute(query)
        for row in cursor:
                print(row)


        conn.close()

