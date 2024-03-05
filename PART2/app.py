# app.py

from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

# Function to fetch data from the database
def get_data_from_db():
    db_path = './data.db'
    if os.path.exists(db_path):
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Fetch data from the database table
        cursor.execute("SELECT * FROM items")
        data = cursor.fetchall()

        # Close the database connection
        conn.close()

        return data
    else:
        print("Database file not found.")

# Route to serve the HTML file and display data
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch updated data
@app.route('/get_data')
def get_updated_data():
    data = get_data_from_db()
    return {'data': data}

if __name__ == '__main__':
    app.run(debug=True, port=5001)
