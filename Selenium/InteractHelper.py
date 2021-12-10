import traceback
import typing

import pyautogui
import threading
import time
import random
from tkinter import Tk
from subprocess import Popen, PIPE
from pywinauto import Desktop
from python_imagesearch.imagesearch import imagesearch  # , imagesearchMultiple
from ControlType import ControlType
import os
import undetected_chromedriver.v2 as uc
import requests
from requests.auth import HTTPProxyAuth
from selenium.webdriver.chrome.webdriver import WebDriver


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
    currentDir = os.getcwd()
    im1 = pyautogui.screenshot()
    im1.save(rf"{currentDir}\result\result-{number}.jpg")
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


def detectImageAndClickLeftTopNewSingle(imagePath, dichX=0, dichY=0, gioiHan=5):
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


# def detectAllImage(imagePath, gioiHan=None):
#     count = 0
#     while True:
#         locations = imagesearchMultiple(imagePath)
#         if len(locations) is not 0:
#             for location in locations:
#                 print("Tìm thấy ở vị trí : ", location[0], location[1])
#             return locations
#         else:
#             print("Không tìm thấy ảnh ! Thử lại sau 2s")
#             time.sleep(2)
#             if gioiHan is not None:
#                 if count == gioiHan:
#                     return 1
#                 count = count + 1


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


def typeKey(control, key: str):
    key = key.replace(' ', '{VK_SPACE}')
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


def deleteContentFolder(folderPath):
    import os, shutil
    folder = folderPath
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def open_driver(chromePath: str, chrome_folder_path: str, driverPath: str, try_time=5, proxy: str = None,
                type_proxy: int = None,
                anti_captcha=None):
    count = 0
    while count < try_time:
        try:
            options = uc.ChromeOptions()
            options.binary_location = chromePath
            # you may need some other options
            # options.add_argument("start-maximized")
            # options.add_experimental_option("excludeSwitches", ["enable-automation"])
            # options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("--remote-debugging-port=9222")
            # options.add_argument('--no-sandbox')
            options.add_argument('--no-default-browser-check')
            options.add_argument('--no-first-run')
            options.add_argument('--disable-default-apps')
            option_str = [
                #               "--disable-3d-apis",
                #               "--disable-background-networking",
                #               "--disable-bundled-ppapi-flash",
                #               "--disable-client-side-phishing-detection",
                #               "--disable-default-apps",
                #               "--disable-hang-monitor",
                #               "--disable-prompt-on-repost",
                #               # "--disable-sync",
                #               # "--disable-webgl", error khi dùng vps
                #               # "--enable-blink-features=ShadowDOMV0",
                #               # "--enable-logging",
                #               "--disable-notifications",
                #               # "--no-sandbox",
                #               # error connect ??
                #               # "--disable-gpu",
                #               # "--disable-dev-shm-usage",
                #               "--disable-web-security",
                #               "--disable-rtc-smoothness-algorithm",
                #               "--disable-webrtc-hw-decoding",
                #               "--disable-webrtc-hw-encoding",
                #               "--disable-webrtc-multiple-routes",
                #               "--disable-webrtc-hw-vp8-encoding",
                #               # error connect chrome
                #               # "--enforce-webrtc-ip-permission-check",
                #               # "--force-webrtc-ip-handling-policy",
                #               # "--ignore-certificate-errors",
                #               # "--disable-infobars",
                #               # "--disable-blink-features=\"BlockCredentialedSubresources\"",
                "--disable-popup-blocking",
                #               "--disable-blink-features=AutomationControlled",
                #               "--credentials_enable_service=False"
            ]
            for option in option_str:
                options.add_argument(option)

            # # Thêm anti capcha
            # if anti_captcha:
            #     print('Thêm anti captcha')
            #
            #     # Xóa plugin
            #     # print('Xóa plugin')
            #     # deleteContentFolderAndFolder('plugin')
            #     # print('Xóa chrome plugin')
            #     # deleteContentFolderAndFolder(f'{chrome_folder_path}\\App\\Chrome-bin\\88.0.4324.104\\plugin')
            #
            #     with zipfile.ZipFile('.\\extension\\anticaptcha-plugin_v0.60.zip', "r") as f:
            #         f.extractall("plugin")
            #
            #     # Config api key
            #     from pathlib import Path
            #
            #     # set API key in configuration file
            #     api_key = anti_captcha
            #     file = Path('.\\plugin\\js\\config_ac_api_key.js')
            #     file.write_text(file.read_text().replace("antiCapthaPredefinedApiKey = ''",
            #                                              "antiCapthaPredefinedApiKey = '{}'".format(api_key)))
            #
            #     # zip plugin directory back to plugin.zip
            #     zip_file = zipfile.ZipFile('.\\plugin.zip', 'w', zipfile.ZIP_DEFLATED)
            #     for root, dirs, files in os.walk(".\\plugin"):
            #         for file in files:
            #             path = os.path.join(root, file)
            #             zip_file.write(path, arcname=path.replace(".\\plugin\\", ""))
            #     zip_file.close()
            #
            #     # options.add_extension('.\\plugin.zip')
            #
            #     # Copy folder to Chrome
            #     from distutils.dir_util import copy_tree
            #     copy_tree(".\\plugin", f"{chrome_folder_path}\\App\\Chrome-bin\\88.0.4324.104\\plugin")
            #     options.add_argument('--load-extension=.\\plugin')
            if proxy:
                lenProxy = len(proxy.split(':'))
                if lenProxy == 2:
                    if type_proxy == 0:
                        options.add_argument(f'--proxy-server= {proxy}')
                    else:
                        options.add_argument(f'--proxy-server= socks5://{proxy}')
                if lenProxy == 4:
                    if type_proxy == 0:
                        options.add_argument(f"--proxy-server= {proxy.split(':')[0]}:{proxy.split(':')[1]}")
                        options.add_argument(f'--load-extension={os.getcwd()}\\extension\\proxy1')
                    else:
                        options.add_argument(f"--proxy-server= socks5://{proxy.split(':')[0]}:{proxy.split(':')[1]}")
                        options.add_argument(f'--load-extension={os.getcwd()}\\extension\\proxy1')

            # from fake_useragent import UserAgent
            # from selenium_stealth import stealth
            # driver = webdriver.Chrome(executable_path=driverPath, options=options)
            # ua = UserAgent()
            # stealth(driver, user_agent=ua.random,
            #         languages=["en-US", "en"],
            #         vendor="Google Inc.",
            #         platform="Win32",
            #         webgl_vendor="Intel Inc.",
            #         renderer="Intel Iris OpenGL Engine",
            #         fix_hairline=True,
            #         )
            print('Trước khi tạo')
            driver = uc.Chrome(options=options, executable_path=driverPath, log_level=1)
            # driver = uc.Chrome(options=options, version_main=96)
            print('Sau khi tạo')
            driver.maximize_window()
            # driver = uc.Chrome(options=options)

            # Kiểm tra ip của chrome
            driver.execute_script(f"document.title=\"proxyauth={proxy}\"")
            driver.get('https://api.myip.com/')
            time.sleep(1)
            pageSource = driver.page_source
            print(pageSource)
            if "ip" not in pageSource:
                print('Lỗi IP! Thử lại')
                continue
            print('Thành Công')
            return driver
        except Exception as err:
            print(err)
            traceback.print_exc()
            count = count + 1
            print('Lỗi mở driver! Thử lại')
            # Đóng hết telegram
            try:
                print('Đóng hết chrome')
                os.system("taskkill /f /im chrome.exe")
                quitAllDriver(driver=driver)
            except:
                pass
            if count == try_time:
                return 1


