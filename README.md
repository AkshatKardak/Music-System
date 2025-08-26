## Music-System

This is a full-stack web application designed to manage and display a collection of songs and playlists. The system is built with a lightweight Python backend using the Flask framework, a MySQL database for data persistence, and a modern frontend using HTML, CSS, and dynamic JavaScript.

---

## Features
- Browse a list of all available songs.
- View curated playlists and see which songs belong to them.
- Add new songs to the library through a simple web form.
- Automatically handle new artists by adding them to the database if they do not already exist.

## Tech Stack
- Frontend: HTML, CSS, JavaScript (using the Fetch API for asynchronous communication).
- Backend: Python 3.x, Flask
- Database: MySQL, Flask-MySQLdb

---

## Prerequisites
- Before running this project, you need to have the following installed:
- Python 3.x: (e.g., Python 3.13)
- MySQL Server: A running instance of MySQL.

 ---
 
## Installation & Setup
Follow these steps to get the project running on your local machine.
1. Clone the Project (or open your existing folder)
```sh
git clone https://github.com/AkshatKardak/Music-System.git
cd Music-System

```

2. Set up the Python Environment
Create a virtual environment to manage project dependencies and activate it.

```sh
python -m venv venv
```

# For Windows:
# .\venv\Scripts\activate

---

# For macOS/Linux:
# source venv/bin/activate

---

## Install Python Libraries
- Install Flask and the MySQL connector within your activated virtual environment.

```sh
pip install Flask Flask-MySQLdb
```

--- 

## Database Setup
- You must create and populate the MySQL database for the application to function.
- Connect to your MySQL server and run the following commands:

# app.py
...
- app.config['MYSQL_HOST'] = 'localhost'
- app.config['MYSQL_USER'] = 'root'
- app.config['MYSQL_PASSWORD'] = 'your_mysql_password' # <-- Replace with your password
- app.config['MYSQL_DB'] = 'music_system'
...

---

How to Run
After completing all the setup steps, run the application from your terminal.

```sh
# Make sure your virtual environment is active
.\venv\Scripts\activate
# Run the Flask app
python app.py
The application will be accessible at http://127.0.0.1:5000.

```

---

## Usage
- Once the page loads, you can:
- View all pre-populated playlists and songs.
- Click on a playlist to see only the songs within it.
- Use the "Add New Song" form to add a new song to your database. The page will automatically refresh to show the new entry.

## Contributors
Akshat Kardak - GitHub Profile **"https://github.com/AkshatKardak"**




