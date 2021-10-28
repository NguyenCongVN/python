import requests
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import WindowAutomationPart
import traceback
import threading
from InteractHelper import waitThreadAndJoin


class windowAutoThread(threading.Thread):
    def __init__(self, windowPath, startCom, stopCom, exceptComOut):
        threading.Thread.__init__(self)
        self.windowPath = windowPath
        self.startCom = startCom
        self.stopCom = stopCom
        self.exceptComOut = exceptComOut

    def run(self):
        time.sleep(40)
        # # back to window working
        print('opening window')
        window = WindowAutomationPart.OpenWindow(self.windowPath)
        print('handling window')
        WindowAutomationPart.handleComRange(window, self.startCom, self.stopCom, self.windowPath, self.exceptComOut)


class windowAutoThreadCustomized(threading.Thread):
    def __init__(self, windowPath, startCom, stopCom, exceptComOut, pathThunderBirdData, pathThunderBirdExe):
        threading.Thread.__init__(self)
        self.windowPath = windowPath
        self.startCom = startCom
        self.stopCom = stopCom
        self.exceptComOut = exceptComOut
        self.pathThunderBirdData = pathThunderBirdData
        self.pathThunderBirdExe = pathThunderBirdExe

    def run(self):
        # # back to window working
        print('opening window')
        window = WindowAutomationPart.OpenWindow(self.windowPath)
        print('handling window')
        WindowAutomationPart.handleComRangeCustomized(window, self.startCom, self.stopCom, self.windowPath,
                                                      self.exceptComOut, self.pathThunderBirdData,
                                                      self.pathThunderBirdExe)


def clickWithJs(driver, buttonElement):
    driver.execute_script("arguments[0].click();", buttonElement)


def clickHandlerException(driver, buttonElement):
    try:
        buttonElement.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        print('error interception => handle with js function')
        clickWithJs(driver, buttonElement)


def open_driver(path):
    options = Options()
    options.binary_location = path
    # you may need some other options
    options.add_experimental_option("useAutomationExtension", value=False)
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--no-sandbox')
    options.add_argument('--no-default-browser-check')
    options.add_argument('--no-first-run')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-default-apps')
    driver = webdriver.Chrome(executable_path=r'D:\python\chromedriver80\chromedriver.exe', options=options)
    driver.maximize_window()
    return driver


#
def press_an_key_with_control(driver, wait, key):
    wait.until()
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys(key).key_up(Keys.CONTROL).perform()


# switch tab
def switch_tabs(driver, tabNum):
    driver.switch_to.window(driver.window_handles[tabNum])


#  press project button
def press_project(driver, wait):
    # try: //a[text()=' My projects '] contains(text(),"My projects")
    cssSelectorProjectBtn = '//a[contains(text(),"My projects")]'
    projectBtn = wait.until(EC.element_to_be_clickable((By.XPATH, cssSelectorProjectBtn)))
    clickHandlerException(driver, projectBtn)


def checkElementHasClass(driver, CssSelector, className):
    t = driver.execute_script("return $('{CssSelector}')[0]".format(CssSelector=CssSelector))
    clsVal = t.get_attribute("class")
    print(clsVal)
    if className in clsVal:
        return True
    else:
        return False


def addJqueryToHtml(driver):
    i = 0
    while i < 10:
        try:
            jquery = requests.get("https://code.jquery.com/jquery-3.5.1.js").text
            driver.execute_script(jquery)
            driver.execute_script("""
                if (window.jQuery) {  
        
                } else {
                    // jQuery is not loaded
                    alert("Doesn't Work In Jquery");
                }""")
            break
        except:
            i = i + 1
            continue


# https: // console.cloud.google.com / compute
def openNewTabWithUrl(url, driver):
    driver.execute_script(
        "window.open('{path}');".format(path=url))