def quitAllDriver(driver: WebDriver):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        driver.close()
    driver.quit()


def CheckProxy(proxy: str, typeProxy: int, auth=True):
    try:
        text = ""
        proxy_props = proxy.split(':')
        proxyDict = {
            "http": proxy,
            "https": proxy,
        }
        if typeProxy == 0 and proxy != "":
            baseUrl = 'https://api64.ipify.org'
            if auth:
                if len(proxy_props) > 2:
                    proxies = {'https': f'http://{proxy_props[2]}:{proxy_props[3]}@{proxy_props[0]}:{proxy_props[1]}',
                               'http': f'https://{proxy_props[2]}:{proxy_props[3]}@{proxy_props[0]}:{proxy_props[1]}'}
                    auth = HTTPProxyAuth(proxy_props[2], proxy_props[3])
                    r = requests.get(baseUrl, proxies=proxies, timeout=5, auth=auth)
                else:
                    return ""
            else:
                r = requests.get(baseUrl, proxies=proxyDict, timeout=5)
            text = r.text
            print(text)
            if len(text.split('.')) != 4 and len(text.split('.')) != 8:
                text = ""
    except Exception as err:
        print(err)
        text = ""
    return text


def CheckConnectionToProxy(proxy: str, num_check: int):
    proxy_running = False
    for i in range(num_check):
        print('Đang kiểm tra proxy')
        if CheckProxy(proxy, 0) != "":
            print('Proxy hoạt động')
            proxy_running = True
            break
        else:
            print('Proxy không hoạt động')
            time.sleep(5)
    if proxy_running:
        return proxy
    else:
        return False


def clickUntilDisapper(imagePath, gioiHan=2):
    count = 0
    is_clicked = False
    while count < gioiHan:
        if detectImageAndClickLeftTopNewSingle(imagePath=imagePath, gioiHan=2) == 0:
            is_clicked = True
        count = count + 1
        time.sleep(5)
    print('Dừng nhấn')
    return is_clicked


def getAllSubDir(path):
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    return subfolders
