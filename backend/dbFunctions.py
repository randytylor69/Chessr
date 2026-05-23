import sqlite3, os, csv
from fetchFunctions import *
from utilFunctions import *
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

            # --- opening name
            opening = getOpeningFromPGN(moves)

            # ---- check finish time
            finishTime = game['lastMoveAt']

            db.execute(
                'INSERT INTO all_games VALUES(?,?,?,?,?,?,?,?)',
                [id, color, variant, status, winner, moves, opening, finishTime]
            )
        except Exception as e:
            print(f"An error has occured: {e}")

    print(f"A total of {len(allGames)} games are read. ")

def deleteAllGamesFromDB():
    db = sqlite3.connect('playerstats.db', isolation_level=None)
    db.execute('DELETE FROM all_games WHERE 1')
    db.execute('DELETE FROM opening_winrate WHERE 1')

'''
 1. Read from all_games table.

 2. Sort individual games by opening and output into a 3D array, with the following headers:
    OPENING | COLOR | WINNER (1 or 0)

 3. Sort the 3D array into a 2nd #D ARRAY that contains unique openings:
    OPENING | COLOR | GAMES | WON_GAMES | WINRATE

 4. Append the last ARRAY to DB
'''

def condenseGamesToDB():

    db = sqlite3.connect('playerstats.db', isolation_level=None)
    CSV_ARRAY_INITIAL = [] # has all games, with headers: OPENING | COLOR | WINNER
    CSV_ARRAY_FINAL = []   # has condensed games, headers: 
                           # OPENING | COLOR | GAMES | WON_GAMES | WINRATE
    

    ALL_GAMES_OUTPUT = db.execute('SELECT * FROM all_games')
    
    
    for game in ALL_GAMES_OUTPUT:
        
        # get all the information from a game
        opening = game[6]
        color = game[1]
        winner = game[4]

        # add opening to array
        CSV_ARRAY_INITIAL.append([opening, color, winner])
    
    
    for game in CSV_ARRAY_INITIAL:
        # 1. check if opening is alreayd recorded
        recorded = False
        
        for row in CSV_ARRAY_FINAL:
            # headers:
            # OPENING | COLOR | GAMES | WON_GAMES | WINRATE
            
            if row[0] == game[0]:
                recorded = True

                # the opening is recorded -> update opening status
                row[2] += 1 # total games + 1
                if game[2] == 1:
                    row[3] += 1
                    row[4] = round(row[3] / row[2], 4)
                break
            
        # 2. if not recorded, then record it 
        if recorded == False:
            opening = game[0]
            color = game[1]
            total_games = 1
            won_games = game[2]
            winrate = round(won_games / total_games, 4)
            CSV_ARRAY_FINAL.append([opening, color, total_games, won_games, winrate])
        

    # Finally, we add CSV_ARRAY_FINAL to its own table in the database.
    for row in CSV_ARRAY_FINAL:

        db.execute(
            f"INSERT INTO opening_winrate VALUES (?,?,?,?)",
            [row[0], row[1], row[2], row[4]]
        )

    print(f"{len(CSV_ARRAY_FINAL)} openings analyzed and stored in db")


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

def getDataFromTable(table):
    db = sqlite3.connect('playerstats.db', isolation_level=None)
    cursorObj = db.execute(f"SELECT * FROM {table}")

    # get table headers into a list
    headers = list(map(lambda header : header[0], cursorObj.description))
    # enumerated headers:
    # [(0, 'opening'), (1, 'color'), (2, 'games_count'), (3, 'winrate')]

    # convert to JSON
    # Example Row: ('Vienna Game: Max Lange Defense', 'white', 10, 0.5556)
    JSON_result = [{header : row[i] for i, header in enumerate(headers)} for row in cursorObj]
    return JSON_result
    