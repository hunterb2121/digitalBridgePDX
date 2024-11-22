from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email, Regexp, Length


phone_pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"


class PartnerRegistrationForm(FlaskForm):
    form_type = HiddenField(
        default="partner"
    )

    business_name = StringField(
        "Business Name",
        validators=[
            DataRequired()
        ]
    )

    contact_name = StringField(
        "Contact Person Name", 
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
            DataRequired(),
            Regexp(
                phone_pattern, 
                message="Please enter a valid phone number"
            )
        ]
    )

    message = TextAreaField(
        "Message", 
        validators=[
            Length(
                max=5000, 
                message="Message must be 5000 characters or less"
            )
        ]
    )

    submit = SubmitField("Submit")