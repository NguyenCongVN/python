import time
import time
import traceback
from subprocess import Popen

import pyautogui

from InteractHelper import LayCacTenWindow
from InteractHelper import waitThreadAndJoin, detectImageAndClickCenter, \
    detectImageAndClickLeftTopNew, DoiThoiGian, detectAllImage, clickWithLocation
import subprocess
from InteractHelper import *
from ControlType import ControlType

pyautogui.FAILSAFE = False
cap = 0


# Copy một file từ trong máy
def copyFile(path, fileName):
    # mở explorer và chọn path
    subprocess.Popen(r'explorer /select,"{path}"'.format(path=path))
    # Đợi 5s để explorer sẵn sàng
    waitThreadAndJoin(5)
    #
    tenCacWindow = LayCacTenWindow()
    print(tenCacWindow)
    dlg = Desktop(backend="uia")['Google Drive']
    # Để cửa sổ lên đầu
    dlg.minimize()
    dlg.restore()
    # Chọn file trong cửa sổ explore với path đã mở
    file = dlg[fileName]
    file.click_input()
    # Nhấn Ctrl+C
    file.type_keys('^c')


# Mở file
def openFile(window, number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    waitThreadAndJoin(5)
    r = None
    count = 0
    while r is None:
        try:
            if count == 20:
                break
            r = pyautogui.locateOnScreen('testing.png', confidence=0.8)
            point = pyautogui.center(r)
            pointx, pointy = point
            pyautogui.doubleClick(pointx, pointy)
        except:
            count = count + 1
            continue


def openFileCustomised(window, number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    if detectImageAndClickCenter('./ChiHa/codeRun1.jpg') == 1:
        detectImageAndClickCenter('./ChiHa/codeRun.jpg')


if __name__ == "__main__":
    try:
        # # Mở telegram.exe
        # subprocess.Popen(
        #     r'explorer /select,"{path}"'.format(path=r'E:\ToolKDPNew\VPS 79\VPS 79\2-79 +84817725987\Telegram (1).exe'))
        # exploreWindow = OpenWindow(r'2-79 +84817725987')
        # bringToFrontControl(control=exploreWindow)
        # drawOutlineControl(control=exploreWindow)
        # typeKeyWithControl(control=exploreWindow, key='c')
        # close_control(control=exploreWindow)
        #
        # # Mở
        # subprocess.Popen(r'explorer /select,"{path}"'.format(path=r'E:\ToolKDPNew\VPS 79\VPS 79'))
        # exploreWindow = OpenWindow('VPS')
        # drawOutlineControl(exploreWindow)
        # # Chọn cửa sổ explore
        # # exploreWindow.print_control_identifiers()
        # VPS = getChildItem(exploreWindow, controlType=ControlType.ListItem)
        #
        # # Mở cửa sổ VPS bên trong
        # VPS.draw_outline()
        # VPS.double_click_input()
        #
        # # Tìm Item phone bên trong
        # # Mở cửa sổ đầu tiên
        # phoneItem = getChildItem(exploreWindow, controlType=ControlType.ListItem, found_index=0)
        # print_control_identifiers(control=phoneItem)
        # phone = getTextOfListItem(control=phoneItem)
        # print(phone)
        # drawOutlineControl(control=phoneItem)
        # double_click_input(control=phoneItem)
        #
        # # paste telegram
        # exploreWindow = OpenWindow(tuKhoa=str(phone))
        # drawOutlineControl(control=exploreWindow)
        # # Để cửa sổ lên đầu
        # bringToFrontControl(control=exploreWindow)
        # typeKeyWithControl(control=exploreWindow, key='v')
        # time.sleep(5)
        #
        # # Mở app telegram
        # telegramAppListItem = getChildItem(control=exploreWindow, controlType=ControlType.ListItem,
        #                                    title='Telegram (1).exe')
        # double_click_input(control=telegramAppListItem)
        # telegramApp = OpenWindow('Telegram')
        # bringToFrontControl(control=telegramApp, tuKhoa='Tele')
        #
        # # Đóng cửa sổ explore
        # close_control(control=exploreWindow)
        # # Điền link vào search
        # searchEdit = None
        # while searchEdit is None:
        #     searchEdit = getChildItem(control=telegramApp, controlType=ControlType.Edit)
        #     print(searchEdit)
        # drawOutlineControl(control=searchEdit, color='red')
        # typeKey(control=searchEdit, key='https://t.me/CHUMBIVALLEY_Bot?start=r02789726500')
        # typeKeyEnter(control=searchEdit)
        # typeKeyEnter(control=searchEdit)
        # # print_control_identifiers(control=telegramApp)
        telegramApp = OpenWindow('Telegram')
        bringToFrontControl(control=telegramApp, tuKhoa='Tele')

        # Nhấn start
        # StartElemt = telegramApp.GroupBox18
        # click_input(StartElemt)

        # # GroupLeft
        # GroupLeft = getControlChildArrayDepth(control=telegramApp, arr=[5, 0, 0, 0])
        # print_control_identifiers(GroupLeft)
        # drawOutlineControl(control=GroupLeft, color='red')
        #
        # time.sleep(10)

        # GroupRight
        GroupRight = getControlChildArrayDepth(control=telegramApp, arr=[5, 0, 0, 1])
        print_control_identifiers(GroupRight)
        drawOutlineControl(control=GroupRight, color='green')

        time.sleep(1000)

        # Vào Group và join
        searchEdit = None
        while searchEdit is None:
            searchEdit = getChildItem(control=GroupLeft, controlType=ControlType.Edit)
            print(searchEdit)
        print_control_identifiers(searchEdit)
        drawOutlineControl(control=searchEdit, color='red')
        typeKey(control=searchEdit, key='@chumbivalley02')
        JoinGroupButton = telegramApp.GroupBox18
        click_input(JoinGroupButton)

        time.sleep(5)

        detectImageAndClickLeftTopNewSingle(imagePath='Image\\CheckButton.png')

        # print_control_identifiers(control=StartElemt)

        # Nhấn chọn bot


    except Exception as err:
        print('Có lỗi xảy ra')
        print(traceback.print_exc())
