import requests, json

# function lists
def fetchGamesFromUser(username, token, amount=''):
    try:
        res = requests.get(
            f"https://lichess.org/api/games/user/{username}",

            headers={
                "Accept":"application/x-ndjson",
                "Authorization": f"Bearer {token}"
            },
            params={
                "max":amount
            }
        )
        result = []
        for line in res.iter_lines():
            data = json.loads(line)
            result.append(data)
        
        return result

    except Exception as e:
        return "something's off"
