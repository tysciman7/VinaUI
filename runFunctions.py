import os
from datetime import datetime, time
import time
import fnmatch
import directoryManager


# Creates Configuration File then runs Vina
def create_conf(vina_conf_dict):
    os.chdir(directoryManager.get_config('data_path'))
    _ligand_path = directoryManager.get_config('ligand_path')
    _receptor_path = directoryManager.get_config('receptor_path')
    _output_path = directoryManager.get_config('output_path')
    _log_path = directoryManager.get_config('log_path')

    receptor, ligand, center_x, center_y, center_z, size_x, size_y, size_z, exhaustiveness, seed, cpu_value = vina_conf_dict.values()

    ligand_name = str(ligand[:-6])
    receptor_name = receptor[:-6]

    current_date_time = str(datetime.now())
    current_date_time = current_date_time.replace(':', '.')
    current_date_time = current_date_time[0:-7]
    log_file_name = ligand_name + '+' + receptor_name + '_' + current_date_time + '_log.txt'
    output_file_name = ligand_name + '+' + receptor_name + '_' + current_date_time + "_output.pdbqt"

    config_file = open("conf.txt", "w")
    config_file.write("receptor = " + _receptor_path + "\\" + receptor + "\n")
    config_file.write("ligand = " + _ligand_path + "\\" + ligand + "\n")
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
    config_file.write("log = " + _log_path + '\\' + log_file_name + "\n")
    config_file.write("out = " + _output_path + '\\' + output_file_name + "\n")
    config_file.close()

    os.chdir(_log_path)
    open(log_file_name, 'w').close()
    os.chdir(_output_path)
    open(output_file_name, 'w').close()

    launch_vina()


# Runs vina
def launch_vina():
    os.chdir(directoryManager.get_config('data_path'))
    _vina_path = directoryManager.get_config('vina_path')
    _vina_path = os.path.normpath(_vina_path)
    _vina_path = "\"" + _vina_path + "\""
    os.system(_vina_path + ' --config conf.txt')


# Runs user selected ligand
def run_selected_ligand(vina_conf_dict):
    create_conf(vina_conf_dict)


# Runs all ligands contained in the ligands directory
def run_all_ligands(ui, vina_conf_dict):
    os.chdir(directoryManager.get_config('ligand_path'))
    ligand_list = fnmatch.filter(os.listdir(), '*.pdbqt')
    ligands_remaining = len(ligand_list)
    for _ligand in ligand_list:
        tic = time.perf_counter()
        vina_conf_dict.update({"Ligand": _ligand})
        create_conf(vina_conf_dict)
        toc = time.perf_counter()
        time_inst = toc - tic
        time_remaining = time_inst * ligands_remaining
        print('Time Remaining: ' + str(time_remaining) + 'seconds')
        ui.update_time_remaining(time_remaining)
        ligands_remaining -= 1



