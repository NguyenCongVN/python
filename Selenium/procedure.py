import os
import subprocess
import traceback
from InteractHelper import *
from Interface.Error import TelegramError


def CopyTelegram():
    CurrentDirectory = os.getcwd()
    subprocess.Popen(
        r'explorer /select,"{path}"'.format(
            path=rf'{CurrentDirectory}\Telegram.exe'))
    lastPath = CurrentDirectory.split('\\')[len(CurrentDirectory.split('\\')) - 1]
    print(lastPath)
    exploreWindow = OpenWindow(f'{lastPath}')
    bringToFrontControl(control=exploreWindow)
    drawOutlineControl(control=exploreWindow)
    typeKeyWithControl(control=exploreWindow, key='c')
    close_control(control=exploreWindow)


def MoTelegramIndex(telepath: str):
    while True:
        controlDangMo = []
        time_try = 0
        try:
            if time_try == 3:
                raise Exception(TelegramError.time_num_out)
            CurrentDirectory = os.getcwd()
            # Mở cửa sổ chứa telegram
            print('Mở cửa số chứa telegram')
            subprocess.Popen(
                r'explorer /select,"{path}"'.format(path=fr'{telepath}\tdata'))
            exploreWindow = OpenWindow(telepath.split('\\')[-1])
            controlDangMo.append(exploreWindow)
            # drawOutlineControl(exploreWindow)
            # print('Đưa cửa sổ lên đầu')
            # bringToFrontControl(control=exploreWindow, tuKhoa='Tele')

            # # Nhấn chọn thư mục đầu tiên
            # print('Nhấn chọn thư mục đầu tiên')
            # double_click_input(control=getChildItem(exploreWindow, controlType=ControlType.ListItem, found_index=0))

            # Tìm Item phone bên trong
            # Mở thư mục tương ứng với các acc
            # print('Mở thư mục đối với từng index')
            # phoneItem = getChildItem(exploreWindow, controlType=ControlType.ListItem, found_index=index)
            # phone = getTextOfListItem(control=phoneItem)
            # print(f'Mở thư mục {phone}')
            # drawOutlineControl(control=phoneItem)
            # double_click_input(control=phoneItem)
            # controlDangMo.remove(exploreWindow)

            # paste telegram
            print('Tìm explore với thư mục phone hiện tại')
            # exploreWindow = OpenWindow(tuKhoa=str(phone))
            # controlDangMo.append(exploreWindow)
            # drawOutlineControl(control=exploreWindow)
            # Để cửa sổ lên đầu
            bringToFrontControl(control=exploreWindow)
            typeKeyWithControl(control=exploreWindow, key='v')
            print('Đợi 5s để tiến hanh paste xong')
            time.sleep(5)

            bringToFrontControl(control=exploreWindow, tuKhoa=telepath.split('\\')[-1])

            # Mở app telegram
            print('Mở telegram app')
            telegramAppListItem = getChildItem(control=exploreWindow, controlType=ControlType.ListItem,
                                               title='Telegram.exe')
            double_click_input(control=telegramAppListItem)
            telegramApp = OpenWindow('Telegram')
            controlDangMo.append(telegramApp)
            bringToFrontControl(control=telegramApp, tuKhoa='Tele')

            # Đóng cửa sổ explore
            close_control(control=exploreWindow)
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
        typeKey(control=searchEdit, key='CHUMBI VALLEY AIRDROP')
    except:
        searchEdit = TimSearchEdit(telegramApp=telegramApp)
        typeKey(control=searchEdit, key='CHUMBI VALLEY AIRDROP')
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
    for folder in getAllSubDir(fr'{os.getcwd()}\Tele\Tele'):
        filePath = fr'{folder}\Telegram.exe'
        try:
            XoaFilePath(filePath)
        except:
            pass
