from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,FloatField
from wtforms.validators import DataRequired
from utils import get_estimated_price,load_saved_artifacts,get_location_names
app = Flask(__name__)
app.config['SECRET_KEY'] = 'i am good'

class MyForm(FlaskForm):
    squareft= FloatField('Square_Foot', validators=[DataRequired()])
    bath = IntegerField('Number of Bathrooms', validators=[DataRequired()])
    bhk= IntegerField('Number of Bedrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])

    submit = SubmitField('Result')
locations=get_location_names()

load_saved_artifacts()
@app.route('/', methods=['GET', 'POST'])
def index():
   
    form = MyForm()
    
    if form.validate_on_submit():
        # Process form data
        
        squareft = form.squareft.data
        bath = form.bath.data
        bhk = form.bhk.data
        location = form.location.data
        
        price=get_estimated_price(location,squareft,bhk,bath)
       
        return render_template('index.html',price=price,form=form,locations=locations)
        
    return render_template('index.html', form=form,locations=locations)

