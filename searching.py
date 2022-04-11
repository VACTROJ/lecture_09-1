import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field in set(data.keys()):
        return data[field]

def linear_search(sequence, number):
    idx = 0
    positions = []
    count = 0
    for i in sequence:
        if i == number:
            positions.append(idx)
            count = count + 1
            idx = idx + 1
        else:
            idx = idx + 1
    output = dict()
    output["positions"] = positions
    output["count"] = count
    return output



def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)
    number_count = linear_search(unordered_numbers, 0)
    print(number_count)


if __name__ == '__main__':
    main()