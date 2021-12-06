import typing

import pyautogui
import threading
import time
import random
from tkinter import Tk
from subprocess import Popen, PIPE
from pywinauto import Desktop
from python_imagesearch.imagesearch import imagesearch, imagesearchMultiple
from ControlType import ControlType
import ctypes
from ctypes import *
from ctypes import wintypes, windll
import os


class waitThread(threading.Thread):
    def __init__(self, timeWait):
        threading.Thread.__init__(self)
        self.timeWait = timeWait

    def run(self):
        time.sleep(self.timeWait)
        # # back to window working


def waitThreadAndJoin(time):
    thread = waitThread(timeWait=time)
    thread.start()
    thread.join()


def captureScreen(number):
    im1 = pyautogui.screenshot()
    im1.save(r"C:\Users\Admin\Pictures\testingImage-{j}.jpg".format(j=number))
    waitThreadAndJoin(1)


def detectImageAndClickCenterSingle(imagePath):
    r = None
    count = 0
    while r is None:
        try:
            if count == 5:
                break
            r = pyautogui.locateOnScreen(imagePath, confidence=0.75)
            point = pyautogui.center(r)
            pointx, pointy = point
            pyautogui.click(pointx, pointy)
        except:
            count = count + 1
            continue


def detectImageAndClickCenter(imagePath):
    r = None
    count = 0
    while r is None:
        try:
            if count == 5:
                captureScreen(random.randrange(1, 100, 1))
                return 1
            r = pyautogui.locateOnScreen(imagePath, confidence=0.6)
            point = pyautogui.center(r)
            pointx, pointy = point
            pyautogui.doubleClick(pointx, pointy)
            return 0
        except:
            print('Chưa tìm thấy ảnh tương ứng ! Thử lại')
            count = count + 1
            continue


def detectImageAndClickLeftTopNew(imagePath, dichX=0, dichY=0, gioiHan=None):
    count = 0
    while True:
        pos = imagesearch(imagePath)
        if pos[0] != -1:
            print("Tìm thấy ở vị trí : ", pos[0], pos[1])
            pyautogui.doubleClick(pos[0] + dichX, pos[1] + dichY)
            return 0
        else:
            print("Không tìm thấy ảnh ! Thử lại sau 2s")
            time.sleep(2)
            if gioiHan is not None:
                if count == gioiHan:
                    return 1
                count = count + 1


def detectImageAndClickLeftTopNewSingle(imagePath, dichX=0, dichY=0, gioiHan=None):
    count = 0
    while True:
        pos = imagesearch(imagePath)
        if pos[0] != -1:
            print("Tìm thấy ở vị trí : ", pos[0], pos[1])
            pyautogui.click(pos[0] + dichX, pos[1] + dichY)
            return 0
        else:
            print("Không tìm thấy ảnh ! Thử lại sau 2s")
            time.sleep(2)
            if gioiHan is not None:
                if count == gioiHan:
                    return 1
                count = count + 1


def detectAllImage(imagePath, gioiHan=None):
    count = 0
    while True:
        locations = imagesearchMultiple(imagePath)
        if len(locations) is not 0:
            for location in locations:
                print("Tìm thấy ở vị trí : ", location[0], location[1])
            return locations
        else:
            print("Không tìm thấy ảnh ! Thử lại sau 2s")
            time.sleep(2)
            if gioiHan is not None:
                if count == gioiHan:
                    return 1
                count = count + 1


def clickWithLocation(location, dichX=0, dichY=0):
    pyautogui.click(location[1] + dichX, location[0] + dichY)
    print(f'Đã Cick {location}')


def detectImage(imagePath, gioiHan=None):
    count = 0
    while True:
        pos = imagesearch(imagePath)
        if pos[0] != -1:
            print("Tìm thấy ở vị trí : ", pos[0], pos[1])
            return 0
        else:
            print("Không tìm thấy ảnh ! Thử lại sau 2s")
            time.sleep(2)
            if gioiHan is not None:
                if count == gioiHan:
                    return 1
                count = count + 1


def detectImageAndClickLeft(imagePath, coord):
    r = None
    count = 0
    while r is None:
        try:
            if count == 5:
                captureScreen(random.randrange(1, 100, 1))
                return 1
            r = pyautogui.locateOnScreen(imagePath, confidence=0.7)
            point = pyautogui.center(r)
            pointx, pointy = point
            pyautogui.doubleClick(pointx + coord, pointy)
            return 0
        except:
            count = count + 1
            continue