# main flow run
def InitRun(pathChrome, pathCode, wantCopy):
    driver = open_driver(pathChrome)
    # run and init pages
    driver.get('https://console.cloud.google.com/billing')

    # add jquery to brower tab 0
    addJqueryToHtml(driver)
    openNewTabWithUrl(r'https://console.cloud.google.com/compute', driver)

    # switch tab 1
    switch_tabs(driver, 1)

    # add jquery to brower tab 1

    addJqueryToHtml(driver)
    # time.sleep(3)
    #     copy file code
    if wantCopy:
        WindowAutomationPart.copyFile(pathCode, pathCode.split('\\')[-1])
    return driver


#     need change start stop with number of computer : done not test
def startComRange(wait, driver, start, stop):
    # select computer
    # add sleep to fix
    # time.sleep(3)
    for i in range(start, stop + 1):
        result = driver.execute_script('''
        $($('.p6n-tag-value')).each(function(idx ,item){{
        if($(item).text() == ': {number}')
        {{$($($($($($($($($($(item).parent()).parent()).parent()).parent()).parent()).parent()).parent()).parent()).find('[type="checkbox"]')).click()}}
        }})'''.format(number=i))
        print(result)

    # run virtual Com

    # Start / Resume

    while True:
        try:
            driver.execute_script('''$($($($('pan-action-bar-button[icon="start"]')).children()).children()).click()''')
            startXPath = '//a//span[contains(text(),"Start")]'
            start = wait.until(EC.element_to_be_clickable((By.XPATH, startXPath)))
            clickHandlerException(driver, start)
            waitThreadAndJoin(5)
            try:
                startCheck = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, startXPath)))
                print('click again because it\'s appeared')
                clickHandlerException(driver, startCheck)
            except:
                break
        except:
            continue
    # check if success if not start again
    elementText = ''
    while True:
        successString = 'succeeded'
        try:
            elementText = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.p6n-toast-content'))).text
        except (selenium.common.exceptions.StaleElementReferenceException, selenium.common.exceptions.TimeoutException):
            continue
        if successString in elementText:
            print('Success')
            break
        else:
            if 'failed' in elementText.lower():
                while True:
                    # try:
                    print('Start again')
                    driver.execute_script(
                        '''$($($($('pan-action-bar-button[icon="start"]')).children()).children()).click()''')
                    startXPath = '//a//span[contains(text(),"Start")]'
                    start = wait.until(EC.element_to_be_clickable((By.XPATH, startXPath)))
                    clickHandlerException(driver, start)
                    waitThreadAndJoin(5)
                    try:
                        startCheck = WebDriverWait(driver, 1).until(
                            EC.element_to_be_clickable((By.XPATH, startXPath)))
                        print('click again because it\'s appeared')
                        clickHandlerException(driver, startCheck)
                    except:
                        break
                    # except:
                    #     print('Failed Start again')
                    #     continue
            else:
                continue


# Stop
def stopComAll(wait, driver):
    while True:
        try:
            headerXpath = '//*[@id = "headerCheckbox"]//ancestor::th'
            header = wait.until(EC.element_to_be_clickable((By.XPATH, headerXpath)))
            clickHandlerException(driver, header)
            driver.execute_script('''$($($($('pan-action-bar-button[icon="stop"]')).children()).children()).click()''')
            stopXPath = '//a//span[contains(text(),"Stop")]'
            # contains(text(),"Stop")
            # /html/body/div[6]/md-dialog/md-dialog/md-dialog-actions/pan-modal-actions/pan-modal-action[2]/a
            stop = wait.until(EC.element_to_be_clickable((By.XPATH, stopXPath)))
            clickHandlerException(driver, stop)
            waitThreadAndJoin(5)
            try:
                stopCheck = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, stopXPath)))
                print('click again because it\'s appeared')
                clickHandlerException(driver, stopCheck)
            except:
                break
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
            traceback.print_exc()
            driver.refresh()
            addJqueryToHtml(driver)
            continue
    # check if success if not stop again
    elementText = ''
    while True:
        successString = 'succeeded'
        try:
            elementText = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.p6n-toast-content'))).text
        except (selenium.common.exceptions.StaleElementReferenceException, selenium.common.exceptions.TimeoutException):
            continue
        if successString in elementText:
            print('Success')
            break
        else:
            if 'failed' in elementText.lower():
                while True:
                    try:
                        print('stop again')
                        driver.execute_script(
                            '''$($($($('pan-action-bar-button[icon="stop"]')).children()).children()).click()''')
                        stopXPath = '//span[contains(text(),"Stop")]'
                        stop = wait.until(EC.element_to_be_clickable((By.XPATH, stopXPath)))
                        clickHandlerException(driver, stop)
                        # time.sleep(10)
                        break
                    except:
                        print('Failed stop again')
                        continue
            else:
                continue
    # time.sleep(4)
    driver.execute_script('''$('#headerCheckbox').click()''')


