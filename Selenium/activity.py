import random
import threading
import time
import traceback
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver.v2 as uc
import os
import zipfile


def clickHandlerException(driver, buttonElement, handle_NoInteractAble_with_js=False):
    try:
        buttonElement.click()
    except ElementClickInterceptedException as error:
        print(error)
        print('ElementClickInterceptedException => xử lý với js')
        clickWithJs(driver, buttonElement)
    except ElementNotInteractableException as error:
        print(error)
        if handle_NoInteractAble_with_js:
            print('ElementNotInteractableException => xử lý với js')
            time.sleep(1000)
            clickWithJs(driver, buttonElement)
        else:
            raise error


class waitThread(threading.Thread):
    def __init__(self, timeWait):
        threading.Thread.__init__(self)
        self.timeWait = timeWait

    def run(self):
        time.sleep(self.timeWait)
        # # back to window working


def waitThreadAndJoin(time_wait):
    thread = waitThread(timeWait=time_wait)
    thread.start()
    thread.join()


def clickWithJs(driver, buttonElement):
    driver.execute_script("arguments[0].click();", buttonElement)


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

            # Thêm anti capcha
            if anti_captcha:
                print('Thêm anti captcha')

                # Xóa plugin
                # print('Xóa plugin')
                # deleteContentFolderAndFolder('plugin')
                # print('Xóa chrome plugin')
                # deleteContentFolderAndFolder(f'{chrome_folder_path}\\App\\Chrome-bin\\88.0.4324.104\\plugin')

                with zipfile.ZipFile('.\\extension\\anticaptcha-plugin_v0.60.zip', "r") as f:
                    f.extractall("plugin")

                # Config api key
                from pathlib import Path

                # set API key in configuration file
                api_key = anti_captcha
                file = Path('.\\plugin\\js\\config_ac_api_key.js')
                file.write_text(file.read_text().replace("antiCapthaPredefinedApiKey = ''",
                                                         "antiCapthaPredefinedApiKey = '{}'".format(api_key)))

                # zip plugin directory back to plugin.zip
                zip_file = zipfile.ZipFile('.\\plugin.zip', 'w', zipfile.ZIP_DEFLATED)
                for root, dirs, files in os.walk(".\\plugin"):
                    for file in files:
                        path = os.path.join(root, file)
                        zip_file.write(path, arcname=path.replace(".\\plugin\\", ""))
                zip_file.close()

                # options.add_extension('.\\plugin.zip')

                # Copy folder to Chrome
                from distutils.dir_util import copy_tree
                copy_tree(".\\plugin", f"{chrome_folder_path}\\App\\Chrome-bin\\88.0.4324.104\\plugin")
                options.add_argument('--load-extension=.\\plugin')
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
                        if anti_captcha:
                            options.add_argument(f'--load-extension={os.getcwd()}\\extension\\proxy1,.\\plugin')
                        else:
                            options.add_argument(
                                '--load-extension=E:\\ToolKDPNew\\Selenium\\extension\\proxy1')
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
            if count == try_time:
                return 1


def switch_tabs(driver, tabNum):
    driver.switch_to.window(driver.window_handles[tabNum])


def checkElementHasClass(driver, CssSelector, className):
    t = driver.execute_script("return $('{CssSelector}')[0]".format(CssSelector=CssSelector))
    clsVal = t.get_attribute("class")
    print(clsVal)
    if className in clsVal:
        return True
    else:
        return False


def checkElementHasAttrXpath(wait, Xpath, attr, time_try=10):
    checkClassSuccess = False
    count = 0
    while not checkClassSuccess:
        try:
            t = wait.until(EC.element_to_be_clickable((By.XPATH, Xpath)))
            clsVal = t.get_attribute(attr)
            if clsVal:
                return True
            else:
                return False
        except TimeoutException as err:
            count = count + 1
            if count == time_try:
                raise err
            print('Có lỗi khi kiểm tra attr ! Thử lại')
            continue


def GetAttrElement(driver, xpath, attr, time_try=10, time_out=5, is_multiple_element=False, index=0):
    checkClassSuccess = False
    count = 0
    wait = WebDriverWait(driver=driver, timeout=time_out)
    while not checkClassSuccess:
        try:
            if not is_multiple_element:
                t = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            else:
                t = driver.find_elements_by_xpath(xpath)[index]
            print(t)
            clsVal = t.get_attribute(attr)
            if clsVal:
                return clsVal
            else:
                return ''
        except TimeoutException as err:
            count = count + 1
            if count == time_try:
                raise err
            print('Có lỗi khi kiểm tra attr ! Thử lại')
            continue


