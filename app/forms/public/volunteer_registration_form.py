from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField, RadioField, HiddenField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, Regexp, Length
from ...models.VolunteerJobsModel import VolunteerJobsModel


phone_pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"

jobs = VolunteerJobsModel.get_all_records() or []
print(f"Volunteer jobs: {jobs}")


class VolunteerRegistrationForm(FlaskForm):
    form_type = HiddenField(
        default="volunteer"
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

    volunteer_job = SelectMultipleField(
        "What are you interested in volunteering to do?",
        choices=[
            (t[1].lower(), t[1].title()) for t in jobs
        ],
        validate_choice=True,
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
    )

    experience_in_it = RadioField(
        "Do you have experience working in IT?",
        validators=[
            DataRequired(
                message="Please select if you have experience in IT"
            )
        ],
        choices=[
            ("yes", "Yes"),
            ("no", "No")
        ]
    )

    other_experience = RadioField(
        "Do you have experience working in any other field related to our volunteer opportunities?",
        validators=[
            DataRequired(
                message="Please select if you have experience in our other volunteer opportunities"
            )
        ],
        choices=[
            ("yes", "Yes"),
            ("no", "No")
        ]
    )

    experience_amount = RadioField(
        "How much experience do you have in your main field?",
        validators=[
            DataRequired(
                message="Please select how much experience you have"
            )
        ],
        choices=[
            ("0-1", "0 - 1 years"),
            ("1-5", "1 - 5 years"),
            ("5-10", "5 - 10 years"),
            ("10+", "Over 10 years")
        ]
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