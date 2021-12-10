import os


def getAllSubDir(path):
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    return subfolders


def XoaFilePath(path):
    os.remove(path)

#
# for folder in getAllSubDir(fr'{os.getcwd()}\Tele\Tele'):
#     filePath = fr'{folder}\Telegram.exe'
#     try:
#         XoaFilePath(filePath)
#     except:
#         pass

with open('TelePath.txt' , 'w') as file:
    for folder in getAllSubDir(fr'{os.getcwd()}\VPS 79\VPS 79'):
        file.write(f'{folder}\n')
    file.close()