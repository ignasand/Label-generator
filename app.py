from flask import Flask, render_template, send_file, request
from flask_bootstrap import Bootstrap
from flask_colorpicker import colorpicker

from flask_debugtoolbar import DebugToolbarExtension

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length, NumberRange
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import base64

from label_pil import suggar_num_to_str_en, generate_label

from wine_classifier_load import prediction

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
colorpicker(app)

app.debug = True
# toolbar = DebugToolbarExtension(app)

class LabelForm(FlaskForm):
    title1 = StringField('Enter title', default="Dragon balls", validators=[DataRequired(), Length(max=25)])
    title2 = StringField('Enter type', default="Grape wine", validators=[DataRequired(), Length(max=25)])
    number_alcohol = DecimalField('Enter alcohol (% by vol)', default=11,
                                  validators=[DataRequired(), NumberRange(min=0, max=50, message=None)])
    number_years = IntegerField('Enter years', default=2019,
                                validators=[DataRequired(), NumberRange(min=1900, max=2200, message=None)])
    number_sweetness = DecimalField('Enter residual sugar (g/l)', default=44,
                                    validators=[NumberRange(min=0, max=300, message=None)])
    radio = RadioField('Label', choices=[('C1', 'Single label'), ('C2', '25 labels on a4 size (150dpi)')], default='C1')

    submit = SubmitField('Generate label')

class PredictForm(FlaskForm):
    residualSugar = DecimalField('Enter residual sugar (g/l)', default=5,
                                  validators=[DataRequired(), NumberRange(min=0, max=300, message=None)])
    ph = DecimalField('Enter pH', default=3.0,
                                  validators=[DataRequired(), NumberRange(min=2.5, max=4, message=None)])
    alcohol = DecimalField('Enter alcohol (% by vol)', default=11,
                                  validators=[DataRequired(), NumberRange(min=8, max=16, message=None)])
    submit = SubmitField('Check quality')


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


def load_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=100)
    img_temp = base64.b64encode(img_io.getvalue())
    return img_temp.decode('ascii')

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
    img2 = None
    color_var = 'rgb(255,255,255)'

    if form.validate_on_submit():
        if form.radio.data == 'C1':
            title1 = form.title1.data
            title2 = form.title2.data
            if color_var != request.form.get('rgb'):
                color_var = request.form.get('rgb')
            number_alcohol = form.number_alcohol.data
            number_years = form.number_years.data
            number_sweetness = form.number_sweetness.data
            number_sweetness = suggar_num_to_str_en(number_sweetness)

            # img = Image.new(mode="RGB", size=(200, 200), color=(255, 255, 255))
            img = generate_label(title1, title2, number_alcohol, number_years, number_sweetness, color_var)
            # return serve_pil_image(img)
            img2 = load_image(img)
        if form.radio.data == 'C2':
            title1 = form.title1.data
            title2 = form.title2.data
            if color_var != request.form.get('rgb'):
                color_var = request.form.get('rgb')
            number_alcohol = form.number_alcohol.data
            number_years = form.number_years.data
            number_sweetness = form.number_sweetness.data
            number_sweetness = suggar_num_to_str_en(number_sweetness)
            img = generate_label(title1, title2, number_alcohol, number_years, number_sweetness, color_var)

            img_multy = Image.new("RGB", (1240, 1754))
            for i in range(0, 5):
                for j in range(0, 5):
                    img_multy.paste(img, (i * int(1240 / 5), j * int(1754 / 5)))
                    img_multy.paste(img, (i * int(1240 / 5), j * int(1754 / 5)))
                    img_multy.paste(img, (i * int(1240 / 5), j * int(1754 / 5)))
                    img_multy.paste(img, (i * int(1240 / 5), j * int(1754 / 5)))
                    img_multy.paste(img, (i * int(1240 / 5), j * int(1754 / 5)))

            img2 = load_image(img_multy)

    return render_template('label.html', form=form, img2=img2, color_var=color_var)

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

@app.route('/predict', methods=['GET','POST'])
def predict():
    quality = None
    residualSugar = None
    ph = None
    alcohol = None
    form = PredictForm()

    if form.validate_on_submit():
        residualSugar = form.residualSugar.data
        ph = form.ph.data
        alcohol = form.alcohol.data
        quality = prediction(residualSugar, ph, alcohol)

    return render_template('predict.html', form=form, quality=quality)


