from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QComboBox, QSpinBox, QCheckBox, QPushButton, QAction
from PyQt5 import uic
import os
import fnmatch
import runFunctions as runVina
import directoryManager
import errorMessageBoxes as showError
from loadPathInitUI import PathDialog


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
        os.chdir(self.data_home)
        os.chdir('Ligands')
        _ligand_list = fnmatch.filter(os.listdir(), '*.pdbqt')
        self.ligand_list.addItems(_ligand_list)
        # self.total_ligand_value.setText(str(len(_ligand_list)))

    # Fills the Receptor List with Receptors within Respective Directory
    def pop_receptors(self):
        print('Populating Receptor List')
        self.receptor_list.clear()
        os.chdir(self.data_home)
        os.chdir('Receptors')
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
    def check_entered_seed(self):
        if not (self.random_seed.isChecked()) and self.seed_value.text() == '':
            print('User needs to specify a seed(int) or select randomize seed')
            showError.seed_error()
            return False
        else:
            return True

    # If the user did not fill one of the configuration values then the user is prompted to fix said issues
    def check_empty_fields(self):
        if '' in [self.center_x.text(), self.center_y.text(), self.center_z.text(), self.size_z.text(),
                  self.size_y.text(), self.size_z.text(), self.exhaustiveness.text()]:
            print('One or more fields is empty Fields')
            showError.pop_error()
            return True
        else:
            return False

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
        if not (self.check_entered_seed()) or self.check_empty_fields():
            return
        else:
            _ligand = self.ligand_list.currentText()
            vina_conf = self.get_vina_conf_dict()
            vina_conf.update({"Ligand": _ligand})
            runVina.run_selected_ligand(vina_conf)

    # Calls the function to run all ligands in ligand directory
    def run_all_ligands(self):
        if not (self.check_entered_seed()) or self.check_empty_fields():
            return
        else:
            vina_conf = self.get_vina_conf_dict()
            runVina.run_all_ligands(self, vina_conf)



