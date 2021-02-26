import subprocess
import traceback
from subprocess import Popen
from pywinauto import Desktop
import pyautogui
import pywinauto
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import AutomationWorking
import os
import smtplib
import random
import xlrd
from tkinter import Tk
pyautogui.FAILSAFE = False
cap = 0

def copyStringToClipboard(text):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()  # now it stays on the clipboard after the window is closed
    r.destroy()

def findUserAndPassInCsv(id , csv_path):
    workbook = xlrd.open_workbook(csv_path)
    worksheet = workbook.sheet_by_name('KU')
    return [worksheet.cell(id, 1 ).value , worksheet.cell(id, 4 ).value]
def InitSendMail(userName , passWord):
    count = 0
    while count < 5:
        try:
            s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            s.ehlo()
            s.login(userName, passWord)
            return s
        except:
            count = count + 1
            print('Failed to connection Smtp server time {count}'.format(count=count))
            print(traceback.format_exc())
            continue


def SendMail(ImgFileName , range , fromAd , toAd , smtpServer):
    count = 0
    while count < 5:
        try:
            img_data = open(ImgFileName, 'rb').read()
            msg = MIMEMultipart()
            msg['Subject'] = 'result stop {range}'.format(range=range)
            msg['From'] = fromAd
            msg['To'] = toAd
            text = MIMEText("Result from {range}".format(range=range))
            msg.attach(text)
            image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
            msg.attach(image)
            smtpServer.sendmail(fromAd, toAd , msg.as_string())
            break
        except:
            print('fail to send result email time {count}'.format(count=count))
            print(traceback.format_exc())
            count = count + 1
            continue
def OpenWindow(path):
    Popen(path, shell=True)
    dlg = Desktop(backend="uia")['EAA KUUUUU - Remote Desktop Connection Manager v2.72']
    AutomationWorking.waitThreadAndJoin(5)
    dlg.wait('visible')
    return dlg

def startComputer(window , start , stop , exceptComOut):
    TreeItems = window.TreeItem
    check = start
    while check <= stop:
        if str(check) in exceptComOut:
            temp = check
            print(check)
            check = int(exceptComOut[exceptComOut.index(str(check)) + 1])
            print('see replace with {old} with {new}'.format(old=temp , new=check))
            for item in TreeItems.descendants():
                if str(check) in str(item.texts()):
                    print('starting computer {check}'.format(check=check))
                    item.double_click_input(button='left', coords=(None, None))
                    check = temp
                    print(check)
                    check = check + 1
                    break
        else:
            for item in TreeItems.descendants():
                if str(check) in str(item.texts()):
                    print('starting computer {check}'.format(check=check))
                    item.double_click_input(button='left', coords=(None, None))
                    check = check + 1
                    break
def copyFile(path , fileName):
    import subprocess
    subprocess.Popen(r'explorer /select,"{path}"'.format(path=path))
    AutomationWorking.waitThreadAndJoin(5)
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
            print('pasting computer {check}'.format(check=number))
            item.click_input(button='left', coords=(None, None))
            try:
                staticPanel = window['Input Capture WindowPane']
                # staticPanel.move_mouse_input(coords=(400, 400))
                staticPanel.double_click_input(button='left', coords=(1500, 500))
                staticPanel.type_keys('^v')
            except:
                pass
                # print(traceback.format_exc())
                # if (number - start + 1) == 1:
                #     staticPanel = window.child_window(best_match='Static',found_index=0)
                #     staticPanel.move_mouse_input(coords=(400, 400))
                #     staticPanel.type_keys('^v')
                # else:
                #     if (number - start + 1) == 2:
                #         staticPanel = window.child_window(best_match='Static0' , found_index=0)
                #         staticPanel.move_mouse_input(coords=(400, 400))
                #         staticPanel.type_keys('^v')
                #     else:
                #         staticPanel = window.child_window(best_match='Static{number}'.format(number=(number - start + 1)) , found_index = 0)
                #         staticPanel.move_mouse_input(coords=(400, 400))
                #         staticPanel.type_keys('^v')
            break
def closeOpeningWindow(window , number , start):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            count = 0
            while count < 5:
                print('closing opening window computer {check}'.format(check=number))
                item.click_input(button='left', coords=(None, None))
                try:
                    staticPanel = window['Input Capture WindowPane']
                    # staticPanel.move_mouse_input(coords=(400, 400))
                    staticPanel.double_click_input(button='left', coords=(1200, 700))
                    staticPanel.click_input(button='left', coords=(1200, 700))
                    staticPanel.type_keys('%{F4}')
                    break
                except:
                    # print(traceback.format_exc())
                    startComputer(window , start , start , [])
                    AutomationWorking.waitThreadAndJoin(20)
                    count = count + 1
                    continue
            if count == 5:
                print('close opening window computer {check} fail'.format(check=number))
