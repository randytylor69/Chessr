CREATE TABLE all_games (
    id TEXT PRIMARY KEY,
    color TEXT NOT NULL,
    variant TEXT NOT NULL,
    status TEXT NOT NULL,
    winner INT NOT NULL,
    moves TEXT NOT NULL,
    finishTime TEXT NOT NULL
)

db.execute(
	'ALTER TABLE all_games RENAME COLUMN result TO winner'
)

DROP TABLE all_games
ALTER TABLE all_games DROP COLUMN column_name
