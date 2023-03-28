import re

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PASSWORD_REGEX = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'

def is_valid_email(email):
    return bool(re.match(EMAIL_REGEX, email))

def is_valid_password(password):
    return bool(re.match(PASSWORD_REGEX, password))
