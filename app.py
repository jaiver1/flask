from flask import Flask,render_template
from flaskext.mysql import MySQL


mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'srcg'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/os/show")
def osShow():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM facultades")
    faculties = cursor.fetchall()
    return render_template('os.html',facultades = faculties)


@app.route("/mem/show")
def memShow():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM programas")
    careers = cursor.fetchall()
    return render_template('mem.html',carreras = careers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)