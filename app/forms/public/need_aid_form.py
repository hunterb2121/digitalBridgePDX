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
        validators=[DataRequired()]
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

    aid_type = RadioField(
        "Type of aid needed", 
        validators=[
            DataRequired()
        ], 
        choices=[
            ("computer", "Computer"), 
            ("cell_phone", "Cell Phone"), 
            ("tablet", "Tablet"), 
            ("bills", "Bills"), 
            ("other", "Other")
        ],
        default="computer"
    )

    income = RadioField(
        "Yearly Income", 
        validators=[
            DataRequired()
        ], 
        choices=[
            ("lower", "Less than $30,001"), 
            ("lower_middle", "$30,001 - $58,020"), 
            ("middle", "$58,021 - $94,000"), 
            ("middle_upper", "94,001 - $153,000"), 
            ("upper", "Greater than $153,000")
        ],
        default="lower"
    )

    message = TextAreaField(
        "Information On Your Needs", 
        validators=[
            DataRequired(), 
            Length(
                max=5000, 
                message="Message must be 5000 characters or less"
            )
        ]
    )

    submit = SubmitField("Submit")