def openFile(window , number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    AutomationWorking.waitThreadAndJoin(5)
    r = None
    count = 0
    while r is None:
        try:
            if count == 20:
                break
            r = pyautogui.locateOnScreen('testing.png' ,confidence=0.8)
            point = pyautogui.center(r)
            pointx, pointy = point
            pyautogui.doubleClick(pointx, pointy)
        except:
            count = count + 1
            continue

def handleComRange(window, start , stop , windowPath , exceptComOut):
    try:
        startComputer(window, start, stop ,exceptComOut)
    except:
        # print(traceback.format_exc())
        # close app
        p = Popen("KillRDC.bat", shell=True, stdout=subprocess.PIPE)
        p.wait()
        print(p.returncode)
        OpenWindow(windowPath)
        AutomationWorking.waitThreadAndJoin(5)
        startComputer(window, start, stop , exceptComOut)
    AutomationWorking.waitThreadAndJoin(100)
    for i in range(start, stop + 1):
        if str(i) in exceptComOut:
            replaceCom = int(exceptComOut[exceptComOut.index(str(i)) + 1])
            closeOpeningWindow(window, replaceCom , start)
        else:
            closeOpeningWindow(window, i, start)
    AutomationWorking.waitThreadAndJoin(10)
    for i in range(start, stop + 1):
        if str(i) in exceptComOut:
            replaceCom = int(exceptComOut[exceptComOut.index(str(i)) + 1])
            pasteFile(window, replaceCom, start)
        else:
            pasteFile(window, i , start )
    AutomationWorking.waitThreadAndJoin(60)
    for i in range(start, stop + 1):
        if str(i) in exceptComOut:
            replaceCom = int(exceptComOut[exceptComOut.index(str(i)) + 1])
            openFile(window, replaceCom)
        else:
            openFile(window, i )
    AutomationWorking.waitThreadAndJoin(200)
    img = pyautogui.screenshot()
    img.save(r'.\result\result-{start}-{stop}.png'.format(start=start , stop=stop))
    # close app
    p = Popen("KillRDC.bat", shell=True, stdout=subprocess.PIPE)
    p.wait()
    print(p.returncode)
    AutomationWorking.waitThreadAndJoin(5)
    smtpServer = InitSendMail('nguyenconggg1', 'hocngaydi123')
    SendMail(r'.\result\result-{start}-{stop}.png'.format(start=start , stop=stop) ,'{start}-{stop}'.format(start=start,stop=stop) , 'nguyenconggg1@gmail.com'
             , 'chubodoi.2910@gmail.com' , smtpServer)

def detectImageAndClickCenterSingle(imagePath):
    r = None
    count = 0
    while r is None:
        try:
            if count == 5:
                break
            r = pyautogui.locateOnScreen(imagePath, confidence=0.8)
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
                captureScreen(random.randrange(1 , 100 , 1))
                return 1
            r = pyautogui.locateOnScreen(imagePath, confidence=0.8)
            point = pyautogui.center(r)
            pointx, pointy = point
            pyautogui.doubleClick(pointx, pointy)
            return 0
        except:
            count = count + 1
            continue


def openFileCustomised(window , number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    if detectImageAndClickCenter('./ChiHa/codeRun1.jpg') == 1:
        detectImageAndClickCenter('./ChiHa/codeRun.jpg')

def enterCodeAndOke(window , number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    detectImageAndClickCenter('./ChiHa/enterCode1.jpg')
    AutomationWorking.waitThreadAndJoin(2)
    pyautogui.write(str(number), interval=0.25)
    AutomationWorking.waitThreadAndJoin(2)
    detectImageAndClickCenter('./ChiHa/OkeButton.jpg')

def pressOptionFirefox(window , number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    detectImageAndClickCenter('./ChiHa/OptionButton.jpg')

def pressHelpButton(window , number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    detectImageAndClickCenter('./ChiHa/helpButton.jpg')
    detectImageAndClickCenterSingle('./ChiHa/helpButton.jpg')

def pressAboutButton(window , number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    detectImageAndClickCenter('./ChiHa/AboutFireFoxButton.jpg')

def pressCheckUpdateButton(window , number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    detectImageAndClickCenter('./ChiHa/CheckUpdateButton.jpg')
    AutomationWorking.waitThreadAndJoin(5)
    detectImageAndClickCenter('./ChiHa/updateButton.jpg')
    AutomationWorking.waitThreadAndJoin(5)
    pyautogui.click()




def pressEmailPasswordAndLogin(window , number):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(number) in str(item.texts()):
            item.double_click_input(button='left', coords=(None, None))
            break
    [email , password] = findUserAndPassInCsv(number ,r'C:\Users\Admin\Downloads\KDP February 2021.xlsx' )
    detectImageAndClickCenter('./ChiHa/Email.jpg')
    AutomationWorking.waitThreadAndJoin(5)
    copyStringToClipboard(email)
    try:
        staticPanel = window['Input Capture WindowPane']
        # staticPanel.move_mouse_input(coords=(400, 400))
        staticPanel.type_keys('^v')
    except:
        pass
    detectImageAndClickCenter('./ChiHa/Password.jpg')
    AutomationWorking.waitThreadAndJoin(5)
    copyStringToClipboard(password)
    try:
        staticPanel = window['Input Capture WindowPane']
        # staticPanel.move_mouse_input(coords=(400, 400))
        staticPanel.type_keys('^v')
    except:
        pass
    detectImageAndClickCenter('./ChiHa/SignIn.jpg')

def captureScreen(number):
    im1 = pyautogui.screenshot()
    im1.save(r"C:\Users\Admin\Pictures\testingImage-{j}.jpg".format(j = number))
    AutomationWorking.waitThreadAndJoin(1)
def handleComRangeCustomized(window, start , stop , windowPath , exceptComOut , procedure):
    [startCom , close , paste , open , enterCode , HandleFirefox] = procedure
    csvPath = r'C:\Users\Admin\Downloads\KDP February 2021.xlsx'
    AutomationWorking.waitThreadAndJoin(10)
    if startCom == 1:
        try:
            startComputer(window, start, stop ,exceptComOut)
        except:
            # close app
            p = Popen("KillRDC.bat", shell=True, stdout=subprocess.PIPE)
            p.wait()
            print(p.returncode)
            OpenWindow(windowPath)
            AutomationWorking.waitThreadAndJoin(5)
            startComputer(window, start, stop , exceptComOut)
        print('start done')
        AutomationWorking.waitThreadAndJoin(20)
    if close == 1:
        for i in range(start, stop + 1):
            if str(i) in exceptComOut:
                replaceCom = int(exceptComOut[exceptComOut.index(str(i)) + 1])
                closeOpeningWindow(window, replaceCom , start)
            else:
                closeOpeningWindow(window, i, start)
        AutomationWorking.waitThreadAndJoin(10)
    if paste == 1:
        for i in range(start, stop + 1):
            if str(i) in exceptComOut:
                replaceCom = int(exceptComOut[exceptComOut.index(str(i)) + 1])
                pasteFile(window, replaceCom, start)
            else:
                pasteFile(window, i , start )
        AutomationWorking.waitThreadAndJoin(20)
    if open == 1:
        for i in range(start, stop + 1):
            if str(i) in exceptComOut:
                replaceCom = int(exceptComOut[exceptComOut.index(str(i)) + 1])
                openFileCustomised(window, replaceCom)
            else:
                openFileCustomised(window, i )
    if enterCode == 1:
        for i in range(start, stop + 1):
            if str(i) in exceptComOut:
                replaceCom = int(exceptComOut[exceptComOut.index(str(i)) + 1])
                enterCodeAndOke(window, replaceCom)
            else:
                enterCodeAndOke(window, i )
    if HandleFirefox == 1:
        for i in range(start, stop + 1):
            if str(i) in exceptComOut:
                replaceCom = int(exceptComOut[exceptComOut.index(str(i)) + 1])
                pressOptionFirefox(window, replaceCom)
                AutomationWorking.waitThreadAndJoin(10)
                pressHelpButton(window ,replaceCom )
                AutomationWorking.waitThreadAndJoin(5)
                pressAboutButton(window , replaceCom)
                AutomationWorking.waitThreadAndJoin(5)
                pressCheckUpdateButton(window, replaceCom)
            else:
                pressOptionFirefox(window, i)
                AutomationWorking.waitThreadAndJoin(6)
                pressHelpButton(window, i)
                AutomationWorking.waitThreadAndJoin(2)
                pressAboutButton(window, i)
                AutomationWorking.waitThreadAndJoin(2)
                pressCheckUpdateButton(window, i)
    for i in range(start, stop + 1):
        if str(i) in exceptComOut:
            replaceCom = int(exceptComOut[exceptComOut.index(str(i)) + 1])
            pressEmailPasswordAndLogin(window , replaceCom)
        else:
            pressEmailPasswordAndLogin(window , i)
    p = Popen("KillRDC.bat", shell=True, stdout=subprocess.PIPE)
    p.wait()
    print(p.returncode)