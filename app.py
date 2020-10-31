from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql.cursors



app = Flask(__name__)
app.secret_key = 'many random bytes'

"""app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'passer123'
app.config['MYSQL_DATABASE'] = 'gestion_incident'"""

mysql = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="gestion_incident"
    )

#mysql = MySQL(app)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/probleme')
def probleme():
    cur = mysql.cursor()
    cur.execute("SELECT  * FROM probleme")
    data = cur.fetchall()
    cur.close()

    return render_template('index2.html', probleme=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Probleme enregistreé avec succes")
        severité = request.form['severité']
        description=request.form['description']
        date_p = request.form['date_p']
        id_user  = request.form['id_user']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO probleme (severité, description, date_p,id_user) VALUES (%s, %s, %s, %s)", (severité, description, date_p,id_user))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("l'incident a été bien enregistré")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM probleme WHERE id_p=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))




@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id_p']
        severité = request.form['severité']
        description = request.form['description']
        date_p = request.form['date_p']
        id_user = request.form['id_user']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE probleme
               SET severité=%s, description=%s, date_p=%s,id_user=%s
               WHERE id_p=%s"
            """, (severité, description, date_p, id_user,id_data))
        flash("Modification réussie avec succés")
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