def openNewTabWithUrl(url, driver, last_num_tab):
    driver.execute_script(
        "window.open('{path}');".format(path=url))
    switch_tabs(driver=driver, tabNum=(last_num_tab + 1))


def back(driver):
    driver.execute_script("window.history.go(-1)")


def closeCurrentTab(driver, last_tab_after_close):
    driver.close()
    switch_tabs(driver=driver, tabNum=last_tab_after_close)


def countElement(driver, xpath, timeout=10):
    try:
        wait = WebDriverWait(driver=driver, timeout=timeout)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        customElement = driver.find_elements_by_xpath(xpath)
        return len(customElement)
    except:
        return 0


def numberTabs(driver):
    return len(driver.window_handles)


def clickByXpath(driver, wait, xpath, timesleeprandom1=0, timesleeprandom2=0, time_try=5, manualCheck=False,
                 is_multiple_element=False, isRandom=False, IndexClick=0, click_all=False,
                 handle_NoInteractAble_with_js=False, click_clickable=False):
    count = 0
    while count != time_try:
        try:
            customElement = None
            if click_clickable:
                customElements = wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
                for element in customElements:
                    if element.is_displayed():
                        customElement = element
                        clickHandlerException(driver=driver, buttonElement=customElement,
                                              handle_NoInteractAble_with_js=handle_NoInteractAble_with_js)
            else:
                customElement = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                clickHandlerException(driver=driver, buttonElement=customElement,
                                      handle_NoInteractAble_with_js=handle_NoInteractAble_with_js)
            print(customElement)
            if is_multiple_element:
                customElement = wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
                print(customElement)
                if not click_all:
                    if isRandom:
                        customElement = customElement[random.randint(0, len(customElement) - 1)]
                    else:
                        customElement = customElement[IndexClick]
                    print(customElement)
                    clickHandlerException(driver=driver, buttonElement=customElement,
                                          handle_NoInteractAble_with_js=handle_NoInteractAble_with_js)
                else:
                    for element in customElement:
                        try:
                            clickHandlerException(driver=driver, buttonElement=element,
                                                  handle_NoInteractAble_with_js=handle_NoInteractAble_with_js)
                        except ElementNotInteractableException as error:
                            print(error)
                            pass
            if timesleeprandom1 != 0:
                if timesleeprandom2 != 0:
                    time.sleep(random.randint(timesleeprandom1, timesleeprandom2))
            break
        except TimeoutException as err:
            count = count + 1
            if count == time_try:
                if manualCheck:
                    print('Click lỗi hãy kiểm tra lại')
                    time.sleep(20)
                    continue
                else:
                    raise err
        except Exception as err:
            raise err


def sendKeyByXpath(wait, xpath, keys, timesleeprandom1=0, timesleeprandom2=0, time_try=5, manualCheck=False,
                   check_value=True, check_text=False, continue_send=False, send_element_show=False):
    count = 0
    while count < time_try:
        try:
            inputElement = None
            if send_element_show:
                customElements = wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
                for element in customElements:
                    if element.is_displayed():
                        inputElement = element
            else:
                inputElement = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            if timesleeprandom1 != 0:
                if timesleeprandom2 != 0:
                    time.sleep(random.randint(timesleeprandom1, timesleeprandom2))
            if not continue_send:
                if inputElement:
                    inputElement.clear()
            if inputElement:
                inputElement.send_keys(keys)
            if check_value:
                print(inputElement.get_attribute('value'))
                if str(inputElement.get_attribute('value')) != keys:
                    print('Input chưa nhận keys ! Thử lại')
                    continue
                break
            if check_text:
                print(inputElement.text)
                if str(inputElement.text) != keys:
                    print('Input chưa nhận keys ! Thử lại')
                    continue
                break
            # Nếu không check gì thì chuyển
            break
        except TimeoutException as err:
            count = count + 1
            if count == time_try:
                if manualCheck:
                    print('Send key lỗi hãy kiểm tra lại')
                    time.sleep(100)
                    continue
                else:
                    raise err


def checkElementExistingXpath(driver, xpath, wait=None, time_try=5, time_out=4):
    if not wait:
        wait = WebDriverWait(driver=driver, timeout=time_out)
    count = 0
    while count < time_try:
        try:
            wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            count = count + 1
    return False


def checkElementClickAbleXpath(driver, xpath, wait=None, time_try=5, time_out=4):
    if not wait:
        wait = WebDriverWait(driver=driver, timeout=time_out)
    count = 0
    while count < time_try:
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return True
        except TimeoutException:
            count = count + 1
    return False


