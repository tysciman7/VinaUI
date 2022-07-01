import os
from datetime import datetime, time
import time
import fnmatch
import subprocess
import directoryManager
import errorMessageBoxes as showError


# Creates Configuration File then runs Vina
def create_conf(vina_conf_dict):
    receptor, ligand, center_x, center_y, center_z, size_x, size_y, size_z, exhaustiveness, seed, cpu_value = vina_conf_dict.values()

    ligand_name = str(ligand[:-6])
    receptor_name = receptor[:-6]
    log_file_name = ligand_name + '+' + receptor_name + '_' + directoryManager.get_current_date_time() + '_log.txt'
    output_file_name = ligand_name + '+' + receptor_name + '_' + directoryManager.get_current_date_time() + "_output.pdbqt"

    _receptor_path = os.path.join(directoryManager.get_config('receptor_path'), receptor)
    _ligand_path = os.path.join(directoryManager.get_config('ligand_path'), ligand)
    _log_path = os.path.join(directoryManager.get_config('log_path'), log_file_name)
    _output_path = os.path.join(directoryManager.get_config('output_path'), output_file_name)
    _conf_path = os.path.join(directoryManager.get_config('data_path'), 'conf.txt')

    config_file = open(_conf_path, "w")
    config_file.write(f"receptor = {_receptor_path}\n")
    config_file.write(f"ligand = {_ligand_path}\n")
    config_file.write(f"center_x = {center_x}\n")
    config_file.write(f"center_y = {center_y}\n")
    config_file.write(f"center_z = {center_z}\n")
    config_file.write(f"size_x = {size_x}\n")
    config_file.write(f"size_y = {size_y}\n")
    config_file.write(f"size_z = {size_z}\n")
    config_file.write(f"exhaustiveness = {exhaustiveness}\n")
    config_file.write(f"cpu = {cpu_value}\n")
    if not (seed == ''):
        config_file.write(f"seed = {seed}\n")
    config_file.write(f"log = {_log_path}\n")
    config_file.write(f"out = {_output_path}\n")
    config_file.close()

    open(_log_path, 'w').close()
    open(_output_path, 'w').close()

    launch_vina(_conf_path)


# Runs vina
def launch_vina(_conf_path):
    _vina_path = directoryManager.get_config('vina_path')
    subprocess.run([_vina_path, '--config', _conf_path], encoding='utf-8')

    # if run_output > 0:
    #     # Substring this error
    #     showError.vina_error_stder(run_output.stderr)


# Runs user selected ligand
def run_selected_ligand(vina_conf_dict):
    create_conf(vina_conf_dict)


# Runs all ligands contained in the ligands directory
def run_all_ligands(main_ui, vina_conf_dict):
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
        main_ui.update_time_remaining(time_remaining)
        ligands_remaining -= 1



