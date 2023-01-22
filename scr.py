from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
from datetime import date
import pandas as p


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Satish/Downloads/firsttask/database.db'
db = SQLAlchemy(app)


#create table called user
class user(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(200))
    password=db.Column(db.String(200))
    firstname=db.Column(db.String(200))
    lastname=db.Column(db.String(200))
    date1=db.Column(db.String(200))


#index page
@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        email=request.form['emailid']
        password=request.form['passuser']
        login=user.query.filter_by(email=email,password=password).first()
        if login is not None:
            return redirect(url_for("success"))
    return render_template("login.html")



#signup page
@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        mail = request.form['email']
        passw = request.form['passwd']
        fname = request.form['fname']
        lname = request.form['lname']
        print(mail)


        repassw = request.form['repasswd']
        date2 = date.today()
        engine = create_engine('sqlite:////Users/Satish/Downloads/firsttask/database.db', convert_unicode=True)
        usertabledata=engine.execute('select * from user ')
        dfsign=p.DataFrame(usertabledata,columns=('sn','email','password','fname','lname','date2'))
        print(dfsign)

        emailid=list(dfsign['email'])
        print(emailid)
        
        try:
            
            if emailid.index(mail)>=0:
                return render_template("a.html")
        except:
            register = user( email = mail, password = passw , firstname = fname, lastname = lname, date1 = date2)
            db.session.add(register)
            db.session.commit()

        return redirect(url_for("login"))
    return render_template("signup.html")


#success page 
@app.route('/success',methods=['POST','GET'])
def success():
	return render_template('success.html')


while True:
    
    db.create_all()
    app.run(debug='True')