def enableBill(driver, wait, KDPRange, inputBill):
    while True:
        try:
            press_project(driver, wait)
            # choose project and enable bill
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Table of projects"]')))
            scriptClickProject = '''
                var target;
                $('.cfc-inline-flex-container').each(function(idx){{
                txt = $(this).text();
                if(txt.includes('{KDPRange}')){{
                target = $($(this).parent()).parent()
                }}}});
                $($($(target).children()[4]).find('button')).click();
                '''.format(KDPRange=KDPRange)

            driver.execute_script(scriptClickProject)

            # click change bill  //span[text()=" Set account "]   contains(text(),"Change billing")
            changeBillingCssSelector = '//span[contains(text(),"Change billing")]'
            changeBillingButton = wait.until(EC.presence_of_element_located((By.XPATH, changeBillingCssSelector)))
            clickHandlerException(driver, changeBillingButton)

            # click select bill
            billingSelectCssSelector = '.mat-form-field-infix'
            selectButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, billingSelectCssSelector)))
            clickHandlerException(driver, selectButton)

            # select bill
            # billNumber = 1
            # {billNumber}
            billingCssSelector = '//mat-optgroup//mat-option[{billNumber}]'.format(
                billNumber=int(inputBill))
            BillSelect = wait.until(EC.presence_of_element_located((By.XPATH, billingCssSelector)))
            clickHandlerException(driver, BillSelect)

            # accept bill contains(text(),"Set account")
            setAccountCssSelector = '//span[contains(text(),"Set account")]'
            setAccountButton = wait.until(EC.presence_of_element_located((By.XPATH, setAccountCssSelector)))
            clickHandlerException(driver, setAccountButton)
            break
        except selenium.common.exceptions.TimeoutException:
            driver.refresh()
            addJqueryToHtml(driver)
            continue


def chooseProject(driver, wait, KDPRange):
    while True:
        try:
            # click choose project
            switch_tabs(driver, 1)
            chooseTabCssSelector = '.gm1-switcher-button.cfc-switcher-button'
            chooseTab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, chooseTabCssSelector)))
            clickHandlerException(driver, chooseTab)

            # Click All button contains(text(),"All")
            try:
                allCssSelector = '//div[contains(text(),"All")]'
                allButton = wait.until(EC.element_to_be_clickable((By.XPATH, allCssSelector)))
                clickHandlerException(driver, allButton)
            except:
                allXpath = '/html/body/div[3]/div[2]/div/mat-dialog-container/ng-component/div[1]/mat-tab-group/mat-tab-header/div[2]/div/div/div[3]'
                allButton = wait.until(EC.element_to_be_clickable((By.XPATH, allXpath)))
                clickHandlerException(driver, allButton)
            # Select project in tab 1
            # time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'cfc-tree-node-expander')))
            selectProjectScript = """
            $('a.ng-star-inserted').each(function(idx){{
            txt = $(this).text()
            if(txt.includes('{KDPRange}')){{
            this.click()}}
            }})
            """.format(KDPRange=KDPRange)
            driver.execute_script(selectProjectScript)

            # select button to show label
            # time.sleep(5)
            collumnButtonCssSelector = '.goog-flat-menu-button'
            collumnButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, collumnButtonCssSelector)))
            clickHandlerException(driver, collumnButton)
            labelCssSelector = '//span[contains(text(),"Labels")]'
            labelCssSelectorCheck = '.p6n-dropdown-row:contains("Labels") input'
            if checkElementHasClass(driver, labelCssSelectorCheck, 'ng-empty'):
                print('waiting to click label')
                labelButton = wait.until(EC.element_to_be_clickable((By.XPATH, labelCssSelector)))
                clickHandlerException(driver, labelButton)
            else:
                print('no need to enable label again')
                clickHandlerException(driver, collumnButton)
            # sort the column
            # ignore sort collumn
            # sortLabelXPath = '/html/body/pan-shell/pcc-shell/cfc-panel-container/div/div/cfc-panel[1]/div[1]/div/div[3]/cfc-panel-container/div/div/cfc-panel/div/div/cfc-panel-container/div/div/cfc-panel[1]/div/div/cfc-panel-container/div/div/cfc-panel[2]/div/div/central-page-area/div/div/pcc-content-viewport/div/div/ng2-router-root/div/ng1-router-root-loader/xap-deferred-loader-outlet/ng1-router-root-wrapper/ng1-router-root/div/ng-view/pan-panel-container/div/div/div/div/div/div/div/div[2]/ng-transclude/div/table/thead/tr/th[8]/span[1]/a'
            # sortButton = wait.until(EC.element_to_be_clickable((By.XPATH, sortLabelXPath)))
            # sortButton.click()
            break
        except (
                selenium.common.exceptions.TimeoutException,
                selenium.common.exceptions.ElementNotInteractableException) as e:
            print('Cant find computers')
            driver.execute_script("window.history.go(-1)")
            driver.refresh()
            driver.execute_script("window.history.go(1)")
            addJqueryToHtml(driver)
            continue


