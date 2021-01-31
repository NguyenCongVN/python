import traceback
from subprocess import Popen
from pywinauto import Desktop
import pyautogui
import time
pyautogui.FAILSAFE = False
def OpenWindow(path):
    Popen(path, shell=True)
    dlg = Desktop(backend="uia")['EAA KUUUUU - Remote Desktop Connection Manager v2.72']
    time.sleep(5)
    dlg.wait('visible')
    return dlg

def startComputer(window , start , stop):
    TreeItems = window.TreeItem
    check = start
    while check <= stop:
        for item in TreeItems.descendants():
            if str(check) in str(item.texts()):
                item.double_click_input(button='left', coords=(None, None))
                check = check + 1
                break
def copyFile(path , fileName):
    import subprocess
    subprocess.Popen(r'explorer /select,"{path}"'.format(path=path))
    time.sleep(5)
    dlg = Desktop(backend="uia")['Google Drive']
    # put window on top
    dlg.minimize()
    dlg.restore()
    file = dlg[fileName]
    file.click_input()
    file.type_keys('^c')

def pasteFile(window , number , start):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.click_input(button='left', coords=(None, None))
            try:
                staticPanel = window['Input Capture WindowPane']
                staticPanel.move_mouse_input(coords=(400, 400))
                staticPanel.double_click_input(button='left', coords=(None, None))
                staticPanel.type_keys('^v')
            except:
                print(traceback.format_exc())
                if (number - start + 1) == 1:
                    staticPanel = window['Static']
                    staticPanel.move_mouse_input(coords=(400, 400))
                    staticPanel.type_keys('^v')
                else:
                    if (number - start + 1) == 2:
                        staticPanel = window['Static0']
                        staticPanel.move_mouse_input(coords=(400, 400))
                        staticPanel.type_keys('^v')
                    else:
                        staticPanel = window['Static{number}'.format(number=(number - start + 1))]
                        staticPanel.move_mouse_input(coords=(400, 400))
                        staticPanel.type_keys('^v')
            break
def closeOpeningWindow(window , number , start):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.click_input(button='left', coords=(None, None))
            try:
                staticPanel = window['Input Capture WindowPane']
                staticPanel.move_mouse_input(coords=(400, 400))
                staticPanel.double_click_input(button='left', coords=(None, None))
                staticPanel.type_keys('%{F4}')
            except:
                print(traceback.format_exc())
                if (number - start + 1) == 1:
                    staticPanel = window['Static']
                    staticPanel.move_mouse_input(coords=(400, 400))
                    staticPanel.double_click_input(button='left', coords=(None, None))
                    staticPanel.type_keys('%{F4}')
                else:
                    if (number - start + 1) == 2:
                        staticPanel = window['Static0']
                        staticPanel.move_mouse_input(coords=(400, 400))
                        staticPanel.double_click_input(button='left', coords=(None, None))
                        staticPanel.type_keys('%{F4}')
                    else:
                        staticPanel = window['Static{number}'.format(number=(number - start + 1))]
                        staticPanel.move_mouse_input(coords=(400, 400))
                        staticPanel.double_click_input(button='left', coords=(None, None))
                        staticPanel.type_keys('%{F4}')
            break
def openFile(window , number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    time.sleep(5)
    r = None
    while r is None:
        try:
            r = pyautogui.locateOnScreen('testing.png' ,confidence=0.8)
        except:
            continue
    point = pyautogui.center(r)
    pointx, pointy = point
    pyautogui.doubleClick(pointx ,  pointy)

def handleComRange(window, start , stop , windowPath):
    try:
        startComputer(window, start, stop)
    except:
        print(traceback.format_exc())
        OpenWindow(windowPath)
        time.sleep(5)
        startComputer(window, start, stop)
    time.sleep(120)
    for i in range(start, stop + 1):
        closeOpeningWindow(window, i , start)
    time.sleep(20)
    for i in range(start, stop + 1):
        pasteFile(window, i , start)
    time.sleep(110)
    for i in range(start, stop + 1):
        openFile(window, i )
    time.sleep(70)
    img = pyautogui.screenshot()
    img.save(r'.\result\result-{start}-{stop}.png'.format(start=start , stop=stop))
    # close app
    window.Close.click_input()
    window.Dialog.Yes.click_input()