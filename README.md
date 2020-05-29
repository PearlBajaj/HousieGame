# HousieGame
Housie is a indian version of bingo, this website is to assist users in managing the game online especially during times of quarantine.

NOTE: This project is not complete and I'm still working on it. 

Instructions to run
1. Go to terminal
2. cd to the folder where the repository is cloned
3. Open the folder through terminal, ls and you should see housiegame, readme and venv.
4. In terminal run the following command:
    1. source venv/bin/activate
    2. cd housiegame
    3. ls (you should see, db.sqlite3,	housie,		housiegame,	manage.py)
    4. python manage.py makemigrations
    5. python manage.py migrate
    6. python manage.py runserver
5. to exit virtual env use this command: "deactivate" 