def checkAnyElementVisibleXpath(driver, xpath, wait=None, time_try=5, time_out=4):
    if not wait:
        wait = WebDriverWait(driver=driver, timeout=time_out)
    count = 0
    while count < time_try:
        try:
            wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            count = count + 1
    return False


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


def deleteContentFolderAndFolder(folderPath):
    import os, shutil
    folder = folderPath
    try:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
                continue
        shutil.rmtree(folder)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (folder, e))


def quitAllDriver(driver):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        driver.close()
    driver.quit()


def getAuthCodeFromFile(auth_path):
    isReadCodeSuccess = False
    while not isReadCodeSuccess:
        try:
            with open(auth_path) as authFile:
                return authFile.read()[0:-1]
        except Exception as err:
            print(err)
            print('Lỗi khi đọc file auth')
            continue


def ResetMailCodeFile(codeMailPath):
    with open(codeMailPath, 'w') as codeMailFile:
        # Reset lại mailbox
        codeMailFile.write('')
        codeMailFile.close()


def CheckStringIsUrl(url):
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    result = re.match(regex, url)
    if result:
        return True
    return False


def getAllCatagoriesAndSaveToFile(driver, filePath):
    # click hết để load các catagories
    listXpath = './/span[@data-action="toggle-category"]/a'
    clickByXpath(driver=driver, wait=WebDriverWait(driver=driver, timeout=10), xpath=listXpath,
                 is_multiple_element=True, click_all=True)

    time.sleep(10)

    # Lấy hết tên catagory vào arr

    catagoriesXpath = './/input[@nodeid and @id and @type="checkbox"]/following-sibling::i/following-sibling::span'
    catagories = driver.find_elements_by_xpath(catagoriesXpath)
    print(catagories)
    # Lặp qua từng catagory lấy tên lưu vào file
    isSaveCatagoriesSuccess = False
    while not isSaveCatagoriesSuccess:
        try:
            with open(filePath, 'w') as catagoriesFile:
                for catagory in catagories:
                    print(catagory.text)
                    if catagory.text != '':
                        catagoriesFile.writelines(f'{catagory.text}\n')
                catagoriesFile.close()
            isSaveCatagoriesSuccess = True
        except Exception as err:
            print(err)
            traceback.print_exc()
            print('Có lỗi khi lưu file catagory')
            continue


def getAllCatagoriesByNameAndSaveToFile(driver, filePath):
    # click hết để load các catagories
    listXpath = './/span[@data-action="toggle-category"]/a'
    clickByXpath(driver=driver, wait=WebDriverWait(driver=driver, timeout=10), xpath=listXpath,
                 is_multiple_element=True, click_all=True)

    time.sleep(10)

    # Lấy hết tên catagory vào arr

    catagoriesXpath = './/input[@nodeid and @id and @type="checkbox"]/following-sibling::i/following-sibling::span'
    catagories = driver.find_elements_by_xpath(catagoriesXpath)
    print(catagories)
    # Lặp qua từng catagory lấy tên lưu vào file
    isSaveCatagoriesSuccess = False
    while not isSaveCatagoriesSuccess:
        try:
            with open(filePath, 'w') as catagoriesFile:
                for catagory in catagories:
                    print(catagory.text)
                    if catagory.text != '':
                        catagoriesFile.writelines(f'{catagory.text}\n')
                catagoriesFile.close()
            isSaveCatagoriesSuccess = True
        except Exception as err:
            print(err)
            traceback.print_exc()
            print('Có lỗi khi lưu file catagory')
            continue


