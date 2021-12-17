import os
import shutil
import subprocess
import time
import traceback
import typing
from pathlib import Path

from selenium.webdriver.support.wait import WebDriverWait

from InteractHelper import *
from Interface.Error import TelegramError
from Interface.DiscordData import DiscordData
from Interface.TwitterData import TwitterData
from activity import clickByXpath, download_wait, checkIsStartDownload


def CopyTelegram(telepath):
    CurrentDirectory = os.getcwd()
    from shutil import copyfile
    copyfile(rf'{CurrentDirectory}\Telegram.exe', telepath)


def MoTelegramIndex(telepath: str):
    while True:
        controlDangMo = []
        time_try = 0
        try:
            if time_try == 3:
                raise Exception(TelegramError.time_num_out)
            # Mở app telegram
            print('Mở telegram app')
            subprocess.Popen(telepath)
            telegramApp = OpenWindow('Telegram')
            controlDangMo.append(telegramApp)
            bringToFrontControl(control=telegramApp, tuKhoa='Tele')
            # Đóng cửa sổ explore
            return telegramApp
        except Exception as err:
            traceback.print_exc()
            if err.args[0] in [TelegramError.time_num_out]:
                raise err
            print('Có lỗi xảy ra! Đóng các control đang mở và thử lại')
            time_try = time_try + 1
            for control in controlDangMo:
                close_control(control=control)
            continue


def TimSearchEdit(telegramApp):
    # Điền link vào search
    print('Tìm search edit')
    searchEdit = None
    while searchEdit is None:
        try:
            searchEdit = getChildItem(control=telegramApp, controlType=ControlType.Edit, found_index=1)
            drawOutlineControl(control=searchEdit, color='red')
        except:
            searchEdit = getChildItem(control=telegramApp, controlType=ControlType.Edit, found_index=0)
            drawOutlineControl(control=searchEdit, color='red')
    return searchEdit


def TimChatEdit(telegramApp):
    print('Tìm chat edit')
    chatEdit = None
    while chatEdit is None:
        try:
            searchEdit = getChildItem(control=telegramApp, controlType=ControlType.Edit, found_index=1)
            drawOutlineControl(control=searchEdit, color='red')

            chatEdit = getChildItem(control=telegramApp, controlType=ControlType.Edit, found_index=0)
            drawOutlineControl(control=chatEdit, color='red')
        except:
            return -1
    return chatEdit


def QuayVeBot(telegramApp):
    # Quay trở lại tìm nhấn bot
    searchEdit = TimSearchEdit(telegramApp=telegramApp)
    # Điền vào bot
    try:
        searchEdit.set_text('')
    except:
        searchEdit = TimSearchEdit(telegramApp=telegramApp)
        searchEdit.set_text('')
    try:
        typeKey(control=searchEdit, key='Chumbi Valley Airdrop (New Round)')
    except:
        searchEdit = TimSearchEdit(telegramApp=telegramApp)
        typeKey(control=searchEdit, key='Chumbi Valley Airdrop (New Round)')
    time.sleep(7)
    try:
        typeKeyEnter(control=searchEdit)
    except:
        searchEdit = TimSearchEdit(telegramApp=telegramApp)
        typeKeyEnter(control=searchEdit)


def TimVaVaoTelegramVoiTuKhoa(telegramApp, tuKhoa=''):
    searchEdit = TimSearchEdit(telegramApp=telegramApp)
    typeKey(control=searchEdit, key=tuKhoa)
    time.sleep(10)
    searchEdit = TimSearchEdit(telegramApp=telegramApp)
    typeKeyEnter(control=searchEdit)


def DienVaoChatEditVaNhanEnter(telegramApp, keys=''):
    ChatEdit = TimChatEdit(telegramApp=telegramApp)
    typeKey(control=ChatEdit, key=keys)
    ChatEdit = TimChatEdit(telegramApp=telegramApp)
    typeKeyEnter(control=ChatEdit)


def XoaFilePath(path):
    os.remove(path)


def XoaHetTeleExe():
    for folder in getAllSubDir(fr'{os.getcwd()}\Tele\Tele'):
        filePath = fr'{folder}\Telegram.exe'
        try:
            XoaFilePath(filePath)
        except:
            pass


def XoaFolder(path):
    shutil.rmtree(path, ignore_errors=True)


def DowloadTele(url):
    from urllib.request import urlopen

    file_name = url.split('/')[-1]
    import os
    if os.path.exists(file_name):
        print('File đã tồn tại! Bỏ qua tải về')
        return
    u = urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8) * (len(status) + 1)
        print(status)
    f.close()
    print('Tải về thành công! Đang giải nén')
    extractFile(f'{os.getcwd()}\\{file_size}', out_path=f'{os.getcwd()}\\Tele\\Tele')
    with open('TelePath.txt', 'w') as file:
        for folder in getAllSubDir(fr'{os.getcwd()}\Tele\Tele'):
            file.write(f'{folder}\n')
        file.close()


def DowloadTeleWithChrome(url, driver: WebDriver):
    print('Đi tới trang tải telegram')
    driver.get(url)
    downloads_path = f'{Path.home()}\Downloads'
    print('Xóa hết file đợi download')
    for file in getAllFiles(downloads_path):
        if file.endswith('.crdownload'):
            os.remove(file)

    print('Getting file name')
    fileNameXpath = '//span[@class="uc-name-size"]/a'
    file_Element = driver.find_elements_by_xpath(xpath=fileNameXpath)
    file_name = file_Element[0].text
    print(f'Nhận được {file_name}')

    while not checkIsStartDownload(downloads_path) and not download_wait(downloads_path, filename=file_name, test=True):
        print('Nhấn tải về telegram')
        downloadButtonXpath = '//a[contains(text() , "Download anyway")]'
        clickByXpath(driver=driver, wait=WebDriverWait(driver=driver, timeout=5), click_clickable=True,
                     xpath=downloadButtonXpath)
        time.sleep(10)
    print('Đang đợi tải về')
    file_name_after_check = download_wait(path_to_downloads=downloads_path, filename=file_name)
    print('Tải về thành công! Đang giải nén')
    extractFile(f'{downloads_path}\\{file_name_after_check}', out_path=f'{os.getcwd()}\\Tele\\Tele')
    with open('TelePath.txt', 'w') as file:
        for folder in getAllSubDir(fr'{os.getcwd()}\Tele\Tele'):
            file.write(f'{folder}\n')
        file.close()


def extractFile(path: str, out_path):
    import patoolib
    from pathlib import Path
    Path(out_path).mkdir(parents=True, exist_ok=True)
    patoolib.extract_archive(path, outdir=out_path)


def TaoData(emails: typing.List[str], tws: typing.List[TwitterData], discords: typing.List[DiscordData], telePaths,
            wls):
    data = []
    with open('data.txt', 'w', encoding='utf-8', errors='ignore') as file:
        for email, tw, discord, telePath, wl in zip(emails, tws, discords, telePaths, wls):
            file.write(f'{email}::{tw.username}::{discord.username}::{telePath}::{wl}\n')
            data.append(f'{email}::{tw.username}::{discord.username}::{telePath}::{wl}\n')
        file.close()
    return data


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
