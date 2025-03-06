from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="event_db"
)
cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM events ORDER BY event_date")
    events = cursor.fetchall()
    return render_template('index.html', events=events)

@app.route('/add', methods=['POST'])
def add_event():
    name = request.form['name']
    date = request.form['date']
    cursor.execute("INSERT INTO events (name, event_date) VALUES (%s, %s)", (name, date))
    db.commit()
    return redirect('/')

@app.route('/delete/<int:event_id>')
def delete_event(event_id):
    cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

