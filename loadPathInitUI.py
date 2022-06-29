from PyQt5.QtWidgets import QLineEdit, QPushButton, QFileDialog, QDialog, QCheckBox, QGroupBox, QLabel
from PyQt5 import uic
import os

import directoryManager
import errorMessageBoxes
import errorMessageBoxes as showError


class PathDialog(QDialog):
    def __init__(self, call_type=None):
        super(PathDialog, self).__init__()

        # Load pathDialog()
        os.chdir(directoryManager.get_project_path())
        uic.loadUi('pathInitDialog.ui', self)
        self.setWindowTitle('Initialize Data and Vina Paths')

        # Load Main Widgets
        self.data_path = self.findChild(QLineEdit, 'data_lineedit')
        self.vina_path = self.findChild(QLineEdit, 'vina_lineedit')
        self.data_button = self.findChild(QPushButton, 'data_pushbutton')
        self.vina_button = self.findChild(QPushButton, 'vina_pushbutton')

        # Load Sub Widgets
        self.sub_paths_checkbox = self.findChild(QCheckBox, 'sub_paths_checkbox')
        self.sub_path_group = self.findChild(QGroupBox, 'sub_path_groupbox')
        self.ligand_path = self.findChild(QLineEdit, 'ligand_lineedit')
        self.receptor_path = self.findChild(QLineEdit, 'receptor_lineedit')
        self.output_path = self.findChild(QLineEdit, 'output_lineedit')
        self.log_path = self.findChild(QLineEdit, 'log_lineedit')
        self.ligand_button = self.findChild(QPushButton, 'ligand_pushbutton')
        self.receptor_button = self.findChild(QPushButton, 'receptor_pushbutton')
        self.output_button = self.findChild(QPushButton, 'output_pushbutton')
        self.log_button = self.findChild(QPushButton, 'log_pushbutton')

        # Something
        if call_type is not None:
            self.data_path.setText(directoryManager.get_config('data_path'))
            self.vina_path.setText(directoryManager.get_config('vina_path'))
            self.ligand_path.setText(directoryManager.get_config('ligand_path'))
            self.receptor_path.setText(directoryManager.get_config('receptor_path'))
            self.output_path.setText(directoryManager.get_config('output_path'))
            self.log_path.setText(directoryManager.get_config('log_path'))


        # Widget Tips

        # Button Actions
        self.vina_button.clicked.connect(lambda: self.vina_path_search())
        self.data_button.clicked.connect(lambda: self.data_path_search())
        self.sub_paths_checkbox.stateChanged.connect(lambda: self.sub_paths_check())
        self.ligand_button.clicked.connect(lambda: self.ligand_path_search())
        self.receptor_button.clicked.connect(lambda: self.receptor_path_search())
        self.output_button.clicked.connect(lambda: self.output_path_search())
        self.receptor_button.clicked.connect(lambda: self.log_path_search())
        self.accepted.connect(lambda: self.pass_paths())
        self.rejected.connect(lambda: self.dialog_cancel(call_type))

    def vina_path_search(self):
        print('Vina path')
        _vina_file_path = QFileDialog.getOpenFileName(self, 'Please Select Vina.exe')
        if check_vina_path(_vina_file_path[0]):
            print('Correct File Found')
            self.vina_path.setText(_vina_file_path[0])
        else:
            showError.vina_error()
            print('Incorrect File Chosen')

    def data_path_search(self):
        print('Data Path Search')
        _data_dir_path = QFileDialog.getExistingDirectory(self,
                                                          'Please Choose a Directory for Data to accessed/ stored')
        self.data_path.setText(_data_dir_path)
        self.sub_paths_init()

    def sub_paths_check(self):
        if self.sub_paths_checkbox.isChecked():
            print('Enable Sub Path Editing')
            [label.setEnabled(True) for label in self.sub_path_group.findChildren(QLabel)]
            [lineedit.setEnabled(True) for lineedit in self.sub_path_group.findChildren(QLineEdit)]
            [button.setEnabled(True) for button in self.sub_path_group.findChildren(QPushButton)]
        else:
            [label.setEnabled(False) for label in self.sub_path_group.findChildren(QLabel)]
            [lineedit.setEnabled(False) for lineedit in self.sub_path_group.findChildren(QLineEdit)]
            [button.setEnabled(False) for button in self.sub_path_group.findChildren(QPushButton)]
            self.sub_paths_init()

    def sub_paths_init(self):
        if self.data_path.text() == '':
            print('No Data Path Specified')
            errorMessageBoxes.no_data_path_specified()
            return -4

        _ligand_path = os.path.join(self.data_path.text(), 'Ligands')
        _receptor_path = os.path.join(self.data_path.text(), 'Receptors')
        _output_path = os.path.join(self.data_path.text(), 'Outputs')
        _log_path = os.path.join(self.data_path.text(), 'Logs')

        self.ligand_path.setText(_ligand_path)
        self.receptor_path.setText(_receptor_path)
        self.output_path.setText(_output_path)
        self.log_path.setText(_log_path)

    def ligand_path_search(self):
        print('Ligand Path Search')
        _ligand_dir_path = QFileDialog.getExistingDirectory(self,
                                                            'Please Choose a Directory for Ligands to accessed')
        self.ligand_path.setText(_ligand_dir_path)

    def receptor_path_search(self):
        print('Receptor Path Search')
        _receptor_dir_path = QFileDialog.getExistingDirectory(self,
                                                              'Please Choose a Directory for Receptors to accessed')
        self.receptor_path.setText(_receptor_dir_path)

    def output_path_search(self):
        print('Output Path Search')
        _output_dir_path = QFileDialog.getExistingDirectory(self,
                                                            'Please Choose a Directory for Output to accessed / stored')
        self.output_path.setText(_output_dir_path)

    def log_path_search(self):
        print('Log Path Search')
        _log_dir_path = QFileDialog.getExistingDirectory(self,
                                                         'Please Choose a Directory for Logs to accessed / stored')
        self.log_path.setText(_log_dir_path)

    def pass_paths(self):
        directoryManager.set_config('data_path', self.data_path.text())
        directoryManager.set_config('ligand_path', self.ligand_path.text())
        directoryManager.set_config('receptor_path', self.receptor_path.text())
        directoryManager.set_config('output_path', self.output_path.text())
        directoryManager.set_config('log_path', self.log_path.text())

        if check_vina_path(self.vina_path.text()):
            directoryManager.set_config('vina_path', self.vina_path.text())
        else:
            showError.vina_error()
            self.vina_path.clear()
            self.show()


def check_vina_path(_path):
    if str(_path[-8:]) == "vina.exe":
        return True
    else:
        return False


def dialog_cancel(_call_type):
    if _call_type is None:
        showError.no_paths_init()
