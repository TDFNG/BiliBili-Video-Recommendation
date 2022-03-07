from os import makedirs
from os.path import isfile
from shutil import rmtree


def chucun(name):
    try:
        name = str(name)
        path = 'DATA'
        for i in range(len(name)):
            path = path + '\\' + name[i]
        testp = path.replace('DATA', 'TMP', 1)
        makedirs(testp)
        rmtree('TMP')
        try:
            makedirs(path)
        except:
            pass
        with open(path + '\\E', 'w+') as tp:
            pass
        return True
    except:
        rmtree('TMP')
        return False


def chazhao(name):
    name = str(name)
    path = 'DATA'
    for i in range(len(name)):
        path = path + '\\' + name[i]
    return isfile(path + '\\E')
