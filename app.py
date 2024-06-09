from flask import Flask, render_template, request
from flask_mysqldb import MySQL
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "portfolio"

mysql= MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # success=False
    if request.method=='POST':
        aname = request.form['name']
        aemail = request.form['email']
        asubject = request.form['subject']
        amessage = request.form['message']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user_request (aname,aemail,asubject,amessage) VALUES (%s,%s,%s,%s)",(aname,aemail,asubject,amessage))
        mysql.connection.commit()
        cur.close()

        
        return 'success'
        
    return render_template('index.html')

@app.route('/project1')
def project1():
    return render_template('project_army.html')
@app.route('/project2')
def project2():
    return render_template('project_resturant.html')
@app.route('/project3')
def project3():
    return render_template('project_tourism.html')
@app.route('/project4')
def project4():
    return render_template('project_company.html')
@app.route('/p')
def proje4():
    return render_template('he.html')

if __name__=="__main__":
    app.run(debug=True)