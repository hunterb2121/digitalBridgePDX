from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField, RadioField, HiddenField
from wtforms.validators import DataRequired, Email, Regexp, Length


phone_pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"


class DonateForm(FlaskForm):
    form_type = HiddenField(
        default="donate"
    )

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

    donate_type = RadioField(
        "What are you planning on donating?", 
        validators=[
            DataRequired(
                message="Please let us know what you are going to be donating"
            )
        ], 
        choices=[
            ("computer", "Computer"), 
            ("cell phone", "Cell Phone"), 
            ("tablet", "Tablet"),
            ("other device", "Other Device"), 
            ("money", "Money")
        ],
        default="computer"
    )

    message = TextAreaField(
        "Information On Your Donation", 
        validators=[
            Length(
                max=5000, 
                message="Message must be 5000 characters or less"
            )
        ]
    )

    submit = SubmitField("Submit")