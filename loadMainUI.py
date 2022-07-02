from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QComboBox, QSpinBox, QCheckBox, QPushButton, QAction, \
    QStatusBar, QFileDialog
from PyQt5 import uic
import os
import fnmatch
import runFunctions as runVina
import directoryManager
import errorMessageBoxes as showError
from loadPathInitUI import PathDialog
import sortData
from loadRunAllLigandsDialog import RunAllLigandsDialog


class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()

        # Load the MainUI file
        uic.loadUi("vinaMainWindow.ui", self)

        # Define Widgets
        self.receptor_list = self.findChild(QComboBox, 'receptor_comboBox')
        self.ligand_list = self.findChild(QComboBox, 'ligand_comboBox')
        self.refresh_lists = self.findChild(QPushButton, 'refresh_list_pushbutton')
        self.center_x = self.findChild(QLineEdit, 'center_x_lineedit')
        self.center_y = self.findChild(QLineEdit, 'center_y_lineedit')
        self.center_z = self.findChild(QLineEdit, 'center_z_lineedit')
        self.size_x = self.findChild(QLineEdit, 'size_x_lineedit')
        self.size_y = self.findChild(QLineEdit, 'size_y_lineedit')
        self.size_z = self.findChild(QLineEdit, 'size_z_lineedit')
        self.exhaustiveness = self.findChild(QLineEdit, 'exhaustiveness_lineedit')
        self.seed_value = self.findChild(QLineEdit, 'seed_lineedit')
        self.random_seed = self.findChild(QCheckBox, 'random_seed_checkbox')
        self.cpu_set = self.findChild(QSpinBox, 'cpu_spinbox')
        self.populate_previous = self.findChild(QPushButton, 'populate_config_pushbutton')
        self.selected_ligand = self.findChild(QPushButton, 'run_selected_ligand_pushbutton')
        self.all_ligands = self.findChild(QPushButton, 'run_all_ligands_pushbutton')
        self.reinit_paths = self.findChild(QAction, 'reconfigure_paths_action')
        self.sort_existing = self.findChild(QAction, 'sort_existing_action')
        self.status_bar = self.findChild(QStatusBar, 'statusbar')

        # Bounds CPU Core selection
        self.cpu_set.setRange(1, os.cpu_count())

        # Define Variables
        self.data_home = None

        # Button Actions
        self.refresh_lists.clicked.connect(lambda: self.pop_ligands())
        self.refresh_lists.clicked.connect(lambda: self.pop_receptors())
        self.populate_previous.clicked.connect(lambda: self.pop_previous_data())
        self.random_seed.stateChanged.connect(lambda: self.clear_seed_value())
        self.selected_ligand.clicked.connect(lambda: self.run_selected_ligand())
        self.all_ligands.clicked.connect(lambda: self.run_all_ligands())
        self.reinit_paths.triggered.connect(lambda: self.open_path_dialog('reinit'))
        self.sort_existing.triggered.connect(lambda: self.sort_existing_logs())

    # Prompts user to specify a directory to sort older/ existing log files
    def sort_existing_logs(self):
        _log_path = QFileDialog.getExistingDirectory(self, 'Log Path')
        if _log_path == '':
            return -1
        sortData.sort_log_data(_log_path, 'main')

    # Initializes the data path and fills the receptor and ligand combo boxes with their respective directories
    def init_all(self):
        self.data_home = directoryManager.get_config('data_path')
        self.pop_receptors()
        self.pop_ligands()

    # Call PathDialog
    def open_path_dialog(self, _call_type=None):
        PathDialog(_call_type).exec()
        self.init_all()

    # Fills the Ligand List with Ligands within Respective Directory
    def pop_ligands(self):
        print('Populating Ligand List')
        self.ligand_list.clear()
        os.chdir(directoryManager.get_config('ligand_path'))
        _ligand_list = fnmatch.filter(os.listdir(), '*.pdbqt')
        self.ligand_list.addItems(_ligand_list)
        # self.total_ligand_value.setText(str(len(_ligand_list)))

    # Fills the Receptor List with Receptors within Respective Directory
    def pop_receptors(self):
        print('Populating Receptor List')
        self.receptor_list.clear()
        os.chdir(directoryManager.get_config('receptor_path'))
        _receptor_list = fnmatch.filter(os.listdir(), '*.pdbqt')
        self.receptor_list.addItems(_receptor_list)

    # Populates configuration text boxes with previous config file (if it exists) if not then user is prompted
    def pop_previous_data(self):
        try:
            os.chdir(self.data_home)
            config_file = open("conf.txt", "r")
            config_file.readline()
            config_file.readline()
            _temp = config_file.readline()
            self.center_x.setText(_temp[11:-1])
            _temp = config_file.readline()
            self.center_y.setText(_temp[11:-1])
            _temp = config_file.readline()
            self.center_z.setText(_temp[11:-1])
            _temp = config_file.readline()
            self.size_x.setText(_temp[9:-1])
            _temp = config_file.readline()
            self.size_y.setText(_temp[9:-1])
            _temp = config_file.readline()
            self.size_z.setText(_temp[9:-1])
            _temp = config_file.readline()
            self.exhaustiveness.setText(_temp[17:-1])
            _temp = config_file.readline()
            self.cpu_set.setValue(int(_temp[6:-1]))
        except:
            print('Error with Populating Previous Data')
            showError.pop_error()

    # If User Selects to Use Randomized Seeds, The field associated with a Seed Value is cleared
    def clear_seed_value(self):
        print('Clearing Seed Value')
        if self.random_seed.isChecked():
            self.seed_value.clear()

    # If user did not select randomized seed and a seed is not provided
    # Then an error will show prompting the user for one or the other
    def valid_seed(self):
        if not (self.random_seed.isChecked()) and self.seed_value.text() == '':
            print('User needs to specify a seed(int) or select randomize seed')
            showError.seed_error()
            return False
        else:
            return True

    # If the user did not fill one of the configuration values then the user is prompted to fix said issues
    def valid_fields(self):
        fields = {'Center X': self.center_x.text(),
                  'Center Y': self.center_y.text(),
                  'Center Z': self.center_z.text(),
                  'Size X': self.size_z.text(),
                  'Size Y': self.size_y.text(),
                  'Size Z': self.size_z.text(),
                  'Exhaustiveness': self.exhaustiveness.text()
                  }

        for field in fields:
            if fields[field] == '':
                print(field + ' is empty')
                showError.blank_field(field)
                return False

            if not fields[field].isdigit():
                print(field + ' has a non-int type inputted')
                showError.non_int(field)
                return False

        return True

    # Takes all user inputted data and creates a dict to contain all variables
    def get_vina_conf_dict(self):
        vina_conf = {
            "Receptor": self.receptor_list.currentText(),
            "Ligand": '',
            "CenterX": self.center_x.text(),
            "CenterY": self.center_y.text(),
            "CenterZ": self.center_z.text(),
            "SizeX": self.size_x.text(),
            "SizeY": self.size_y.text(),
            "SizeZ": self.size_z.text(),
            "Exhaustiveness": self.exhaustiveness.text(),
            "Seed": self.seed_value.text(),
            "CPU": self.cpu_set.value()
        }
        return vina_conf

    # Calls the function to run the user selected ligand
    def run_selected_ligand(self):
        if not (self.valid_seed()) or not self.valid_fields():
            return
        else:
            _ligand = self.ligand_list.currentText()
            vina_conf = self.get_vina_conf_dict()
            vina_conf.update({"Ligand": _ligand})
            runVina.run_selected_ligand(vina_conf)

    # Calls the function to run all ligands in ligand directory
    def run_all_ligands(self):
        if not (self.valid_seed()) or not self.valid_fields():
            return
        else:
            self.status_bar.showMessage('Time Remaining: ')
            self.status_bar.repaint()
            _vina_conf = self.get_vina_conf_dict()
            RunAllLigandsDialog(self, _vina_conf).exec()

    # Updates status bar with a time remaining on a vina run
    def update_time_remaining(self, _time):
        self.status_bar.showMessage('Time Remaining: ' + f"{_time:.3f}")
        self.status_bar.repaint()
