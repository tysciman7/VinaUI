import sys

from PyQt5.QtWidgets import QMessageBox


# Dealing with User Errors
class MessageBox(QMessageBox):
    def __init__(self, msg_title, msg_text, msg_icon):
        super(MessageBox, self).__init__()
        self.setWindowTitle(msg_title)
        self.setText(msg_text)
        self.msg_icon = None

        if msg_icon == 'warning':
            self.setIcon(self.Icon.Warning)
        elif msg_icon == 'critical':
            self.setIcon(self.Icon.Critical)
            sys.exit()


# Errors Handled with Main Window

# Informs user of error with populating previous configuration data
def pop_error():
    MessageBox('Populate Previous Data Error',
               'Error with previous configuration file, please manually enter data',
               'warning'
               ).exec()


# Informs user of error with seed selection
def seed_error():
    MessageBox('Seed Selection Error',
               'Please indicate either specific seed or random seed',
               'warning'
               ).exec()


# Informs the user of blank lineedit within conf data
def blank_field(field):
    MessageBox('Blank Field Encountered',
               field + ' cannot be blank',
               'warning'
               ).exec()


#
def non_int(field):
    MessageBox('Non-Integer Field Encountered',
               field + ' can only contain integers',
               'warning'
               ).exec()


# Errors Handled with PathDialog

# Informs user that they have not specified a correct vina path
def vina_error():
    MessageBox('Error with Vina Path Selection',
               'Vina path was not selected correctly please locate vina',
               'warning'
               ).exec()


# Informs user that they must specify paths or vina will be unable to run
def no_paths_init():
    MessageBox('No Paths Initialized',
               'This program will not run without first initializing the paths',
               'critical'
               ).exec()


# Informs user that they must first specify a data path before continuing below
def no_data_path_specified():
    MessageBox('No Data Path Specified',
               'Please Specify a Data Path',
               'warning'
               ).exec()


# Errors Handled with RunAll Dialog
# Informs user that the selected directory has no ligands within
def no_ligands():
    MessageBox('No Ligands Available',
               'No ligands are in selected directory',
               'warning'
               ).exec()


# Informs user that they have not specified an output directory
def no_output_path():
    MessageBox('No Output Specified',
               'Please Specify an Output File',
               'warning'
               ).exec()


def vina_error_stder(error):
    vina_stder = QMessageBox()
    vina_stder.setWindowTitle('Error')
    vina_stder.setText('Vina Error: ' + str(error))
    vina_stder.setIcon(vina_stder.Warning)
    vina_stder.exec()
