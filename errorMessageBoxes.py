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


def vina_error():
    _vina_error_msg = QMessageBox()
    _vina_error_msg.setWindowTitle('Error with Vina Path Selection')
    _vina_error_msg.setText('Vina path was not selected correctly please locate vina.exe')
    _vina_error_msg.exec()


def no_paths_init():
    _no_path_error_msg = QMessageBox()
    _no_path_error_msg.setWindowTitle('No Paths Initialized')
    _no_path_error_msg.setText('This program will not run without first initializing the paths')
    _no_path_error_msg.exec()
