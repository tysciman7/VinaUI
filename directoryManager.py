import os
import json

PROJECT_HOME = os.getcwd()
CONFIG_FILE_NAME = 'CONFIG.json'
DATA_PATH = ''
VINA_PATH = ''
CONFIG_DATA = {}


def init_config(ui):
    os.chdir(PROJECT_HOME)
    if not os.path.exists(CONFIG_FILE_NAME):
        open(CONFIG_FILE_NAME, 'w').close()
        ui.initialize_data_path()
        ui.initialize_vina_path()
    else:
        load_config()
    init_data_directory()


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


def load_config():
    global CONFIG_DATA
    os.chdir(PROJECT_HOME)
    with open(CONFIG_FILE_NAME, 'r') as _config_file:
        CONFIG_DATA = json.load(_config_file)


def get_config(element):
    os.chdir(PROJECT_HOME)
    if element in CONFIG_DATA.keys():
        return CONFIG_DATA[element]
    else:
        print('Unknown element entered')


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


