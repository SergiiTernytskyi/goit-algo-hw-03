import re

def normalize_phone(phone_number):
    sanitized_number = re.sub(r'[^\+\d]', '', phone_number)
    if not sanitized_number.startswith('+'):
        if sanitized_number.startswith('380'):
            sanitized_number = '+' + sanitized_number
        elif sanitized_number.startswith('0'):
            sanitized_number = '+38' + sanitized_number
    return sanitized_number
