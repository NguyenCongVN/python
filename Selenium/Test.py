import os


def getAllSubDir(path):
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    return subfolders


def XoaFilePath(path):
    os.remove(path)


for folder in getAllSubDir(fr'{os.getcwd()}\Tele\Tele'):
    filePath = fr'{folder}\Telegram.exe'
    try:
        XoaFilePath(filePath)
    except:
        pass
