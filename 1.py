import random


def get_unique_list_numbers(size=15, min_num=-10, max_num=10):
    if size > (max_num - min_num + 1):
        raise ValueError("Размер списка больше, чем количество уникальных чисел в указанном диапазоне.")

    unique_numbers = set()
    while len(unique_numbers) < size:
        unique_numbers.add(random.randint(min_num, max_num))

    return list(unique_numbers)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
