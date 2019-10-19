from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class NumberForm(FlaskForm):
    number = DecimalField('Enter first number', validators=[DataRequired()])
    number2 = DecimalField('Enter second number', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts', methods=['GET','POST'])
def contacts():
    number = None
    number2 = None
    form = NumberForm()
    if form.validate_on_submit():
        number = form.number.data
        number2 = form.number2.data
        form.number.data = ''
        form.number2.data = ''

    return render_template('contacts.html', form=form, number=number, number2=number2)




