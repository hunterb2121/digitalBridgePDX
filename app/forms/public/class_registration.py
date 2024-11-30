from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email, Regexp


phone_pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"


class ClassRegistrationForm(FlaskForm):
    identifier = HiddenField(
        default="class_registration"
    )

    schedule_id = HiddenField(
        default=None,
        validators=[
            DataRequired(
                message="Error with submitting your form. Please try again later. If issues persist, please submit a form on our contact page or send us an email at digitalbridgepdx@gmail.com and reference error code: 150"
            )
        ]
    )

    name = StringField(
        "Name", 
        validators=[
            DataRequired()
        ]
    )

    email = EmailField(
        "Email", 
        validators=[
            DataRequired(), 
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

    submit = SubmitField("Register")

