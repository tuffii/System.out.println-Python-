import csv
import json

INPUT_FILENAME = "input.csv"


def csv_to_json(input_filename: str) -> None:
    with open(input_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        headers = next(csv_reader)

        data_list = []

        for row in csv_reader:
            data_dict = {headers[i]: row[i] for i in range(len(headers))}
            data_list.append(data_dict)

    json_data = json.dumps(data_list, indent=4)
    print(json_data, end="")


csv_to_json(INPUT_FILENAME)
