from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField, RadioField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, Regexp, Length


phone_pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"


class TechSupportForm(FlaskForm):
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

    support_location = RadioField(
        "Where do you need support?", 
        validators=[
            DataRequired(
                message="Please select where you would like to receive support"
            )
        ], 
        choices=[
            ("in-person", "In-Person Event"), 
            ("in-home", "In-Home"), 
            ("over-the-phone", "Over the Phone")
        ],
        default="in-person"
    )

    preferred_times = SelectMultipleField(
        "Preferred Times",
        choices=[
            ("morning", "Morning"),
            ("afternoon", "Afternoon"),
            ("evening", "Evening")
        ],
        validate_choice=True,
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
    )

    message = TextAreaField(
        "Problem Description", 
        validators=[
            DataRequired(
                message="Please give us some information on your issue"
            ),
            Length(
                max=5000, 
                message="Message must be 5000 characters or less"
            )
        ]
    )

    submit = SubmitField("Submit")