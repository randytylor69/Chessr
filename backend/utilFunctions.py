import csv

# inquire opening name from PGN input
def getOpeningFromPGN(pgn):
    opening = []
    pgn = pgn.strip()
    dbNameArray = ['a','b','c','d','e']

    for dbName in dbNameArray:

        with open(f"openingDB/{dbName}.tsv", newline='') as file:
            
            tsv_reader = csv.reader(file, delimiter='\t')
            for row in tsv_reader:
                
                if row[2].strip() in pgn:
                    opening.append(row[1])


    if len(opening)>0:
        return opening[-1]
    else:
        return None

