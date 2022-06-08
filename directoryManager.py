import os
import json

PROJECT_HOME = os.getcwd()
CONFIG_FILE_NAME = 'CONFIG'


def init_config(ui):
    os.chdir(PROJECT_HOME)
    if not os.path.exists(CONFIG_FILE_NAME):
        open(CONFIG_FILE_NAME, 'w').close()
        ui.initialize_data_dir()
    init_data_directory()

def set_config(config_data):
    os.chdir(PROJECT_HOME)
    with open(CONFIG_FILE_NAME, 'w') as _config_file:
        json.dump(config_data, _config_file)

def get_config():
    os.chdir(PROJECT_HOME)
    with open(CONFIG_FILE_NAME, 'r') as _config_file:
        return json.load(_config_file)

def init_data_directory():
    os.chdir(get_config())
    if not os.path.isdir('Ligands'):
        os.mkdir('Ligands')
    if not os.path.isdir('Receptors'):
        os.mkdir('Receptors')
    if not os.path.isdir('Ligand Outputs'):
        os.mkdir('Ligand Outputs')
    if not os.path.isdir('Logs'):
        os.mkdir('Logs')


