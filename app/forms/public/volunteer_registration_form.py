from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, Regexp, Length


phone_pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"


class VolunteerRegistrationForm(FlaskForm):
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

    volunteer_job = RadioField(
        "What are you donating?", 
        validators=[
            DataRequired()
        ], 
        choices=[
            ("computer", "Computer"), 
            ("cell_phone", "Cell Phone"), 
            ("tablet", "Tablet"),
            ("other_device", "Other Device"), 
            ("money", "Money"), 
        ],
        default="computer"
    )

    experience_in_it = RadioField(
        "Do you have experience working in IT?",
        validators=[
            DataRequired()
        ],
        choices=[
            ("yes", "Yes"),
            ("no", "No")
        ],
        default="yes"
    )

    other_experience = RadioField(
        "Do you have experience working in any other field related to our volunteer opportunities?",
        validators=[
            DataRequired()
        ]
        choices=[
            ("yes", "Yes"),
            ("no", "No")
        ],
        default="yes"
    )

    experience_amount = RadioField(
        "How much experience do you have in your main field?",
        validators=[
            DataRequired()
        ],
        choices=[
            ("0-1", "0 - 1 years"),
            ("1-5", "1 - 5 years"),
            ("5-10", "5 - 10 years"),
            ("10+", "Over 10 years")
        ],
        default="0-1"
    )

    message = TextAreaField(
        "Additional Information", 
        validators=[
            Length(
                max=5000, 
                message="Message must be 5000 characters or less"
            )
        ]
    )

    submit = SubmitField("Submit")