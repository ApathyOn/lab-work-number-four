#import random
#from string import ascii_letters, digits, punctuation

#chars = ascii_letters + digits + "!@#$*?"

import random

def password_generator(chars):
    """Генератор случайных паролей длиной 12 символов из chars."""
    while True:
        yield ''.join(random.choice(chars) for _ in range(12))