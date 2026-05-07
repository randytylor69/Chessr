import sqlite3, os
from fetchFunctions import *

def addAllGamesToDB(username, API_TOKEN):

    db = sqlite3.connect('playerstats.db', isolation_level=None)
    
    # fetch all games
    allGames = fetchGamesFromUser(username, API_TOKEN)
    for game in allGames:
        try:
            # ---- check id
            id = game['id']

            # ---- check color
            color = ''
            if game['players']['white']['user']['name'] == username:
                color = 'white'
            else:
                color = 'black'

            # ---- check variant
            variant = game['variant']

            # ---- check winner (BOOLEAN)
            winner = 0
            if 'winner' in game:
                winner = (game['winner'] == color)
            
            # ---- check status
            status = game['status']
            
            # ---- check moves
            moves = game['moves']

            # ---- check finish time
            finishTime = game['lastMoveAt']

            db.execute(
                'INSERT INTO all_games VALUES(?,?,?,?,?,?,?)',
                [id, color, variant, status, winner, moves, finishTime]
            )
        except Exception as e:
            print(f"An error has occured: {e}")

    print(f"A total of {len(allGames)} games are read. ")


def deleteAllGamesFromDB():
    db = sqlite3.connect('playerstats.db', isolation_level=None)
    db.execute('DELETE FROM all_games WHERE 1')