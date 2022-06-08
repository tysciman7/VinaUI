import os
import fnmatch
from PyQt5 import QtCore, QtGui, QtWidgets
import runFunctions as runVina

# Used to make dirs in same folder
# DATA_HOME = os.getcwd()

# Used to make dirs one above
PATH_HOME = os.getcwd()
DATA_HOME = os.path.dirname(PATH_HOME)


# LOGS_FILE = DATA_HOME + '\Logs'
# OUTPUT_FILE = DATA_HOME + '\Ligand Outputs'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.receptorList = QtWidgets.QComboBox(self.centralwidget)
        self.receptorList.setGeometry(QtCore.QRect(80, 15, 170, 22))
        self.receptorList.setObjectName("receptorList")
        self.ligand = QtWidgets.QComboBox(self.centralwidget)
        self.ligand.setGeometry(QtCore.QRect(340, 15, 170, 22))
        self.ligand.setObjectName("ligand")
        self.receptorListLabel = QtWidgets.QLabel(self.centralwidget)
        self.receptorListLabel.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.receptorListLabel.setObjectName("receptorListLabel")
        self.ligandListLabel = QtWidgets.QLabel(self.centralwidget)
        self.ligandListLabel.setGeometry(QtCore.QRect(290, 20, 47, 13))
        self.ligandListLabel.setObjectName("ligandListLabel")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 121, 121))
        self.groupBox.setObjectName("groupBox")
        self.center_x = QtWidgets.QLineEdit(self.groupBox)
        self.center_x.setGeometry(QtCore.QRect(50, 30, 51, 20))
        self.center_x.setObjectName("center_x")
        self.center_y = QtWidgets.QLineEdit(self.groupBox)
        self.center_y.setGeometry(QtCore.QRect(50, 60, 51, 20))
        self.center_y.setObjectName("center_y")
        self.center_z = QtWidgets.QLineEdit(self.groupBox)
        self.center_z.setGeometry(QtCore.QRect(50, 90, 51, 20))
        self.center_z.setObjectName("center_z")
        self.cXlabel = QtWidgets.QLabel(self.groupBox)
        self.cXlabel.setGeometry(QtCore.QRect(20, 30, 21, 20))
        self.cXlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cXlabel.setObjectName("cXlabel")
        self.cYlabel = QtWidgets.QLabel(self.groupBox)
        self.cYlabel.setGeometry(QtCore.QRect(20, 60, 21, 16))
        self.cYlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cYlabel.setObjectName("cYlabel")
        self.cZlabel = QtWidgets.QLabel(self.groupBox)
        self.cZlabel.setGeometry(QtCore.QRect(20, 90, 21, 16))
        self.cZlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cZlabel.setObjectName("cZlabel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(170, 50, 121, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.size_x = QtWidgets.QLineEdit(self.groupBox_2)
        self.size_x.setGeometry(QtCore.QRect(50, 30, 51, 20))
        self.size_x.setObjectName("size_x")
        self.size_y = QtWidgets.QLineEdit(self.groupBox_2)
        self.size_y.setGeometry(QtCore.QRect(50, 60, 51, 20))
        self.size_y.setObjectName("size_y")
        self.size_z = QtWidgets.QLineEdit(self.groupBox_2)
        self.size_z.setGeometry(QtCore.QRect(50, 90, 51, 20))
        self.size_z.setObjectName("size_z")
        self.sizeX_label = QtWidgets.QLabel(self.groupBox_2)
        self.sizeX_label.setGeometry(QtCore.QRect(20, 30, 21, 20))
        self.sizeX_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sizeX_label.setObjectName("sizeX_label")
        self.sizeY_label = QtWidgets.QLabel(self.groupBox_2)
        self.sizeY_label.setGeometry(QtCore.QRect(20, 60, 21, 16))
        self.sizeY_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sizeY_label.setObjectName("sizeY_label")
        self.sizeZ_label = QtWidgets.QLabel(self.groupBox_2)
        self.sizeZ_label.setGeometry(QtCore.QRect(20, 90, 21, 16))
        self.sizeZ_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sizeZ_label.setObjectName("sizeZ_label")
        # Exhaustiveness
        self.exhaustiveness = QtWidgets.QLineEdit(self.centralwidget)
        self.exhaustiveness.setGeometry(QtCore.QRect(110, 180, 51, 20))
        self.exhaustiveness.setObjectName("exhaustiveness")
        self.exhaustiveness_label = QtWidgets.QLabel(self.centralwidget)
        self.exhaustiveness_label.setGeometry(QtCore.QRect(20, 180, 81, 16))
        self.exhaustiveness_label.setObjectName("exhaustiveness_label")
        # Refresh Receptors and Ligands Button
        self.refresh_lists = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_lists.setGeometry(QtCore.QRect(400, 50, 110, 25))
        self.refresh_lists.setObjectName("refresh_lists")
        self.refresh_lists.setToolTip('Updates both receptor and ligand lists with current inventory.')
        # Go Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 290, 120, 25))
        self.pushButton.setObjectName("pushButton")
        # Populate Previous Data Button
        self.pop_previous = QtWidgets.QPushButton(self.centralwidget)
        self.pop_previous.setGeometry(QtCore.QRect(20, 250, 120, 25))
        self.pop_previous.setObjectName("pop_previous")
        self.pop_previous.setToolTip('Populates above fields with previous configuration data.')
        # Populate Data Verification
        self.popVerify = QtWidgets.QMessageBox(self.centralwidget)
        self.popVerify.setWindowTitle('Populate Previous Data Error')
        self.popVerify.setText('Error with previous configuration file, please manually enter data')
        self.popVerify.setIcon(self.popVerify.Warning)
        # Run all ligands
        self.all_ligands = QtWidgets.QPushButton(self.centralwidget)
        self.all_ligands.setGeometry(QtCore.QRect(400, 260, 100, 25))
        self.all_ligands.setObjectName("all_ligands")
        self.all_ligands.setToolTip('Runs all ligands currently within the ligand directory.')
        # Total Ligand Label
        self.total_ligand_label = QtWidgets.QLabel(self.centralwidget)
        self.total_ligand_label.setGeometry(QtCore.QRect(340, 90, 100, 25))
        self.total_ligand_label.setAlignment(QtCore.Qt.AlignCenter)
        self.total_ligand_label.setObjectName("total_ligand_label")
        # Total Ligand Value
        self.total_ligand_value = QtWidgets.QLabel(self.centralwidget)
        self.total_ligand_value.setGeometry(QtCore.QRect(400, 90, 100, 25))
        self.total_ligand_value.setAlignment(QtCore.Qt.AlignCenter)
        self.total_ligand_value.setObjectName("total_ligand_value")
        # Time Remaining Label
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(340, 110, 100, 25))
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        # Time Remaining Value
        self.time_remaining = QtWidgets.QLabel(self.centralwidget)
        self.time_remaining.setGeometry(QtCore.QRect(400, 110, 100, 25))
        self.time_remaining.setAlignment(QtCore.Qt.AlignCenter)
        self.time_remaining.setObjectName("time_remaining")
        # Cpu Label
        self.cpuLabel = QtWidgets.QLabel(self.centralwidget)
        self.cpuLabel.setGeometry(QtCore.QRect(170, 180, 60, 20))
        self.cpuLabel.setObjectName("cpuLabel")
        # CPU Spin Box
        self.cpuSet = QtWidgets.QSpinBox(self.centralwidget)
        self.cpuSet.setGeometry(QtCore.QRect(230, 180, 50, 20))
        self.cpuSet.setObjectName("cpuSet")
        self.cpuSet.setRange(1, os.cpu_count())
        self.cpuSet.setValue(os.cpu_count())
        self.cpuSet.setToolTip('More CPU threads equals faster runs, but with less multitasking capabilities')
        # Seed Label
        self.seedLabel = QtWidgets.QLabel(self.centralwidget)
        self.seedLabel.setGeometry(QtCore.QRect(20, 210, 50, 20))
        self.seedLabel.setObjectName("seedLabel")
        # Seed Value
        self.seed_value = QtWidgets.QLineEdit(self.centralwidget)
        self.seed_value.setGeometry(QtCore.QRect(70, 210, 70, 20))
        self.seed_value.setObjectName("seed_value")
        self.seed_value.setToolTip('If randomize is left unchecked, place a seed(integer) to be used to run one/all ligand(s) with the same seed.')
        # Seed Checkbox
        self.randomSeed = QtWidgets.QCheckBox(self.centralwidget)
        self.randomSeed.setGeometry(QtCore.QRect(150, 210, 150, 20))
        self.randomSeed.setObjectName("randomSeed")
        self.randomSeed.setText("Randomize Seed")
        self.randomSeed.setToolTip('Randomizes the seed for each ligand docking.')
        # Seed Verification
        self.seedChecker = QtWidgets.QMessageBox(self.centralwidget)
        self.seedChecker.setWindowTitle('Seed Selection Error')
        self.seedChecker.setText('Please indicate either specific seed or random seed')
        self.seedChecker.setIcon(self.seedChecker.Warning)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Call Functions
        runVina.initialize_dir()
        self.pop_receptors()
        self.pop_ligands()

        # Button Actions
        self.refresh_lists.clicked.connect(lambda: self.pop_ligands())
        self.refresh_lists.clicked.connect(lambda: self.pop_receptors())
        self.pop_previous.clicked.connect(lambda: self.pop_previous_data())
        self.randomSeed.stateChanged.connect(lambda: self.clear_seed_value())
        self.pushButton.clicked.connect(lambda: self.run_selected_ligand())
        self.all_ligands.clicked.connect(lambda: self.run_all_ligands())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interactive Vina v0.4"))
        self.receptorListLabel.setText(_translate("MainWindow", "Receptor:"))
        self.ligandListLabel.setText(_translate("MainWindow", "Ligand:"))
        self.groupBox.setTitle(_translate("MainWindow", "Center Position"))
        self.cXlabel.setText(_translate("MainWindow", "X"))
        self.cYlabel.setText(_translate("MainWindow", "Y"))
        self.cZlabel.setText(_translate("MainWindow", "Z"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Selection Box Size"))
        self.sizeX_label.setText(_translate("MainWindow", "X"))
        self.sizeY_label.setText(_translate("MainWindow", "Y"))
        self.sizeZ_label.setText(_translate("MainWindow", "Z"))
        self.exhaustiveness_label.setText(_translate("MainWindow", "Exhaustiveness:"))
        self.refresh_lists.setText(_translate("MainWindow", "Refresh Both Lists"))
        self.pushButton.setText(_translate("MainWindow", "Run Selected Ligand"))
        self.pop_previous.setText(_translate("MainWindow", "Populate Config Data"))
        self.all_ligands.setText(_translate("MainWindow", "Run All Ligands"))
        self.total_ligand_label.setText(_translate("MainWindow", "Total Ligands:"))
        self.total_ligand_value.setText(_translate("MainWindow", ""))
        self.time_label.setText(_translate("MainWindow", "Time Remaining: "))
        self.time_remaining.setText(_translate("MainWindow", "..."))
        self.cpuLabel.setText(_translate("MainWindow", "CPU Cores:"))
        self.seedLabel.setText(_translate("MainWindow", "Set Seed:"))

    # Fills the Ligand List with Ligands within Respective Directory
    def pop_ligands(self):
        self.ligand.clear()
        os.chdir(DATA_HOME)
        os.chdir('Ligands')
        ligand_list = fnmatch.filter(os.listdir(), '*.pdbqt')
        self.ligand.addItems(ligand_list)
        self.total_ligand_value.setText(str(len(ligand_list)))

    # Fills the Receptor List with Receptors within Respective Directory
    def pop_receptors(self):
        self.receptorList.clear()
        os.chdir(DATA_HOME)
        os.chdir('Receptors')
        receptor_list = fnmatch.filter(os.listdir(), '*.pdbqt')
        self.receptorList.addItems(receptor_list)

    def pop_previous_data(self):
        try:
            os.chdir(DATA_HOME)
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
            self.cpuSet.setValue(int(_temp[6:-1]))
        except:
            print('Error with Populate')
            self.popVerify.exec()

    # If User Selects to Use Randomized Seeds, The field associated with a Seed Value is clearer
    def clear_seed_value(self):
        if self.randomSeed.isChecked():
            self.seed_value.clear()

    # If
    def check_entered_seed(self):
        if not (self.randomSeed.isChecked()) and self.seed_value.text() == '':
            print('User needs to specify a seed(int) or select randomize seed')
            self.seedChecker.exec()
            return False
        else:
            return True

    def check_empty_fields(self):
        if '' in [self.center_x.text(), self.center_y.text(), self.center_z.text(), self.size_z.text(),
                  self.size_y.text(), self.size_z.text(), self.exhaustiveness.text()]:
            print('One or more fields is empty Fields')
            self.popVerify.exec()
            return True
        else:
            return False

    def get_vina_conf_dict(self):
        vina_conf = {
            "Receptor": self.receptorList.currentText(),
            "Ligand": '',
            "CenterX": self.center_x.text(),
            "CenterY": self.center_y.text(),
            "CenterZ": self.center_z.text(),
            "SizeX": self.size_x.text(),
            "SizeY": self.size_y.text(),
            "SizeZ": self.size_z.text(),
            "Exhaustiveness": self.exhaustiveness.text(),
            "Seed": self.seed_value.text(),
            "CPU": self.cpuSet.value()
        }
        return vina_conf

    def run_selected_ligand(self):
        if not (self.check_entered_seed()) or self.check_empty_fields():
            return
        else:
            _ligand = self.ligand.currentText()
            vina_conf = self.get_vina_conf_dict()
            vina_conf.update({"Ligand": _ligand})
            runVina.run_selected_ligand(vina_conf)

    def run_all_ligands(self):
        if not (self.check_entered_seed()) or self.check_empty_fields():
            return
        else:
            vina_conf = self.get_vina_conf_dict()
            runVina.run_all_ligands(self, vina_conf)

    def update_time_remaining(self, time_r):
        self.time_remaining.setText(f"{time_r:.3f}")

