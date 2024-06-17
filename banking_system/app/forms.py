# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  FloatField, SelectField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[InputRequired(), Length(min=6, max=50)])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=20)])

class TransactionForm(FlaskForm):
    amount = FloatField('Amount', validators=[InputRequired()])
    transaction_type = SelectField('Transaction Type', choices=[('deposit', 'Deposit'), ('withdraw', 'Withdraw')], validators=[InputRequired()])
