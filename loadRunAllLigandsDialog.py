from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox, QFileDialog
from PyQt5 import uic
import os
import fnmatch
from shutil import copy2
import directoryManager
import errorMessageBoxes as showError
import runFunctions
import sortData


class RunAllLigandsDialog(QDialog):
    def __init__(self, main_ui, vina_conf):
        super(RunAllLigandsDialog, self).__init__()

        # Load RunAllLigandsDialog
        os.chdir(directoryManager.get_project_path())
        uic.loadUi('runAllLigandsDialog.ui', self)

        # Load Widgets
        self.ligand_list = self.findChild(QComboBox, 'ligand_combobox')
        self.ligand_path_button = self.findChild(QPushButton, 'ligand_path_pushbutton')
        self.ligand_refresh = self.findChild(QPushButton, 'ligand_refresh_pushbutton')
        self.total_ligands = self.findChild(QLabel, 'total_ligands_output_label')
        self.output_path_input = self.findChild(QLineEdit, 'output_path_lineedit')
        self.output_path_button = self.findChild(QPushButton, 'output_path_pushbutton')
        self.output_path_label = self.findChild(QLabel, 'output_path_label')
        self.sort_checkbox = self.findChild(QCheckBox, 'sort_checkbox')

        # Initialize
        self.main_ui = main_ui
        self.vina_conf = vina_conf
        self.set_ligands(directoryManager.get_config('ligand_path'))
        self.sort_check()
        self.output_parent_path = None
        self.output_path = None
        self.log_path = None

        # Button Actions
        self.ligand_path_button.clicked.connect(lambda: self.ligand_path_search())
        self.ligand_refresh.clicked.connect(lambda: self.set_ligands(directoryManager.get_config('ligand_path')))
        self.sort_checkbox.stateChanged.connect(lambda: self.sort_check())
        self.output_path_button.clicked.connect(lambda: self.output_path_search())
        self.accepted.connect(lambda: self.run())
        self.rejected.connect(lambda: cancel_all())

    def set_ligands(self, _ligand_path):
        self.ligand_list.clear()
        os.chdir(_ligand_path)
        _ligand_list = fnmatch.filter(os.listdir(), '*.pdbqt')
        self.ligand_list.addItems(_ligand_list)
        self.total_ligands.setText(str(len(_ligand_list)))

    def ligand_path_search(self):
        print('Ligand Path Search')
        _ligand_dir_path = QFileDialog.getExistingDirectory(self,
                                                            'Please Choose a Directory for Ligands to be accessed')
        if _ligand_dir_path == '':
            print('No new ligand path specified')
            return -1
        self.set_ligands(_ligand_dir_path)
        directoryManager.set_config('ligand_path', _ligand_dir_path, True)

    def output_path_search(self):
        print('Output Path Search')
        _output_dir_path = QFileDialog.getExistingDirectory(self,
                                                            'Please Choose a Directory for Output to be stored')
        self.output_parent_path = os.path.join(_output_dir_path, 'Run_All_Ligands ' + str(directoryManager.get_current_date_time()))
        self.output_path = os.path.join(self.output_parent_path, 'Output')
        self.log_path = os.path.join(self.output_parent_path, 'Log')
        self.output_path_input.setText(self.output_parent_path)

    def output_enabled(self, _enabled):
        if not _enabled:
            self.output_path_input.clear()
        self.output_path_input.setEnabled(_enabled)
        self.output_path_button.setEnabled(_enabled)
        self.output_path_label.setEnabled(_enabled)

    def sort_check(self):
        if not self.sort_checkbox.isChecked():
            self.output_enabled(False)
        else:
            self.output_enabled(True)

    def run(self):
        if len(self.ligand_list) == 0:
            print('No Ligands in Chosen Directory')
            showError.no_ligands()
            return -5
        if self.sort_checkbox.isChecked() and self.output_path_input.text() == '':
            print('No Output path specified')
            showError.no_output_path()
            return -6
        if self.sort_checkbox.isChecked():
            directoryManager.set_config('output_path', self.output_path, True)
            directoryManager.set_config('log_path', self.log_path, True)
            os.mkdir(self.output_parent_path)
            os.chdir(self.output_parent_path)
            os.mkdir(self.output_path)
            os.mkdir(self.log_path)

        runFunctions.run_all_ligands(self.main_ui, self.vina_conf)

        if self.sort_checkbox.isChecked():
            sortData.sort_log_data(directoryManager.get_config('log_path'))
            _conf_path = os.path.join(directoryManager.get_config('data_path'), 'conf.txt')
            copy2(_conf_path, self.output_parent_path)


def cancel_all():
    directoryManager.load_config()
