from random import choice

EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]
counts = [10, 100, 1000, 100000, 1000000]
list_freq = []

for count in counts:
    eagle_count = 0
    tails_count = 0

    for _ in range(count):
        result = choice(coin)
        if result == EAGLE:
            eagle_count += 1
        else:
            tails_count += 1

    min_count = min(eagle_count, tails_count)
    max_count = max(eagle_count, tails_count)

    if max_count == 0:
        list_freq.append(0)
    else:
        list_freq.append(min_count / max_count)

print(list_freq)