import requests
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import WindowAutomationPart
import traceback
import threading
class windowAutoThread (threading.Thread):
    def __init__(self , windowPath , startCom , stopCom):
        threading.Thread.__init__(self)
        self.windowPath = windowPath
        self.startCom = startCom
        self.stopCom = stopCom
    def run(self):
        time.sleep(40)
        # # back to window working
        window = WindowAutomationPart.OpenWindow(self.windowPath)
        WindowAutomationPart.handleComRange(window, self.startCom, self.stopCom, self.windowPath)

def clickWithJs(driver ,buttonElement):
    driver.execute_script("arguments[0].click();", buttonElement)

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
def press_an_key_with_control(driver ,wait, key):
    wait.until()
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys(key).key_up(Keys.CONTROL).perform()
# switch tab
def switch_tabs(driver ,tabNum):
    driver.switch_to.window(driver.window_handles[tabNum])
#  press project button
def press_project(driver ,wait):
    # try: //a[text()=' My projects ']
    cssSelectorProjectBtn = '//a[text()=" My projects "]'
    projectBtn = wait.until(EC.element_to_be_clickable((By.XPATH , cssSelectorProjectBtn)))
    projectBtn.click()
    # except selenium.common.exceptions.ElementClickInterceptedException:
    #     clickWithJs(driver, projectBtn)
#     .p6n-dropdown-row:contains("Labels") input
def checkElementHasClass(driver, CssSelector , className):
    t = driver.execute_script("return $('{CssSelector}')[0]".format(CssSelector = CssSelector))
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
def openNewTabWithUrl(url , driver):
    driver.execute_script(
        "window.open('{path}');".format(path=url))

# main flow run
def InitRun(pathChrome , pathCode , wantCopy):
    driver = open_driver(pathChrome)
    # run and init pages
    driver.get('https://console.cloud.google.com/billing')

    # add jquery to brower tab 0
    addJqueryToHtml(driver)
    openNewTabWithUrl(r'https://console.cloud.google.com/compute' , driver)


    # switch tab 1
    switch_tabs(driver ,1)

    # add jquery to brower tab 1

    addJqueryToHtml(driver)
    # time.sleep(3)
#     copy file code
    if wantCopy:
        WindowAutomationPart.copyFile(pathCode, pathCode.split('\\')[-1])
    return driver
#     need change start stop with number of computer : done not test
def startComRange(wait , driver , start , stop):
    # select computer
    # add sleep to fix
    time.sleep(3)
    for i in range(start, stop + 1):
        driver.execute_script('''
        $($('.p6n-tag-value')).each(function(idx ,item){{
        if($(item).text().includes('{number}'))
        {{$($($($($($($($($($(item).parent()).parent()).parent()).parent()).parent()).parent()).parent()).parent()).find('[type="checkbox"]')).click()}}
        }})'''.format(number=i))

    # run virtual Com

    # Start / Resume


    while True:
        try:
            driver.execute_script('''$($($($('pan-action-bar-button[icon="start"]')).children()).children()).click()''')
            startXPath = '//span[text()="Start"]'
            # /html/body/div[6]/md-dialog/md-dialog/md-dialog-actions/pan-modal-actions/pan-modal-action[2]/a
            start = wait.until(EC.presence_of_element_located((By.XPATH, startXPath)))
            start.click()
            break
            # time.sleep(5)
            # while True:
            #     try:
            #         check = driver.find_element_by_xpath(startXPath)
            #         start.click()
            #         # time.sleep(3)
            #     except:
            #         print('check is disappear')
            #         break
            # break
        except:
            continue
    # check if success if not start again
    elementText = ''
    while True:
        successString = 'succeeded'
        try:
            elementText = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.p6n-toast-content'))).text
        except (selenium.common.exceptions.StaleElementReferenceException , selenium.common.exceptions.TimeoutException):
            continue
        if successString in elementText:
            print('Success')
            break
        else:
            if 'failed' in elementText.lower():
                while True:
                    try:
                        print('Start again')
                        driver.execute_script(
                            '''$($($($('pan-action-bar-button[icon="start"]')).children()).children()).click()''')
                        startXPath = '//span[text()="Start"]'
                        start = wait.until(EC.presence_of_element_located((By.XPATH, startXPath)))
                        start.click()
                        # time.sleep(10)
                        break
                    except:
                        print('Failed Start again')
                        continue
            else:
                continue
