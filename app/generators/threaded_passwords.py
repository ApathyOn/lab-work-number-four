import random
from string import ascii_letters, digits, punctuation
from concurrent.futures import ThreadPoolExecutor

chars = ascii_letters + digits + "!@#$*?"

def _gen_password():
    return ''.join(random.choice(chars) for _ in range(12))

def threaded_password_gen(count=10, threads=4):
    # Многопоточный генератор паролей
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = list(executor.map(lambda _: _gen_password(), range(count)))
    return results