import os
import sys
import fnmatch
import time
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


#Used to make dirs in same folder
#DATA_HOME = os.getcwd()

#Used to make dirs one above
PATH_HOME = os.getcwd()
DATA_HOME = os.path.dirname(PATH_HOME)

LOGS_FILE = DATA_HOME + '\Logs'
OUTPUT_FILE = DATA_HOME + '\Ligand Outputs'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.receptor = QtWidgets.QComboBox(self.centralwidget)
        self.receptor.setGeometry(QtCore.QRect(80, 15, 170, 22))
        self.receptor.setObjectName("receptor")
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
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 21, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 21, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 21, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        # Exhaustiveness
        self.exhaustiveness = QtWidgets.QLineEdit(self.centralwidget)
        self.exhaustiveness.setGeometry(QtCore.QRect(110, 180, 51, 20))
        self.exhaustiveness.setObjectName("exhaustiveness")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 81, 16))
        self.label_9.setObjectName("label_9")
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
        self.initialize_dir()
        self.pop_receptors()
        self.pop_ligands()
        self.refresh_lists.clicked.connect(lambda: self.pop_ligands())
        self.refresh_lists.clicked.connect(lambda: self.pop_receptors())
        self.pop_previous.clicked.connect(lambda: self.pop_previous_data())
        self.pushButton.clicked.connect(lambda: self.run_selected_ligand())
        self.all_ligands.clicked.connect(lambda: self.run_all_ligands())
        self.randomSeed.stateChanged.connect(lambda: self.clear_seed_value())


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
        self.label_6.setText(_translate("MainWindow", "X"))
        self.label_7.setText(_translate("MainWindow", "Y"))
        self.label_8.setText(_translate("MainWindow", "Z"))
        self.label_9.setText(_translate("MainWindow", "Exhaustiveness:"))
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


    def initialize_dir(self):
        os.chdir(DATA_HOME)
        if not os.path.isdir('Ligands'):
            os.mkdir('Ligands')
        if not os.path.isdir('Receptors'):
            os.mkdir('Receptors')
        if not os.path.isdir('Ligand Outputs'):
            os.mkdir('Ligand Outputs')
        if not os.path.isdir('Logs'):
            os.mkdir('Logs')

    # Fills the Receptor List with Receptors within Respective Directory
    def pop_receptors(self):
        self.receptor.clear()
        os.chdir(DATA_HOME)
        os.chdir('Receptors')
        receptor_list = fnmatch.filter(os.listdir(), '*.pdbqt')
        self.receptor.addItems(receptor_list)

    # Fills the Ligand List with Ligands within Respective Directory
    def pop_ligands(self):
        self.ligand.clear()
        os.chdir(DATA_HOME)
        os.chdir('Ligands')
        ligand_list = fnmatch.filter(os.listdir(), '*.pdbqt')
        self.ligand.addItems(ligand_list)
        self.total_ligand_value.setText(str(len(ligand_list)))

    # If User Selects to Use Randomized Seeds, The field associated with a Seed Value is clearer
    def clear_seed_value(self):
        if self.randomSeed.isChecked():
            self.seed_value.clear()

    # If
    def check_entered_seed(self):
        if (not(self.randomSeed.isChecked()) and self.seed_value.text() == ''):
            print('User needs to specify a seed(int) or select randomize seed')
            self.seedChecker.exec()
            return False
        else:
            return True

    def check_empty_fields(self):
        if '' in [self.center_x.text(), self.center_y.text(), self.center_z.text(), self.size_z.text(), self.size_y.text(), self.size_z.text(), self.exhaustiveness.text()]:
            print('One or more fields is empty Fields')
            self.popVerify.exec()
            return True
        else:
            return False


    def update_time(self, time_string):
        self.time_remaining.setText(time_string)

    #Creates Configuration File then runs Vina
    def create_conf(self, ligand):
        os.chdir(DATA_HOME)

        ligandname = str(ligand[:-6])
        receptor = self.receptor.currentText()
        receptor_name = receptor[:-6]
        cpuValue = self.cpuSet.value()
        seed = self.seed_value.text()

        current_date_time = str(datetime.now())
        current_date_time = current_date_time.replace(':', '.')
        current_date_time = current_date_time[0:-7]
        log_file_name = ligandname + '+' + receptor_name + '_' + current_date_time + '_log.txt'
        output_file_name = ligandname + '+' + receptor_name + '_' + current_date_time + "_output.pdbqt"

        config_file = open("conf.txt", "w")
        config_file.write("receptor = " + DATA_HOME + "\Receptors\\" + receptor + "\n")
        config_file.write("ligand = " + DATA_HOME + "\Ligands\\" + ligand + "\n")
        config_file.write("center_x = " + self.center_x.text() + "\n")
        config_file.write("center_y = " + self.center_y.text() + "\n")
        config_file.write("center_z = " + self.center_z.text() + "\n")
        config_file.write("size_x = " + self.size_x.text() + "\n")
        config_file.write("size_y = " + self.size_y.text() + "\n")
        config_file.write("size_z = " + self.size_z.text() + "\n")
        config_file.write("exhaustiveness = " + self.exhaustiveness.text() + "\n")
        config_file.write("cpu = " + str(cpuValue) + "\n")
        if not(self.randomSeed.isChecked()):
            config_file.write("seed = " + seed + '\n')
        config_file.write("log = " + LOGS_FILE + '\\' + log_file_name + "\n")
        config_file.write("out = " + OUTPUT_FILE + '\\' + output_file_name + "\n")
        config_file.close()

        os.chdir(LOGS_FILE)
        open(log_file_name, 'w').close()
        os.chdir(OUTPUT_FILE)
        open(output_file_name, 'w').close()


        self.launch_vina()


    def launch_vina(self):
        #subprocess.call(DATA_HOME + "\\veni_launch.bat")
        os.chdir(DATA_HOME)
        os.system('"C:\\Program Files (x86)\\The Scripps Research Institute\Vina\\vina.exe"' + ' --config conf.txt')

    def run_selected_ligand(self):
        if not(self.check_entered_seed()) or self.check_empty_fields():
            return
        lig = self.ligand.currentText()
        self.create_conf(lig)

    def run_all_ligands(self):
        if not (self.check_entered_seed()) or self.check_empty_fields():
            return
        os.chdir(DATA_HOME)
        os.chdir('Ligands')
        ligand_list = fnmatch.filter(os.listdir(), '*.pdbqt')
        ligands_remaining = len(ligand_list)
        for lig in ligand_list:
            tic = time.perf_counter()
            self.create_conf(lig)
            toc = time.perf_counter()
            time_inst = toc - tic
            #print(f"Test took: {time_inst:.3f} seconds\t")
            #print(f"Time Remaining: {ligands_remaining * time_inst:.3f}")
            self.time_remaining.setText(f"{ligands_remaining * time_inst:.3f}")
            self.time_remaining.update()

    def pop_previous_data(self):
        try:
            os.chdir(DATA_HOME)
            config_file = open("conf.txt", "r")
            config_file.readline()
            config_file.readline()
            tempLine = config_file.readline()
            self.center_x.setText(tempLine[11:-1])
            tempLine = config_file.readline()
            self.center_y.setText(tempLine[11:-1])
            tempLine = config_file.readline()
            self.center_z.setText(tempLine[11:-1])
            tempLine = config_file.readline()
            self.size_x.setText(tempLine[9:-1])
            tempLine = config_file.readline()
            self.size_y.setText(tempLine[9:-1])
            tempLine = config_file.readline()
            self.size_z.setText(tempLine[9:-1])
            tempLine = config_file.readline()
            self.exhaustiveness.setText(tempLine[17:len(tempLine)])
            tempLine = config_file.readline()
            self.cpuSet.setValue(int(tempLine[6:-1]))
        except:
            print('Error with Populate')
            self.popVerify.exec()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
