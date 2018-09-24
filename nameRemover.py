import os

olf = "/home/ydesta/renamerTest"
key = "rena"


class const():
    def LEFT(self):
        return 0

    def RIGHT(self):
        return 1

    def EXACT(self):
        return 2


CONST = const()


def removeNameFromFile(filePath, key, const):

    if not os.path.isfile(filePath):
        return

    baseName = os.path.basename(filePath)

    path = str.split(filePath, baseName)[0]

    extentionArray = baseName.split(".")

    extention = ""

    if len(extentionArray) > 1:
        extention = extentionArray[len(extentionArray) - 1]

    if const == CONST.LEFT():

        name = str.split(baseName, key)[0]

        if not name.strip() or name == baseName:
            return

        newName = name + extention

        os.rename(filePath, path + newName)

        return

    if const == CONST.RIGHT():

        name = str.split(baseName, key)[-1]

        if not name.strip() or name == baseName:
            return

        newName = name + extention

        os.rename(filePath, path + newName)

        return

    if (const == CONST.EXACT()):

        names = str.split(baseName, key)

        name = ""

        for n in names:
            name += n + " "

        if not name.strip() or name == baseName:
            return

        newName = name + extention

        os.rename(filePath, path + newName)


def removeFileFromDir(dirPath, key, const):
    if not os.path.isdir(dirPath):
        return

    for file in os.listdir(dirPath):

        if not dirPath.endswith("/"):
            dirPath += "/"

        file = dirPath + file

        removeNameFromFile(file, key, const)

