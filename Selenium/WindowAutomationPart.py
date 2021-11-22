import time
import time
import traceback
from subprocess import Popen

import pyautogui
from pywinauto import Desktop

from InteractHelper import LayCacTenWindow
from InteractHelper import waitThreadAndJoin, detectImageAndClickCenter, \
    detectImageAndClickLeftTopNew, DoiThoiGian, detectAllImage, clickWithLocation
import subprocess

pyautogui.FAILSAFE = False
cap = 0


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
        # Mở remote
        subprocess.Popen(r'explorer /select,"{path}"'.format(path=r'E:\ToolKDPNew\VPS 79\VPS 79'))
        exploreWindow = OpenWindow('VPS')
        exploreWindow.draw_outline()
        # Chọn cửa sổ explore
        # exploreWindow.print_control_identifiers()
        VPS = exploreWindow.child_window(control_type="ListItem")

        # Mở cửa sổ VPS bên trong
        VPS.draw_outline()
        VPS.double_click_input()

        # Tìm Item phone bên trong
        # Mở cửa sổ đầu tiên
        phoneItem = exploreWindow.child_window(control_type="ListItem", found_index=0)

        phone = phoneItem.title
        print(phone)
        phoneItem.draw_outline()
        phoneItem.double_click_input()

        # paste telegram
        exploreWindow.draw_outline()
        # Để cửa sổ lên đầu
        exploreWindow.minimize()
        exploreWindow.restore()
        exploreWindow.type_keys('^v')


    except Exception as err:
        print('Có lỗi xảy ra')
        print(traceback.print_exc())
