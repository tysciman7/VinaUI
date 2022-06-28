from datetime import datetime
import os
import fnmatch


def get_current_date_time():
    _current_date_time = str(datetime.now())
    _current_date_time = _current_date_time.replace(':', '.')
    _current_date_time = _current_date_time[0:-7]
    return _current_date_time


def get_log_data(_path, _log_file):
    os.chdir(_path)
    with open(_log_file, 'r') as _file:
        # Skim Through the useless
        for i in range(26):
            _file.readline()

        _raw_data = _file.readline()

        if _raw_data == '':
            return None

    _log_data = {
        'ligand_name': _log_file[:-6],
        'binding_affinity': _raw_data[7:19].replace(" ", ""),
        'dist_from_rmsd_lb': _raw_data[20:30].replace(" ", ""),
        'dist_from_rmsd_ub': _raw_data[31:].replace(" ", "")
    }

    return _log_data


def sort_log_data(_log_path):
    os.chdir(_log_path)
    _log_filename_list = fnmatch.filter(os.listdir(), '*.txt')
    _log_list = []

    for _log_filename in _log_filename_list:
        if _log_filename.__contains__('SORTED'):
            continue
        _log_data = get_log_data(_log_path, _log_filename)
        if _log_data is not None:
            _log_list.append(_log_data)

    _log_list.sort(key=lambda x: float(x['binding_affinity']))

    with open('SORTED LIST ' + str(get_current_date_time()) + '.txt', 'w') as _sorted_file:
        _sorted_file.write('Ligand | Binding Affinity' + '\n')
        for _data in _log_list:
            _sorted_file.write(_data['ligand_name'] + '\t\t' + _data['binding_affinity'] + '\n')

