import pandas as pd
import os
from Basic.IO import file2obj

GBK = 'gbk'

META_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\'
DATA_ROOT = META_DIR + 'StockData\\'

lib_path = {
    'mapper' : META_DIR + 'field_mapper.csv',
    'formula': META_DIR + 'formula.csv',
    'matched': DATA_ROOT + 'matched.json'}
lib = {}


def get_lib(key):
    global lib
    if key not in lib:
        lib[key] = pd.read_csv(lib_path[key], encoding = GBK)
    return lib[key]


def get_error_path(name):
    return META_DIR + '\\%s.txt' % name


def get_error_list(name):
    path = get_error_path(name)
    return file2obj(path)
