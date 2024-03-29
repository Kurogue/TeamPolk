![Logo of ProTrack Automotive Systems](https://user-images.githubusercontent.com/66132436/232945181-891ce761-50df-4637-bfa8-6dddeeee5a87.png)

# ProTrack Automotive Systems
Team Polk's final project for Software Engineering Spring 2023. This project focuses on creating an inventory system to keep record of vehicles for a small company. This program has a selection of features and functions for the user to interact with the GUI. A user, for instance, can find a particular vehicle with a known vehicle ID in the database. 

### Installation

1. Do `git clone https://github.com/Kurogue/TeamPolk.git` to download a local copy of the repository
2. Create a .env file with the valid credentials to connect to the PostgreSQL database, located in db.py in the backend folder

### Usage

1. To run the project, go to the root directory and do `python main.py` to run the program
2. Enter the search forms and click appropriate buttons to execute the query

### Dependencies

Must have Python3 installed on the system. All remaining dependencies are located in the requirements.txt to get the project running. As for tkinter, that is a package that already comes when installing Python

### Database

The PostgreSQL instance runs on Google Cloud. If you want to modify and access any part of the database, you must be an authenicated user listed for the permissions on Google Cloud. There are currently 24 tables in the database that describe the particular features of a vehicle.

### License

MIT license
