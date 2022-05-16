import os
from datetime import datetime, time
import fnmatch

# Used to make dirs in same folder
# DATA_HOME = os.getcwd()

# NOTE make these variables more global / editable in separate file
# Used to make dirs one above
PATH_HOME = os.getcwd()
DATA_HOME = os.path.dirname(PATH_HOME)
LOGS_FILE = DATA_HOME + '\Logs'
OUTPUT_FILE = DATA_HOME + '\Ligand Outputs'


def initialize_dir():
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
# NOTE: This Function should probably remain in UI
# def pop_receptors():
#     self.receptor.clear()
#     os.chdir(DATA_HOME)
#     os.chdir('Receptors')
#     receptor_list = fnmatch.filter(os.listdir(), '*.pdbqt')
#     self.receptor.addItems(receptor_list)


# Fills the Ligand List with Ligands within Respective Directory
# NOTE: This Function should probably remain in UI
# def pop_ligands():
#     self.ligand.clear()
#     os.chdir(DATA_HOME)
#     os.chdir('Ligands')
#     ligand_list = fnmatch.filter(os.listdir(), '*.pdbqt')
#     self.ligand.addItems(ligand_list)
#     self.total_ligand_value.setText(str(len(ligand_list)))


# If User Selects to Use Randomized Seeds, The field associated with a Seed Value is clearer
# NOTE: This Function should probably remain in UI
# def clear_seed_value(self):
#     if self.randomSeed.isChecked():
#         self.seed_value.clear()


# If
# NOTE: This Function should probably remain in UI
# def check_entered_seed(self):
#     if not (self.randomSeed.isChecked()) and self.seed_value.text() == '':
#         print('User needs to specify a seed(int) or select randomize seed')
#         self.seedChecker.exec()
#         return False
#     else:
#         return True


# NOTE: This Function should probably remain in UI
# def check_empty_fields(self):
#     if '' in [self.center_x.text(), self.center_y.text(), self.center_z.text(), self.size_z.text(), self.size_y.text(),
#               self.size_z.text(), self.exhaustiveness.text()]:
#         print('One or more fields is empty Fields')
#         self.popVerify.exec()
#         return True
#     else:
#         return False


def update_time(self, time_string):
    self.time_remaining.setText(time_string)


# Creates Configuration File then runs Vina


def create_conf(vina_conf_dict):
    os.chdir(DATA_HOME)

    receptor, ligand, center_x, center_y, center_z, size_x, size_y, size_z, exhaustiveness, seed, cpu_value = vina_conf_dict.values()

    ligand = str(ligand[:-6])
    receptor = receptor[:-6]

    current_date_time = str(datetime.now())
    current_date_time = current_date_time.replace(':', '.')
    current_date_time = current_date_time[0:-7]
    log_file_name = ligand + '+' + receptor + '_' + current_date_time + '_log.txt'
    output_file_name = ligand + '+' + receptor + '_' + current_date_time + "_output.pdbqt"

    config_file = open("conf.txt", "w")
    config_file.write("receptor = " + DATA_HOME + "\Receptors\\" + receptor + "\n")
    config_file.write("ligand = " + DATA_HOME + "\Ligands\\" + ligand + "\n")
    config_file.write("center_x = " + center_x + "\n")
    config_file.write("center_y = " + center_y + "\n")
    config_file.write("center_z = " + center_z + "\n")
    config_file.write("size_x = " + size_x + "\n")
    config_file.write("size_y = " + size_y + "\n")
    config_file.write("size_z = " + size_z + "\n")
    config_file.write("exhaustiveness = " + exhaustiveness + "\n")
    config_file.write("cpu = " + str(cpu_value) + "\n")
    if not (seed == ''):
        config_file.write("seed = " + seed + '\n')
    config_file.write("log = " + LOGS_FILE + '\\' + log_file_name + "\n")
    config_file.write("out = " + OUTPUT_FILE + '\\' + output_file_name + "\n")
    config_file.close()

    os.chdir(LOGS_FILE)
    open(log_file_name, 'w').close()
    os.chdir(OUTPUT_FILE)
    open(output_file_name, 'w').close()

    launch_vina()


def launch_vina():
    # subprocess.call(DATA_HOME + "\\veni_launch.bat")
    os.chdir(DATA_HOME)
    os.system('"C:\\Program Files (x86)\\The Scripps Research Institute\Vina\\vina.exe"' + ' --config conf.txt')


def run_selected_ligand(vina_conf_dict):
    create_conf(vina_conf_dict)


def run_all_ligands(vina_conf_dict):
    os.chdir(DATA_HOME)
    os.chdir('Ligands')
    ligand_list = fnmatch.filter(os.listdir(), '*.pdbqt')
    ligands_remaining = len(ligand_list)
    for _ligand in ligand_list:
        tic = time.perf_counter()
        vina_conf_dict.update({"Ligand": _ligand})
        create_conf(vina_conf_dict)
        toc = time.perf_counter()
        time_inst = toc - tic
        time_remaining = time_inst * ligands_remaining
        # print(time_remaining)

        # self.time_remaining.setText(f"{ligands_remaining * time_inst:.3f}")
        # self.time_remaining.update()

# NOTE: This Function should probably remain in UI
# def pop_previous_data(self):
#     try:
#         os.chdir(DATA_HOME)
#         config_file = open("conf.txt", "r")
#         config_file.readline()
#         config_file.readline()
#         tempLine = config_file.readline()
#         self.center_x.setText(tempLine[11:-1])
#         tempLine = config_file.readline()
#         self.center_y.setText(tempLine[11:-1])
#         tempLine = config_file.readline()
#         self.center_z.setText(tempLine[11:-1])
#         tempLine = config_file.readline()
#         self.size_x.setText(tempLine[9:-1])
#         tempLine = config_file.readline()
#         self.size_y.setText(tempLine[9:-1])
#         tempLine = config_file.readline()
#         self.size_z.setText(tempLine[9:-1])
#         tempLine = config_file.readline()
#         self.exhaustiveness.setText(tempLine[17:len(tempLine)])
#         tempLine = config_file.readline()
#         self.cpuSet.setValue(int(tempLine[6:-1]))
#     except:
#         print('Error with Populate')
#         self.popVerify.exec()
