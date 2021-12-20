import psycopg2
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')

            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s;", (username, password))
            print (cursor.fetchone())
            if cursor.fetchone() is None:
                return render_template('login.html', wrong='Wrong login or password')

            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s;", (username, password))
            records = list(cursor.fetchone())
            return render_template("account.html", user=records)

    return render_template('login.html')


if __name__ == '__main__':
    app.run()