import os
import shutil
import subprocess
import traceback
from InteractHelper import *
from Interface.Error import TelegramError


def CopyTelegram(telepath):
    CurrentDirectory = os.getcwd()
    from shutil import copyfile
    copyfile(rf'{CurrentDirectory}\Telegram.exe', telepath)


def MoTelegramIndex(telepath: str):
    while True:
        controlDangMo = []
        time_try = 0
        try:
            if time_try == 3:
                raise Exception(TelegramError.time_num_out)
            # Mở app telegram
            print('Mở telegram app')
            subprocess.Popen(telepath)
            telegramApp = OpenWindow('Telegram')
            controlDangMo.append(telegramApp)
            bringToFrontControl(control=telegramApp, tuKhoa='Tele')
            # Đóng cửa sổ explore
            return telegramApp
        except Exception as err:
            traceback.print_exc()
            if err.args[0] in [TelegramError.time_num_out]:
                raise err
            print('Có lỗi xảy ra! Đóng các control đang mở và thử lại')
            time_try = time_try + 1
            for control in controlDangMo:
                close_control(control=control)
            continue


def TimSearchEdit(telegramApp):
    # Điền link vào search
    print('Tìm search edit')
    searchEdit = None
    while searchEdit is None:
        try:
            searchEdit = getChildItem(control=telegramApp, controlType=ControlType.Edit, found_index=1)
            drawOutlineControl(control=searchEdit, color='red')
        except:
            searchEdit = getChildItem(control=telegramApp, controlType=ControlType.Edit, found_index=0)
            drawOutlineControl(control=searchEdit, color='red')
    return searchEdit


def TimChatEdit(telegramApp):
    print('Tìm chat edit')
    chatEdit = None
    while chatEdit is None:
        try:
            searchEdit = getChildItem(control=telegramApp, controlType=ControlType.Edit, found_index=1)
            drawOutlineControl(control=searchEdit, color='red')

            chatEdit = getChildItem(control=telegramApp, controlType=ControlType.Edit, found_index=0)
            drawOutlineControl(control=chatEdit, color='red')
        except:
            return -1
    return chatEdit


def QuayVeBot(telegramApp):
    # Quay trở lại tìm nhấn bot
    searchEdit = TimSearchEdit(telegramApp=telegramApp)
    # Điền vào bot
    try:
        searchEdit.set_text('')
    except:
        searchEdit = TimSearchEdit(telegramApp=telegramApp)
        searchEdit.set_text('')
    try:
        typeKey(control=searchEdit, key='Chumbi Valley Airdrop (New Round)')
    except:
        searchEdit = TimSearchEdit(telegramApp=telegramApp)
        typeKey(control=searchEdit, key='Chumbi Valley Airdrop (New Round)')
    time.sleep(7)
    try:
        typeKeyEnter(control=searchEdit)
    except:
        searchEdit = TimSearchEdit(telegramApp=telegramApp)
        typeKeyEnter(control=searchEdit)


def TimVaVaoTelegramVoiTuKhoa(telegramApp, tuKhoa=''):
    searchEdit = TimSearchEdit(telegramApp=telegramApp)
    typeKey(control=searchEdit, key=tuKhoa)
    time.sleep(10)
    searchEdit = TimSearchEdit(telegramApp=telegramApp)
    typeKeyEnter(control=searchEdit)


def DienVaoChatEditVaNhanEnter(telegramApp, keys=''):
    ChatEdit = TimChatEdit(telegramApp=telegramApp)
    typeKey(control=ChatEdit, key=keys)
    ChatEdit = TimChatEdit(telegramApp=telegramApp)
    typeKeyEnter(control=ChatEdit)


def XoaFilePath(path):
    os.remove(path)


def XoaHetTeleExe():
    for folder in getAllSubDir(fr'{os.getcwd()}\VPS 79\VPS 79'):
        filePath = fr'{folder}\Telegram.exe'
        try:
            XoaFilePath(filePath)
        except:
            pass


def XoaFolder(path):
    shutil.rmtree(path, ignore_errors=True)
