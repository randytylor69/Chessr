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
            
            # ---- check moves and change moves to PGN notation
            moves = movesToPgn(game['moves'])

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


def movesToPgn(moves):
    pgn = ""
    li = moves.split(" ")
    moveNum = 1
    index = 0
    whiteMove = ""
    blackMove = ""
    movesCopied = 0

    while index < len(li) - 1:
        whiteMove = li[index]
        blackMove = li[index+1]
        pgn += f"{moveNum}. {whiteMove} {blackMove} "

        index += 2
        moveNum += 1
        movesCopied += 2
    
    if movesCopied < len(li):
        pgn += f"{moveNum}. {li[-1]}"

    return pgn