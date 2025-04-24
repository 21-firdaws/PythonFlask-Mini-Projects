from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
db_config = {
    'user': 'root',
    'password': 'fardosa2205166',
    'host': 'localhost',
    'database': 'mydatabase'
}

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    if name and email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('records'))
    else:
        return "Please provide both name and email."

@app.route('/records')
def records():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('records.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
