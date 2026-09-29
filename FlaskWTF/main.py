from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,length
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)

app.secret_key="some key"

class LoginForm(FlaskForm):
    email=StringField("email",render_kw={"size":30},validators=[DataRequired(),Email()])
    password=PasswordField("password",render_kw={"size":30},validators=[DataRequired(),length(min=8)])
    submit=SubmitField("Login")
@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        return "<h1>Login Successful</h1>"
    return render_template('login.html',form=form)

@app.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
