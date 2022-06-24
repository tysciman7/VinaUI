import os
import json

PROJECT_HOME = ''
CONFIG_FILE_NAME = 'CONFIG.json'
DATA_PATH = ''
VINA_PATH = ''
CONFIG_DATA = {}


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
def set_config(element, _path):
    global CONFIG_DATA
    global DATA_PATH
    global VINA_PATH
    if element == 'data_path':
        DATA_PATH = _path
    elif element == 'vina_path':
        VINA_PATH = _path
    else:
        print('Error with specified element:' + element)
        return -2

    if '' in [DATA_PATH, VINA_PATH]:
        print('One of the paths was not specified')
        return -3

    CONFIG_DATA = {
        'data_path': DATA_PATH,
        'vina_path': VINA_PATH
    }

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
    os.chdir(get_config('data_path'))
    if not os.path.isdir('Ligands'):
        os.mkdir('Ligands')
    if not os.path.isdir('Receptors'):
        os.mkdir('Receptors')
    if not os.path.isdir('Ligand Outputs'):
        os.mkdir('Ligand Outputs')
    if not os.path.isdir('Logs'):
        os.mkdir('Logs')


