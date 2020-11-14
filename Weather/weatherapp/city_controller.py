import json
import os


def get_all_city_names_starting_with_v():
    path = os.path.dirname(os.path.realpath(__file__))
    path_to_file = path + "/city_data.json"
    with open(path_to_file, 'r') as data:
        city_list = json.loads(data.read())
        city_name_list = []
        for city in city_list:
            city_name_list.append(city['name'])
        return city_name_list
