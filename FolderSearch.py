from os import mkdir
from os.path import exists


def chucun(foldername: str, dataname: str):
    try:
        if not exists(foldername):
            mkdir(foldername)
        mkdir(foldername + '\\%s' % dataname)
        return True
    except:
        return False


def chazhao(foldername: str, dataname: str):
    if exists(foldername + '\\%s' % dataname):
        return True
    return False