# Copy
def copyStringToClipboard(text):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()  # now it stays on the clipboard after the window is closed
    r.destroy()


# In các window đang sử dụng trong máy
def LayCacTenWindow():
    from pywinauto import Desktop
    windows = Desktop(backend="uia").windows()
    return [w.window_text() for w in windows]


# Đóng cửa sổ remote
def DongCuaSoRemote():
    # Đóng cửa sổ remote
    p = Popen("KillRDC.bat", shell=True, stdout=PIPE)
    p.wait()
    print(p.returncode)


#
def DoiThoiGian(soGiay):
    print('Đợi {x}s để remote destop load'.format(x=soGiay))
    time.sleep(5)


def getChildItem(control, title=None, controlType: ControlType = None, found_index=0, depth=None):
    return control.child_window(control_type=controlType.value, found_index=found_index, title=title, depth=depth)


def drawOutlineControl(control, color='green'):
    control.draw_outline(color)


def double_click_input(control):
    control.double_click_input()


def minimize(control):
    control.minimize()


def restoreControl(control):
    control.restore()


def bringToFrontControl(control, tuKhoa=None):
    minimize(control)
    if tuKhoa:
        control = OpenWindow(tuKhoa=tuKhoa)
        restoreControl(control)
    else:
        restoreControl(control)


def typeKeyWithControl(control, key):
    control.type_keys(f'^{key}')


def typeKeyEnter(control):
    control.type_keys('{ENTER}')


def typeKey(control, key):
    control.type_keys(f'{key}')


def getTextOfListItem(control):
    return control.window_text()


def getTextEditControl(control):
    return control.texts()


def print_control_identifiers(control):
    control.print_control_identifiers()


def getTextChildItems(control):
    return control.texts()


def click_input(control):
    control.click_input()


def close_control(control):
    control.close()


def setEditText(EditControl, text):
    EditControl.set_text('')
    EditControl.set_text(text)


# Mở Remote Destop
def OpenWindow(tuKhoa, path=None, moCuaSo=False):
    if moCuaSo:
        Popen(path, shell=True)
    dlg = None
    # Đợi 5s để cửa sổ mở ra hoàn toàn
    waitThreadAndJoin(5)

    #
    tenCacWindow = LayCacTenWindow()
    print(tenCacWindow)

    for tenWindow in tenCacWindow:
        if tuKhoa in tenWindow:
            print('Thấy cửa sổ khớp {tenWindow}'.format(tenWindow=tenWindow))
            dlg = Desktop(backend="uia")[tenWindow]
            break
    dlg.wait('visible')

    # Trả về cửa sổ sau khi đã mở thành công
    return dlg


def GetApplicationFolderPath():
    import os
    return os.getenv('APPDATA')


def GetProgramPath():
    import os
    return os.environ["ProgramFiles(x86)"]


def ChangeProxyWithProxifier(proxy: str, is_auth=True):
    print('Thêm process telegram')
    newValue3 = " <Action type=\"Direct\" />"
    with open('default.ppx', 'r') as defaultFile:
        with open('active.ppx', 'w') as activeFile:
            textAddTelegram = defaultFile.read().replace('{my_setting1}', 'true').replace('{my_setting2}',
                                                                                          'Telegram.exe;').replace(
                '{my_setting3}', newValue3)
            activeFile.write(textAddTelegram)
            activeFile.close()
            defaultFile.close()

    ip, port, username, password = proxy.split(':')
    print('Tiến hành đổi proxy')
    print('Tắt proxifier')
    try:
        os.system("taskkill /f /im Proxifier.exe")
    except:
        pass
    with open('active.ppx', 'r') as activeFile:
        activeText = activeFile.read()
    with open('run.ppx', 'w') as proxifierFile:
        if is_auth:
            runText = activeText.replace('{my_proxy}', ip).replace('{my_port}', port).replace('{is_auth}',
                                                                                              'true').replace(
                '{user_name}', username)
        else:
            runText = activeText.replace('{my_proxy}', ip).replace('{my_port}', port).replace('{is_auth}',
                                                                                              'false').replace(
                '{user_name}', username)
        proxifierFile.write(runText)
        activeFile.close()
        proxifierFile.close()
    print('Xóa file config cũ')
    try:
        os.remove(rf'{GetApplicationFolderPath()}\Proxifier\Profiles\run.ppx')
    except Exception as err:
        print(err)
        pass
    print('Chạy config')
    import subprocess
    subprocess.Popen([rf"{GetProgramPath()}\Proxifier\Proxifier.exe", fr'{os.getcwd()}\run.ppx'])
