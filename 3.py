import random
import string


def get_random_password(length=8):
    alphabet = string.ascii_letters + string.digits
    if length < 1:
        raise ValueError("Длина пароля должна быть положительным числом")
    random_password = ''.join(random.sample(alphabet, length))
    return random_password


print(get_random_password())
