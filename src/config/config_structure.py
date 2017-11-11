from config.config import get_config_json


def get_cfg_structure():
    #
    return get_config_json('structure')['structure']


def get_cfg_structure_name():
    #
    return get_cfg_structure()['name']


def get_cfg_structure_town():
    #
    return get_cfg_structure()['town']


def get_cfg_structure_id():
    #
    return get_cfg_structure()['id']


def get_cfg_structure_postcode():
    #
    return get_cfg_structure()['postcode']