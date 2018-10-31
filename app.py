from flask import Flask , render_template , url_for , flash , redirect
from froms import RegistraionForm , LoginForm
from flask_sqlalchemy import SQLAlchemy
# from modles import Post , User it would not work here because here it dose not know the defination of db in User and Post modle
app= Flask(__name__)
app.config['SECRET_KEY']='2c825c978c06ec686a906ba21718df'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
# db = SQLAlchemy(app)
db = SQLAlchemy(app)
from modles import Post , User

@app.route("/")
def index():
    return render_template("index.html")





#  This is an other Route
@app.route("/home")
def home():
    #  sendind a variable through the rendwer templates
    var= "UsmanApplication"
    return render_template("home.html", myvar=var)




#  This is sthe Application route define here Loop 
@app.route("/application")
def application():
    vars=['First Application ', 'Second application', 'Third Application']
    return render_template('Application.html', apps=vars)





#  Route Register 
@app.route("/register" , methods=['POST', 'GET'])
def Register():
    form = RegistraionForm()
    if form.validate_on_submit():
        flash(f'Account created successfully {form.username.data}', 'success')
        return redirect(url_for('home'))
        
    return render_template("register.html" , form = form)






#  Route Login
@app.route("/login", methods=['POST', 'GET'])
def Login():
    form = LoginForm()
    #  checking credintale with out Data base
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    # return render_template("login.html" , form = form)