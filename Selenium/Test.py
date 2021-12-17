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

with open('TelePath.txt', 'w') as file:
    for folder in getAllSubDir(fr'{os.getcwd()}\Tele\Tele'):
        file.write(f'{folder}\n')
    file.close()
#
# from os import listdir
# from os.path import isfile, join

# with open('Note.txt', 'w') as file:
#     for folder in getAllSubDir(fr'{os.getcwd()}\Tele\Tele'):
#         not_contain = True
#         folders = getAllSubDir(folder)
#         print(folders)
#         for foldercheck in folders:
#             if 'tdata' in foldercheck:
#                 print('contain')
#                 not_contain = False
#         if not_contain:
#             file.write(f'{folder}\n')
#     file.close()

#
# with open('Note.txt' , 'r') as noteFile:
#     FolderNotes = noteFile.readlines()
#     with open('TelePath.txt', 'r') as telePathFile:
#         OldTelePaths = telePathFile.readlines()
#         with open('TelePathNew.txt', 'w') as telePathNew:
#             for OldTelePath in OldTelePaths:
#                 if OldTelePath not in FolderNotes:
#                     telePathNew.write(f'{OldTelePath}')


# with open('VPS cập nhật ngày 4.12_New.rdg', 'r') as file:
#     lines = file.readlines()
#     print(lines)
#     lines2 = lines.copy()
#     wantDelete = False
#     for index, line in enumerate(lines):
#         if '<logonCredentials inherit="None">' in line:
#             wantDelete = True
#         if wantDelete:
#             lines2.remove(line)
#         if '</logonCredentials>' in line:
#             wantDelete = False
#     file.close()
#     print(lines2)
#     with open('VPS cập nhật ngày 4.12_New_Fix.rdg', 'w') as file:
#         for line in lines2:
#             file.write(f'{line}')
#             print(f'{line}')
#         file.close()
