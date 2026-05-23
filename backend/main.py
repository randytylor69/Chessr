from dbFunctions import *
from utilFunctions import *
from server import *
from dotenv import find_dotenv, load_dotenv
import webbrowser
import subprocess

# load env variables from root
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_TOKEN = os.getenv("API_TOKEN")
username = os.getenv("username")

def main():
    # Calls FE to open localhost.
    # PROBLEM: code stops executing after subprocess.run
    cmd = "cd ../frontend ; npm run dev"
    subprocess.run(cmd, shell=True)
    # CODE STOPS EXECUTING
    webbrowser.open_new_tab("http://localhost:5173/")
    deleteAllGamesFromDB()
    addAllGamesToDB(username, API_TOKEN)
    condenseGamesToDB()
    app.run()


if __name__ == "__main__":
    main()
