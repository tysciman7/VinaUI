from PyQt5.QtWidgets import QLineEdit, QPushButton, QFileDialog, QDialog
from PyQt5 import uic
import os

import directoryManager
import errorMessageBoxes as showError


class PathDialog(QDialog):
    def __init__(self):
        super(PathDialog, self).__init__()

        # Load pathDialog()
        os.chdir(directoryManager.get_project_path())
        uic.loadUi('pathInitDialog.ui', self)
        self.setWindowTitle('Initialize Data and Vina Paths')

        # Load Widgets
        self.data_path = self.findChild(QLineEdit, 'data_lineedit')
        self.vina_path = self.findChild(QLineEdit, 'vina_lineedit')
        self.data_button = self.findChild(QPushButton, 'data_pushbutton')
        self.vina_button = self.findChild(QPushButton, 'vina_pushbutton')

        # Widget Tips

        # Button Actions
        self.data_button.clicked.connect(lambda: self.data_path_search())
        self.vina_button.clicked.connect(lambda: self.vina_path_search())
        self.accepted.connect(lambda: self.pass_paths())
        self.rejected.connect(lambda: showError.no_paths_init())

        # Show Dialog
        # self.show()

    def data_path_search(self):
        print('Data Path')
        _data_dir_path = QFileDialog.getExistingDirectory(self,
                                                          'Please Choose a Directory for Data to accessed/ stored')
        self.data_path.setText(_data_dir_path)

    def vina_path_search(self):
        print('Vina path')
        _vina_file_path = QFileDialog.getOpenFileName(self, 'Please Select Vina.exe')
        if self.check_vina_path(_vina_file_path[0]):
            print('Correct File Found')
            self.vina_path.setText(_vina_file_path[0])
        else:
            showError.vina_error()
            print('Incorrect File Chosen')

    def check_vina_path(self, _path):
        if str(_path[-8:]) == "vina.exe":
            return True
        else:
            return False

    def pass_paths(self):
        directoryManager.set_config('data_path', self.data_path.text())
        if self.check_vina_path(self.vina_path.text()):
            directoryManager.set_config('vina_path', self.vina_path.text())
        else:
            showError.vina_error()
            self.vina_path.clear()
            self.show()


# app = QApplication(sys.argv)
# dialog = PathDialog()
# app.exec()
