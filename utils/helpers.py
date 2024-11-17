import re

from flask import render_template


# Function to return an error message
def error(message, code):
    return render_template("error.html", message=message, code=code)


# Function to validate email on the backend just in case
def email_validation(email):
    if not isinstance(email, str):
        return False
    
    email = email.strip()
    pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"

    return bool(re.match(pattern, email))


# Function to validate phone number on the backend just in case
def phone_validation(phone):
    if not isinstance(phone, str):
        return False
    
    phone = phone.strip()
    pattern = r"^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"

    return bool(re.match(pattern, phone))