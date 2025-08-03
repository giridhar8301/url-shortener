import re
import random
import string

def is_valid_url(url):
    regex = re.compile(
        r'^(https?:\/\/)?'  # http:// or https://
        r'([\da-z\.-]+)\.([a-z\.]{2,6})'  # domain
        r'([\/\w \.-]*)*\/?$'  # path
    )
    return re.match(regex, url) is not None

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