def disableBill(driver, wait, KDPRange):
    # disable bill
    tryCount = 0
    while True:
        try:
            switch_tabs(driver, 0)
            # time.sleep(5)
            press_project(driver, wait)
            # choose project and disable bill
            # time.sleep(10)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Table of projects"]')))
            scriptClickProject = '''
                    var target;
                    $('.cfc-inline-flex-container').each(function(idx){{
                    txt = $(this).text();
                    if(txt.includes('{KDPRange}')){{
                    target = $($(this).parent()).parent()
                    }}}});
                    $($($(target).children()[4]).find('button')).click();
                    '''.format(KDPRange=KDPRange)
            print('select bill to disable')
            driver.execute_script(scriptClickProject)
            # time.sleep(5) contains(text(),"Disable billing")
            disableBillCssSelector = '//span[contains(text(),"Disable billing")]'
            disableBillButton = wait.until(EC.element_to_be_clickable((By.XPATH, disableBillCssSelector)))
            clickHandlerException(driver, disableBillButton)
            # driver.execute_script("arguments[0].click();", disableBillButton)
            # time.sleep(3)
            # while True:
            #     try:
            #         check = driver.find_element_by_xpath(disableBillXPath)
            #         check.click()
            #         # time.sleep(3)
            #     except:
            #         print('check is disappear')
            #         break
            # accept disable bill
            # contains(text(),"Disable billing")
            acceptCssSelector = '//span[contains(text(),"Disable billing")]'
            acceptButton = wait.until(EC.element_to_be_clickable((By.XPATH, acceptCssSelector)))
            clickHandlerException(driver, acceptButton)
            break
        except Exception as e:
            if tryCount < 5:
                tryCount = tryCount + 1
                continue
            else:
                raise e


# C:\Users\Admin\Documents\GGC KDP\PO Ho Chieu 1 KDP thang 1 2021 1345-2112\PO Ho Chieu 1\GoogleChromePortable.exe
def run(KDPRange, windowPath, exceptCom, pathThunderBirdData, pathThunderBirdExe):
    [start, stop] = KDPRange.split('-')
    start = int(start)
    stop = int(stop)
    exceptComOut = exceptCom.split(',')
    customThread = windowAutoThreadCustomized(startCom=start, stopCom=stop, windowPath=windowPath,
                                              exceptComOut=exceptComOut, pathThunderBirdData=pathThunderBirdData,
                                              pathThunderBirdExe=pathThunderBirdExe)
    customThread.start()
    customThread.join()
    # # stopComAll(wait, driver)
