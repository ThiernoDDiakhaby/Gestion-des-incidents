from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymysql.cursors
from datetime import date



app = Flask(__name__)
app.secret_key = 'many random bytes'

"""app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'passer123'
app.config['MYSQL_DATABASE'] = 'gestion_incident'"""

mysql = pymysql.connect(
        host="localhost",
        user="root",
        password="passer123",
        database="gestion_incident"
    )

today = date.today()
today = today.strftime("%Y-%m-%d")


def creeation_sesion(login,psw):
    mycursor = mysql.cursor()
    mycursor.execute("SELECT * FROM `utilisateur` WHERE (`login`= '%s') and (`psw`= '%s')"%(login,psw))
    r1 = mycursor.fetchone()
    Tab_U = []
    while r1:
        Tab_U.append(r1)
        r1 = mycursor.fetchone()
    session['id_u']=Tab_U[0][0]
    session['prenom'] = Tab_U[0][1]
    session['nom'] = Tab_U[0][2]
    session['login'] = Tab_U[0][3]
    session['psw'] = Tab_U[0][4]
    session['role'] = Tab_U[0][5]
    return True

#mysql = MySQL(app)
@app.route('/')
def home():
    return redirect(url_for('login'))
@app.route('/probleme')
def probleme():
    try:
        login=session['login']
    except:
        return redirect(url_for('login'))
    cur = mysql.cursor()
    cur.execute("SELECT  * FROM probleme")
    data = cur.fetchall()
    cur.close()
    #login = request.form['login']
    return render_template('index2.html', probleme=data, login=login, today=today,nom=session['nom'], prenom=session['prenom'], role=session['role'])






@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Probleme enregistreé avec succes")
        severite = request.form['severite']
        description = request.form['description']
        date_p = request.form['date_p']
        id_user = session['id_u']
        cur = mysql.cursor()
        cur.execute("insert into `probleme` (`id_user`, `severite`,`description`, `date_p`) values ('%s','%s','%s','%s')" % (id_user, severite, description, date_p))
        mysql.commit()
        return redirect(url_for('probleme'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    if session['role']== "admin":
        flash("l'incident a bien été supprimé")
        cur = mysql.cursor()
        cur.execute("DELETE FROM probleme WHERE id_p=%s", (id_data))
        mysql.commit()
        return redirect(url_for('probleme'))
    else:
        flash("Supprésion non autorisé")
        return redirect(url_for('probleme'))


@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        description = request.form['description']
        date_p = request.form['date_p']
        id_u = session['id_u']
        severite = request.form['severite']
        id_p = request.form['id_p']
        cur = mysql.cursor()
        cur.execute("UPDATE `probleme` SET `id_user`=%s,`description`=%s,`severite`=%s, `date_p`=%s Where `probleme`.`id_p`=%s" , (id_u, description, severite, date_p, id_p))
        mysql.commit()
        flash("Modification réussie avec succés")
        return redirect(url_for('probleme'))













@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == "POST":
        login_ = request.form["login"]
        psw_ = request.form['psw']
        cur = mysql.cursor()
        cur.execute("SELECT  * FROM utilisateur")
        data = cur.fetchall()
        cur.close()
        for i in data:
            print (i[3])
            if(i[3]==login_ and i[4]==psw_):
                if(creeation_sesion(login_,psw_)):
                    return redirect(url_for("probleme"))
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.route('/deconnexion')
def deconnexion():
    session.pop('login', None)
    session.pop('psw', None)
    return redirect(url_for('login'))


@app.route('/inscrire', methods = ['POST'])
def insciption():
    if request.method == "POST":
      nom = request.form["nom"]
      prenom = request.form["prenom"]
      mail = request.form["mail"]
      psw = request.form["psw"]

      cur = mysql.cursor()
      cur.execute("INSERT INTO utilisateur (prenom, nom, Login,psw,role) VALUES (%s, %s, %s, %s,%s)", (prenom, nom, mail, psw,"user"))
      mysql.commit()
      print("insertion reussi")
      return render_template("index.html")

    else:
        print('connexxion non reussi')
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