def selectCatagories(driver, wait, white_list_path, num_select=2):
    # Lấy ngẫu nhiên 2 category từ white list
    isGetRandomCategoriesFinished = False
    categoriesLinkSelected = []
    while not isGetRandomCategoriesFinished:
        try:
            with open(white_list_path) as whiteList:
                categoriesLink = whiteList.readlines()
                indexRandom = random.randint(0, len(categoriesLink) - 1)
                # Get category
                categoryLink = categoriesLink[indexRandom]
                #
                categoryLink = categoryLink[0:-1]
                print(f'Thử {categoryLink}')
                if categoryLink not in categoriesLinkSelected:
                    categoriesLinkSelected.append(categoryLink)
                    print(f'Chọn {categoryLink}')
                if len(categoriesLinkSelected) == num_select:
                    isGetRandomCategoriesFinished = True
        except Exception as err:
            print(err)
            print('Có lỗi trong khi chọn category từ white list ! Thử lại')
            time.sleep(5)
            traceback.print_exc()
            continue

    for categoryLink in categoriesLinkSelected:
        # tranform categoryLink to categoryXpath
        categoryXpath = mapCategoryLinkToXpath(categoryLink)

        #
        categoryNames = categoryLink.split('/')

        # Bỏ tên cuối
        categoryNamesToExpand = categoryNames[0:-1]

        # click hết để expand đến category

        for index, name in enumerate(categoryNamesToExpand):
            try:
                # icon collapse-icon
                listCheckXpath = f'.//div[contains(@class,"collapse-icon")]/../../span[@data-action="toggle-category"]/a[text()="{name}"]/..'
                isNotNeedExpand = checkElementExistingXpath(driver=driver, wait=WebDriverWait(driver=driver, timeout=5),
                                                            xpath=listCheckXpath, time_try=2)
                if not isNotNeedExpand:
                    print(f'Expand cây đến tên loại {name}')
                    # .//*[text()="Nonfiction"]/../../.././/*[text()="Computers"]/../../.././/*[text()="Programming"]/../../.././/*[text()="Games"]/../../..
                    if index == 0:
                        listXpath = f'.//div[contains(@class,"expand-icon")]/../../span[@data-action="toggle-category"]/a[text()="{name}"]/..'
                    else:
                        listXpath = f'.//div[contains(@class,"expand-icon")]/../../span[@data-action="toggle-category"]/a[text()="{name}"]/..'
                    clickByXpath(driver=driver, wait=WebDriverWait(driver=driver, timeout=10), xpath=listXpath,
                                 click_all=True, is_multiple_element=True, no_check_click=True)
                else:
                    print(f'Không cần expand cây đến tên loại {name}')
            except Exception as err:
                print(err)
                pass

        # nhấn chọn loại
        print('Nhấn chọn loại')
        clickByXpath(driver=driver, wait=wait, xpath=categoryXpath)


def uploadFile(driver, wait, open_box_element_input_xpath, keys):
    isUploadFileSuccess = False
    while not isUploadFileSuccess:
        try:
            import pyautogui
            clickByXpath(driver=driver, xpath=open_box_element_input_xpath, wait=wait, timesleeprandom1=1,
                         timesleeprandom2=3)
            time.sleep(5)
            pyautogui.write(keys)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            isUploadFileSuccess = True
        except Exception as err:
            raise err


def mapCategoryLinkToXpath(categoryLink):
    # .//*[text()="Nonfiction"]/../../.././/*[text()="Computers"]/../../.././/*[text()="Programming"]/../../.././/*[text()="Games"]/../../..
    # Link Structure : Nonfiction/Computers/Programming/Games

    # split link

    nameCategories = categoryLink.split('/')
    xpath = ''
    for index, nameCategory in enumerate(nameCategories):
        if index == 0:
            xpath = xpath + f'.//*[text()="{nameCategory}"]/../../../'
            continue
        if index == len(nameCategories) - 1:
            xpath = xpath + f'.//*[text()="{nameCategory}"]/../../..'
            return xpath
        xpath = xpath + f'.//*[text()="{nameCategory}"]/../../../'


def mapArrPathToXpath(ArrPath):
    nameCategories = ArrPath
    xpath = ''
    for index, nameCategory in enumerate(nameCategories):
        if index == 0:
            xpath = xpath + f'.//*[text()="{nameCategory}"]/../../../'
            continue
        if index == len(nameCategories) - 1:
            xpath = xpath + f'.//*[text()="{nameCategory}"]/..'
            return xpath
        xpath = xpath + f'.//*[text()="{nameCategory}"]/../../../'


def checkLoading(driver):
    # check loading
    isLoading = True
    while isLoading:
        loadingXpath = './/div[@id="loadingDiv"]'
        isLoading = checkElementExistingXpath(driver=driver, wait=WebDriverWait(driver=driver, timeout=5),
                                              xpath=loadingXpath)
        if isLoading:
            time.sleep(5)
            print('Đang load')
        else:
            print('Không loading')


def switchToPopupWindow(driver, main_page):
    # changing the handles to access login page
    login_page = None
    for handle in driver.window_handles:
        if handle != main_page:
            login_page = handle

    # change the control to signin page
    driver.switch_to.window(login_page)


def checkIsStartDownload(path_to_downloads):
    for fname in os.listdir(path_to_downloads):
        if fname.endswith('.crdownload'):
            return True
    return False


def download_wait(path_to_downloads, filename: str, test=False):
    seconds = 0
    dl_wait = True
    check_time = 1000
    if test:
        check_time = 5
    while dl_wait and seconds < check_time:
        time.sleep(1)
        dl_wait = True
        for fname in os.listdir(path_to_downloads):
            if filename in fname:
                return fname
            for token in filename.split():
                if token in fname:
                    dl_wait = False
                    return fname
        seconds += 1
    return False
