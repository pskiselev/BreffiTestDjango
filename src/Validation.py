import re


def phone_number_is_valid(phone_number):

    if len(phone_number) != 12:
        return False

    for i, num in enumerate(phone_number):
        if i == 0 and num != '+':
            return False
        if not num.isalnum() and i != 0:
            return False

    return True


def email_is_valid(email):
    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
    return False if re.match(regex, email) is None else True


def phone_is_valid(phone):
    regex = r'^((\+7|7|8)+([0-9]){10})$'
    return False if re.match(regex, phone) is None else True
