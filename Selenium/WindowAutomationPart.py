import time
import time
import traceback
from subprocess import Popen

import pyautogui
from pywinauto import Desktop

from InteractHelper import LayCacTenWindow
from InteractHelper import waitThreadAndJoin, detectImageAndClickCenter, \
    detectImageAndClickLeftTopNew, DoiThoiGian, detectAllImage, clickWithLocation

pyautogui.FAILSAFE = False
cap = 0


# Chọn máy với tên
def chooseComputerWithName(window, tenMay):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        try:
            if str(tenMay) in str(item.texts()):
                print('Đang chọn máy {check}'.format(check=tenMay))
                # Nhấp chuột trái chọn máy
                item.click_input(button='left', coords=(None, None))
        except Exception as err:
            print(err)
            print('Có lỗi xảy ra {err} trong quá trình chọn máy'.format(err=err))


# Mở Remote Destop
def OpenWindow(path, tuKhoa):
    Popen(path, shell=True)
    dlg = None
    # Đợi 5s để cửa sổ mở ra hoàn toàn
    waitThreadAndJoin(5)

    #
    tenCacWindow = LayCacTenWindow()

    for tenWindow in tenCacWindow:
        if tuKhoa in tenWindow:
            print('Thấy cửa sổ khớp {tenWindow}'.format(tenWindow=tenWindow))
            dlg = Desktop(backend="uia")[tenWindow]
            break
    dlg.wait('visible')

    # Trả về cửa sổ sau khi đã mở thành công
    return dlg


# Copy một file từ trong máy
def copyFile(path, fileName):
    import subprocess
    # mở explorer và chọn path
    subprocess.Popen(r'explorer /select,"{path}"'.format(path=path))
    # Đợi 5s để explorer sẵn sàng
    waitThreadAndJoin(5)
    #
    dlg = Desktop(backend="uia")['Google Drive']
    # Để cửa sổ lên đầu
    dlg.minimize()
    dlg.restore()
    # Chọn file trong cửa sổ explore với path đã mở
    file = dlg[fileName]
    file.click_input()
    # Nhấn Ctrl+C
    file.type_keys('^c')


# paste file
def pasteFile(window, tenMay):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(tenMay) in str(item.texts()):
            print('pasting computer {check}'.format(check=tenMay))
            item.click_input(button='left', coords=(None, None))
            try:
                staticPanel = window['Input Capture WindowPane']
                # staticPanel.move_mouse_input(coords=(400, 400))
                staticPanel.double_click_input(button='left', coords=(1500, 500))
                staticPanel.type_keys('^v')
            except:
                pass
            break


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
        # Mở remote
        remoteWindow = OpenWindow(r'C:\Users\chubo\Desktop\RDCMan.exe', 'Remote')



    except Exception as err:
        print('Có lỗi xảy ra')
        print(traceback.print_exc())
