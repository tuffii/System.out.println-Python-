import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    sum_of_products = 0.0

    for item in data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)

        sum_of_products += score * weight

    return round(sum_of_products, 3)


print(task())
