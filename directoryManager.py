import os
import json
from datetime import datetime

PROJECT_HOME = ''
CONFIG_FILE_NAME = 'CONFIG.json'

CONFIG_DATA = {
    'vina_path': None,
    'data_path': None,
    'ligand_path': None,
    'receptor_path': None,
    'output_path': None,
    'log_path': None,
}


def set_project_path(_path):
    global PROJECT_HOME
    PROJECT_HOME = _path


def get_project_path():
    return PROJECT_HOME


''' Checks for existing config file
 If it doesn't exist user is prompted for both data and vina paths
 If it does exist, the config data is read from existing file'''
def init_config(ui):
    os.chdir(PROJECT_HOME)
    if (not os.path.exists(CONFIG_FILE_NAME)) or (os.path.getsize(CONFIG_FILE_NAME) <= 5):
        open(CONFIG_FILE_NAME, 'w').close()
        ui.open_path_dialog()
    else:
        load_config()
    init_data_directory()


# Given a correct path element and the path itself, a config file is written and also stored in CONFIG_DATA variable
def set_config(element, _path, _temp=False):
    global CONFIG_DATA

    if element in CONFIG_DATA.keys():
        CONFIG_DATA[element] = _path
    else:
        print('Error with specified element:' + element)
        return -2

    if _temp:
        return 1

    if '' in CONFIG_DATA.values():
        print('One of the paths was not specified')
        return -3

    os.chdir(PROJECT_HOME)
    with open(CONFIG_FILE_NAME, 'w') as _config_file:
        json.dump(CONFIG_DATA, _config_file)


# Loads paths from config file to config variable
def load_config():
    global CONFIG_DATA
    os.chdir(PROJECT_HOME)
    with open(CONFIG_FILE_NAME, 'r') as _config_file:
        CONFIG_DATA = json.load(_config_file)


# Gets path associated with requested element within config
def get_config(element):
    os.chdir(PROJECT_HOME)
    if element in CONFIG_DATA.keys():
        return CONFIG_DATA[element]
    else:
        print('Unknown element entered')


# Checks root data directory for each directory associated with accessed / stored data
def init_data_directory():
    if not os.path.isdir(CONFIG_DATA['ligand_path']):
        os.mkdir(CONFIG_DATA['ligand_path'])
    if not os.path.isdir(CONFIG_DATA['receptor_path']):
        os.mkdir(CONFIG_DATA['receptor_path'])
    if not os.path.isdir(CONFIG_DATA['output_path']):
        os.mkdir(CONFIG_DATA['output_path'])
    if not os.path.isdir(CONFIG_DATA['log_path']):
        os.mkdir(CONFIG_DATA['log_path'])


def get_current_date_time():
    _current_date_time = str(datetime.now())
    _current_date_time = _current_date_time.replace(':', '.')
    _current_date_time = _current_date_time[0:-7]
    return _current_date_time