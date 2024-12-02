from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp, Length


phone_pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"


class GeneralContactForm(FlaskForm):
    name = StringField(
        "Name", 
        validators=[
            DataRequired(
                message="Please enter your name"
            )
        ]
    )
    email = EmailField(
        "Email", 
        validators=[
            DataRequired(
                message="Please enter your email"
            ), 
            Email(
                message="Please enter a valid email"
            )
        ]
    )
    phone_number = TelField(
        "Phone Number", 
        validators=[
            Regexp(
                phone_pattern, 
                message="Please enter a valid phone number"
            )
        ]
    )
    message = TextAreaField(
        "Message", 
        validators=[
            DataRequired(
                message="Please enter your message for us"
            ), 
            Length(
                max=5000, 
                message="Message must be 5000 characters or less"
            )
        ]
    )
    submit = SubmitField("Submit")