# Stop
def stopComAll(wait , driver):
    while True:
        try:
            driver.execute_script('''$('#headerCheckbox').click()''')
            driver.execute_script('''$($($($('pan-action-bar-button[icon="stop"]')).children()).children()).click()''')
            stopXPath = '//span[text()="Stop"]'
            # /html/body/div[6]/md-dialog/md-dialog/md-dialog-actions/pan-modal-actions/pan-modal-action[2]/a
            stop = wait.until(EC.element_to_be_clickable((By.XPATH , stopXPath)))
            stop.click()
            break
            # driver.execute_script("arguments[0].click();", stop)
            # time.sleep(3)
            # while True:
            #     try:
            #         check = driver.find_element_by_xpath(stopXPath)
            #         stop.click()
            #         # time.sleep(3)
            #     except:
            #         print('check is disappear')
            #         break
        except (selenium.common.exceptions.TimeoutException , selenium.common.exceptions.NoSuchElementException):
            traceback.print_exc()
            driver.refresh()
            # time.sleep(5)
            addJqueryToHtml(driver)
            # time.sleep(5)
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
                        stopXPath = '//span[text()="Stop"]'
                        stop = wait.until(EC.element_to_be_clickable((By.XPATH, stopXPath)))
                        stop.click()
                        # time.sleep(10)
                        break
                    except:
                        print('Failed stop again')
                        continue
            else:
                continue
    # time.sleep(4)
    driver.execute_script('''$('#headerCheckbox').click()''')

def enableBill(driver , wait, KDPRange , inputBill):
    press_project(driver ,wait)
    # choose project and enable bill
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR , '[aria-label="Table of projects"]')))
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

    # click change bill  //span[text()=" Set account "]
    changeBillingCssSelector = '//span[text()=" Change billing "]'
    changeBillingButton = wait.until(EC.presence_of_element_located((By.XPATH, changeBillingCssSelector)))
    changeBillingButton.click()

    # click select bill
    billingSelectCssSelector = '.mat-form-field-infix'
    selectButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, billingSelectCssSelector)))
    selectButton.click()

    # select bill
    # billNumber = 1
    # {billNumber}
    billingCssSelector = '//mat-optgroup//mat-option[{billNumber}]'.format(
        billNumber=int(inputBill))
    BillSelect = wait.until(EC.presence_of_element_located((By.XPATH, billingCssSelector)))
    BillSelect.click()

    # accept bill
    setAccountCssSelector = '//span[text()=" Set account "]'
    setAccountButton = wait.until(EC.presence_of_element_located((By.XPATH, setAccountCssSelector)))
    setAccountButton.click()

