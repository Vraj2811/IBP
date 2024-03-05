from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import sqlite3
import os

app = Flask(__name__)
socketio = SocketIO(app)

# Database setup
current_directory = "./"
db_path = os.path.join(current_directory, 'data.db')
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()
cursor.execute(
    'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name1 TEXT, name2 TEXT, name3 TEXT, name4 TEXT, name5 TEXT)')
conn.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract form data
        name1 = request.form.get('name1')
        name2 = request.form.get('name2')
        name3 = request.form.get('name3')
        name4 = request.form.get('name4')
        name5 = request.form.get('name5')

        # Insert data into the database
        cursor.execute('INSERT INTO items (name1, name2, name3, name4, name5) VALUES (?, ?, ?, ?, ?)',
                       (name1, name2, name3, name4, name5))
        conn.commit()

        return "Form submitted successfully"  # Example response
    else:
        # Fetch initial data from the database
        cursor.execute('SELECT * FROM items')
        items = cursor.fetchall()
        return render_template('index.html', items=items)


@socketio.on('submit')
def handle_submit(data):
    name1 = data['name1']
    name2 = data['name2']
    name3 = data['name3']
    name4 = data['name4']
    name5 = data['name5']
    # Insert data into the database
    cursor.execute('INSERT INTO items (name1, name2, name3, name4, name5) VALUES (?, ?, ?, ?, ?)',
                   (name1, name2, name3, name4, name5))
    conn.commit()
    # Fetch updated data from the database
    cursor.execute('SELECT * FROM items')
    updated_items = cursor.fetchall()
    # Emit signal to update the client with the new data
    emit('update_table', updated_items, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
