from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField, RadioField, HiddenField
from wtforms.validators import DataRequired, Email, Regexp, Length


phone_pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"


class NeedAidForm(FlaskForm):
    form_type = HiddenField(
        default="need_aid"
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

    aid_type = RadioField(
        "Type of aid needed", 
        validators=[
            DataRequired(
                message="Please let us know what you need"
            )
        ], 
        choices=[
            ("computer", "Computer"), 
            ("cell phone", "Cell Phone"), 
            ("tablet", "Tablet"), 
            ("bills", "Bills"), 
            ("other", "Other")
        ],
        default="computer"
    )

    income = RadioField(
        "Yearly Income", 
        validators=[
            DataRequired(
                message="Please select your income to help us prioritize your request"
            )
        ], 
        choices=[
            ("less than 30,001", "Less than $30,001"), 
            ("30,001-58,020", "$30,001 - $58,020"), 
            ("58,021-94,000", "$58,021 - $94,000"), 
            ("94,001-153,000", "94,001 - $153,000"), 
            ("greater than 153,000", "Greater than $153,000")
        ],
        default="less than 30,001"
    )

    message = TextAreaField(
        "Information On Your Needs", 
        validators=[
            DataRequired(
                message="Please give us a little more information on your needs"
            ), 
            Length(
                max=5000, 
                message="Message must be 5000 characters or less"
            )
        ]
    )

    submit = SubmitField("Submit")