def chooseProject(driver , wait , KDPRange):
    while True:
        try:
            # click choose project
            switch_tabs(driver, 1)
            chooseTabCssSelector = '.gm1-switcher-button.cfc-switcher-button'
            chooseTab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR , chooseTabCssSelector)))
            chooseTab.click()

            # Click All button
            try:
                allCssSelector = '//div[text()="All"]'
                allButton = wait.until(EC.element_to_be_clickable((By.XPATH , allCssSelector)))
                allButton.click()
            except:
                allXpath = '/html/body/div[3]/div[2]/div/mat-dialog-container/ng-component/div[1]/mat-tab-group/mat-tab-header/div[2]/div/div/div[3]'
                allButton = wait.until(EC.element_to_be_clickable((By.XPATH, allXpath)))
                allButton.click()

            # Select project in tab 1
            # time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'cfc-tree-node-expander')))
            selectProjectScript = """
            $('a.ng-star-inserted').each(function(idx){{
            txt = $(this).text()
            if(txt.includes('{KDPRange}')){{
            this.click()}}
            }})
            """.format(KDPRange = KDPRange)
            driver.execute_script(selectProjectScript)

            # select button to show label
            # time.sleep(5)
            collumnButtonCssSelector = '.goog-flat-menu-button'
            collumnButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR , collumnButtonCssSelector)))
            collumnButton.click()
            labelCssSelector = '//span[text()="Labels"]'
            labelCssSelectorCheck = '.p6n-dropdown-row:contains("Labels") input'
            if checkElementHasClass(driver ,labelCssSelectorCheck , 'ng-empty'):
                labelButton = wait.until(EC.element_to_be_clickable((By.XPATH ,labelCssSelector)))
                labelButton.click()
            else:
                collumnButton.click()
            # sort the column
            # ignore sort collumn
            # sortLabelXPath = '/html/body/pan-shell/pcc-shell/cfc-panel-container/div/div/cfc-panel[1]/div[1]/div/div[3]/cfc-panel-container/div/div/cfc-panel/div/div/cfc-panel-container/div/div/cfc-panel[1]/div/div/cfc-panel-container/div/div/cfc-panel[2]/div/div/central-page-area/div/div/pcc-content-viewport/div/div/ng2-router-root/div/ng1-router-root-loader/xap-deferred-loader-outlet/ng1-router-root-wrapper/ng1-router-root/div/ng-view/pan-panel-container/div/div/div/div/div/div/div/div[2]/ng-transclude/div/table/thead/tr/th[8]/span[1]/a'
            # sortButton = wait.until(EC.element_to_be_clickable((By.XPATH, sortLabelXPath)))
            # sortButton.click()
            break
        except selenium.common.exceptions.TimeoutException as e:
            print('Cant find computers')
            driver.execute_script("window.history.go(-1)")
            driver.refresh()
            driver.execute_script("window.history.go(1)")
            addJqueryToHtml(driver)
            continue

def disableBill(driver ,wait , KDPRange):
    # disable bill
    tryCount = 0
    while True:
        try:
            switch_tabs(driver, 0)
            # time.sleep(5)
            press_project(driver ,wait)
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
            # time.sleep(5)
            try:
                disableBillCssSelector = '//span[text()=" Disable billing "]'
                disableBillButton = wait.until(EC.element_to_be_clickable((By.XPATH , disableBillCssSelector)))
                disableBillButton.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                clickWithJs(driver ,disableBillButton)
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
            try:
                #
                acceptCssSelector = '//span[text()=" Disable billing "]'
                acceptButton = wait.until(EC.element_to_be_clickable((By.XPATH, acceptCssSelector)))
                acceptButton.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                clickWithJs(driver ,acceptButton)
            # fix selenium.common.exceptions.ElementClickInterceptedException
            # driver.execute_script("arguments[0].click();", acceptButton)
            break
        except Exception as e:
            if tryCount < 5:
                tryCount = tryCount + 1
                continue
            else:
                raise e

#C:\Users\Admin\Documents\GGC KDP\PO Ho Chieu 1 KDP thang 1 2021 1345-2112\PO Ho Chieu 1\GoogleChromePortable.exe
def run(driver, wait , KDPRange , windowPath , inputBill):
    [start , stop] = KDPRange.split('-')
    start = int(start)
    stop = int(stop)
    switch_tabs(driver, 0)
    enableBill(driver , wait , KDPRange , inputBill)
    chooseProject(driver , wait , KDPRange)
    # time 1
    startComRange(wait , driver , start , start + 11)
    # thread1 = windowAutoThread(startCom=start , stopCom=(start + 11) , windowPath=windowPath)
    # thread1.start()
    # thread1.join()
    stopComAll(wait , driver)

    # time 2
    # startComRange(wait, driver, start + 12 , start + 23 )
    # thread2 = windowAutoThread(startCom= ( start + 12 ), stopCom=(start + 23), windowPath=windowPath)
    # thread2.start()
    # thread2.join()
    # stopComAll(wait, driver)

    # time 3
    startComRange(wait, driver, start + 24, start + 31)
    # thread3 = windowAutoThread(startCom=(start + 24), stopCom=(start + 31), windowPath=windowPath)
    # thread3.start()
    # thread3.join()
    disableBill(driver , wait , KDPRange)