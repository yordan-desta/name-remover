import os

def isFileOrDir(path):
    return os.path.isfile(path) or os.path.isdir(path)


def isDir(path):
    return os.path.isdir(path)


def isFile(path):
    return os.path.isfile(path)
