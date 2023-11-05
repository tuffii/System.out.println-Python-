import random


def generate_three_digit_number():
    hundreds = random.randint(0, 9)
    tens = random.randint(0, 9)
    ones = random.randint(0, 9)

    result = hundreds * 100 + tens * 10 + ones

    return result


random_number = generate_three_digit_number()
print(random_number)
