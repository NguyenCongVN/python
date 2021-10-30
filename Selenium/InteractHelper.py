import pyautogui
import threading
import time
import random
from tkinter import Tk
from subprocess import Popen, PIPE

from python_imagesearch.imagesearch import imagesearch, imagesearchMultiple


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
