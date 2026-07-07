from dbFunctions import *
from utilFunctions import *
from server import *
from dotenv import find_dotenv, load_dotenv

# load env variables from root
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_TOKEN = os.getenv("API_TOKEN")
username = os.getenv("username")

def main():
    deleteAllGamesFromDB()
    addAllGamesToDB(username, API_TOKEN)
    condenseGamesToDB()
    app.run(debug=True)

if __name__ == "__main__":
    main()
