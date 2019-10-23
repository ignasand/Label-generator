from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

from label_pil import suggar_num_to_str_en, generate_label

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class NumberForm(FlaskForm):
    number = DecimalField('Enter first number', validators=[DataRequired()])
    number2 = DecimalField('Enter second number', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LabelForm(FlaskForm):
    title1 = StringField('Enter title', default="Marvelous", validators=[DataRequired()])
    title2 = StringField('Enter type', default="Grape wine", validators=[DataRequired()])
    number_alcohol = DecimalField('Enter alcohol (% by vol)', default=11, validators=[DataRequired()])
    number_years = IntegerField('Enter years', default=2019, validators=[DataRequired()])
    number_sweetness = DecimalField('Enter residual sugar (g/l)', default=44)
    submit = SubmitField('Generate label')

# def generate_label(title1, title2, number_alcohol, number_years, number_sweetness):
#     font_size = 20
#     font_color = 'rgb(0, 0, 0)'
#     font = ImageFont.truetype('fonts/Montserrat-Bold.otf', size=font_size)
#     font1 = ImageFont.truetype('fonts/Montserrat-Regular.otf', size=int(font_size))
#     font2 = ImageFont.truetype('fonts/Montserrat-Italic.otf', size=int(font_size / 1.2))
#
#     img = Image.new(mode="RGB", size=(200, 200), color=(255, 255, 255))
#     draw = ImageDraw.Draw(img)
#
#     draw.text((0, 0), title1, fill=font_color, font=font)
#     draw.text((0, 0 + font_size * 1), title2, fill=font_color, font=font)
#     draw.text((0, 0 + font_size * 2), str(number_alcohol), fill=font_color, font=font)
#     draw.text((0, 0 + font_size * 3), str(number_sweetness), fill=font_color, font=font)
#     draw.text((0, 0 + font_size * 4), str(number_years), fill=font_color, font=font)
#     return img


def do_calculations(number, number2):
    result = number / number2
    return result

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route('/img')
def serve_img():
    img = Image.new(mode="RGB", size=(200, 200), color=(28, 50, 150))
    return serve_pil_image(img)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/label', methods=['GET', 'POST'])
def label():
    form = LabelForm()
    title1 = None
    title2 = None
    number_alcohol = None
    number_years = None
    number_sweetness = None

    if form.validate_on_submit():
        title1 = form.title1.data
        title2 = form.title2.data
        number_alcohol = form.number_alcohol.data
        number_years = form.number_years.data
        number_sweetness = form.number_sweetness.data

        number_sweetness = suggar_num_to_str_en(number_sweetness)

        # img = Image.new(mode="RGB", size=(200, 200), color=(255, 255, 255))
        img = generate_label(title1, title2, number_alcohol, number_years, number_sweetness)
        return serve_pil_image(img)
    return render_template('label.html', form=form)

@app.route('/contacts', methods=['GET','POST'])
def contacts():
    number = None
    number2 = None
    result = None
    form = NumberForm()
    if form.validate_on_submit():
        number = form.number.data
        number2 = form.number2.data
        form.number.data = ''
        form.number2.data = ''
        result = do_calculations(number, number2)

    return render_template('contacts.html', form=form, number=number, number2=number2, result=result)




