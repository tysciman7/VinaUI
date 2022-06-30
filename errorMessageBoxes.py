import sys

from PyQt5.QtWidgets import QMessageBox

# Dealing with User Errors


# Informs user of error with populating previous configuration data
def pop_error():
    _pop_error_msg = QMessageBox()
    _pop_error_msg.setWindowTitle('Populate Previous Data Error')
    _pop_error_msg.setText('Error with previous configuration file, please manually enter data')
    _pop_error_msg.setIcon(_pop_error_msg.Warning)
    _pop_error_msg.exec()


# Informs user of error with seed selection
def seed_error():
    _seed_error_msg = QMessageBox()
    _seed_error_msg.setWindowTitle('Seed Selection Error')
    _seed_error_msg.setText('Please indicate either specific seed or random seed')
    _seed_error_msg.setIcon(_seed_error_msg.Warning)
    _seed_error_msg.exec()


# Informs user that they have not specified a correct vina path
def vina_error():
    _vina_error_msg = QMessageBox()
    _vina_error_msg.setWindowTitle('Error with Vina Path Selection')
    _vina_error_msg.setText('Vina path was not selected correctly please locate vina.exe')
    _vina_error_msg.exec()


# Informs user that they must specify paths or vina will be unable to run
def no_paths_init():
    _no_path_error_msg = QMessageBox()
    _no_path_error_msg.setWindowTitle('No Paths Initialized')
    _no_path_error_msg.setText('This program will not run without first initializing the paths')
    _no_path_error_msg.setIcon(_no_path_error_msg.Critical)
    _no_path_error_msg.exec()
    sys.exit()


# Informs user that they must first specify a data path before continuing below
def no_data_path_specified():
    _no_data_path_msg = QMessageBox()
    _no_data_path_msg.setWindowTitle('No Data Path Specified')
    _no_data_path_msg.setText('Please Specify a Data Path')
    _no_data_path_msg.setIcon(_no_data_path_msg.Warning)
    _no_data_path_msg.exec()


# Informs user that the selected directory has no ligands within
def no_ligands():
    _no_ligands = QMessageBox()
    _no_ligands.setWindowTitle('No Ligands Available')
    _no_ligands.setText('No ligands are in selected directory')
    _no_ligands.setIcon(_no_ligands.Warning)
    _no_ligands.exec()


# Informs user that they have not specified an output directory
def no_output_path():
    _no_output = QMessageBox()
    _no_output.setWindowTitle('No Output Specified')
    _no_output.setText('Please Specify an Output File')
    _no_output.setIcon(_no_output.Warning)
    _no_output.exec()