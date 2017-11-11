import json
import os
import ast


def write_config(new_data, config_type):
    try:
        #
        try:
            new_data = ast.literal_eval(new_data)
        except:
            new_data = new_data
        #
        file_name = 'config_{type}.json'.format(type=config_type)
        #
        with open(os.path.join(os.path.dirname(__file__), 'config_files', file_name), 'w+') as output_file:
            output_file.write(json.dumps(new_data, indent=4, separators=(',', ': ')))
            output_file.close()
        #
        return True
    except Exception as e:
        return False


def get_config_json(config_type):
    #
    file_name = 'config_{type}.json'.format(type=config_type)
    #
    with open(os.path.join(os.path.dirname(__file__), 'config_files', file_name), 'r') as data_file:
        return json.load(data_file)