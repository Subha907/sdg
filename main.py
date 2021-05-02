from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
mydb=mysql.connector.connect(
		host="localhost",
		user="root",
		password="",
		database="sdg"
		)
mycursor=mydb.cursor()
@app.route('/',methods=['POST','GET'])
def index():
	if request.method =='POST':
	    signup=request.form
	    name=signup['name']
	    birthdate=signup['birthdate']
	    mycursor.execute("insert into dob(name,birthdate) values(%s,%s)",(name,birthdate))
	    mydb.commit()
	    mycursor.close()
	    return "Thanks"
	return render_template('index.html')
#app.run(debug=True)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/login_validation',methods=['POST','GET'])
def login_validation():
	#signup=request.form.get
	name=request.form.get('name')
	birthdate=request.form.get('birthdate')
	#cursor = mysql.connector.cursor(MySQLdb.cursors.DictCursor)
	mycursor.execute("""SELECT * FROM dob WHERE name LIKE '{}' AND birthdate LIKE '{}'""".format(name,birthdate))
	#mydb.commit()
	#mycursor.close()
	dob=mycursor.fetchall()
	if len(dob)>0:
	    return render_template('dashboard.html',name=name)
	else:
		#msg='Wrong password'
	    return render_template('login.html',msg='Wrong password')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',name=name)
	 	    

if __name__ == '__main__':
   app.run(host='192.168.0.101',port='8081')
