def find_common_participants(first_str, second_str, sep=','):
    participants1 = first_str.split(sep)
    participants2 = second_str.split(sep)
    set1 = set(participants1)
    set2 = set(participants2)
    common_participants = set1.intersection(set2)
    result = sorted(list(common_participants))
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, sep='|'))
