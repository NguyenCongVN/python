import traceback
from Interface.DiscordData import DiscordData
from Interface.Error import ProcessError
from Interface.IDOConfig import IDOConfig
from Interface.TwitterData import TwitterData
from procedure import *
from typing import Union, List
from selenium.webdriver.support.ui import WebDriverWait

pyautogui.FAILSAFE = False
cap = 0


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


def readDataProxy(ProxyPath: str) -> Union[int, List[str]]:
    try:
        with open(ProxyPath) as fileData:
            lines = fileData.readlines()
            listProxyData = []
            for line in lines:
                listProxyData.append(line)
            fileData.close()
            return listProxyData
    except Exception as err:
        print(err)
        traceback.print_exc()
        return -1


def readConfig() -> IDOConfig:
    """
    Đọc config
    :rtype: IDOConfig
    """
    with open('config.conf') as configFile:
        idoConfig = IDOConfig('', '', '', '', '', '', '', '', '', '', '')
        lines = configFile.readlines()
        CurrentDirectory = os.getcwd()
        for index, line in enumerate(lines):
            if index != len(lines) - 1:
                line = line[0:-1]
            [name, value] = line.split('=')
            if name == 'webdriver':
                if '\\' not in value:
                    idoConfig.webdriverPath = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.webdriverPath = value
            if name == 'chrome_path':
                if '\\' not in value:
                    idoConfig.chrome_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.chrome_path = value
            if name == 'twitter_data_path':
                if '\\' not in value:
                    idoConfig.twitter_data_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.twitter_data_path = value
            if name == 'gmail_data_path':
                if '\\' not in value:
                    idoConfig.gmail_data_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.gmail_data_path = value
            if name == 'chrome_folder_path':
                if '\\' not in value:
                    idoConfig.chrome_folder_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.chrome_folder_path = value
            if name == 'proxy_api_path':
                if '\\' not in value:
                    idoConfig.proxy_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.proxy_path = value
            if name == 'wallet_path':
                if '\\' not in value:
                    idoConfig.wallet_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.wallet_path = value
            if name == 'anti_captcha_path':
                if '\\' not in value:
                    idoConfig.anti_captcha_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.anti_captcha_path = value
            if name == 'telegram_data_path':
                if '\\' not in value:
                    idoConfig.telegram_data_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.telegram_data_path = value
            if name == 'proxy_data_path':
                if '\\' not in value:
                    idoConfig.telegram_data_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.telegram_data_path = value
            if name == 'discord_data_path':
                if '\\' not in value:
                    idoConfig.discord_data_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.discord_data_path = value
            if name == 'proxy_data_path':
                if '\\' not in value:
                    idoConfig.proxy_data_path = f'{CurrentDirectory}\\{value}'
                else:
                    idoConfig.proxy_data_path = value
        if idoConfig.webdriverPath == '' or idoConfig.chrome_path == '' or idoConfig.twitter_data_path == '' \
                or idoConfig.chrome_folder_path == '' or idoConfig.proxy_path == '' or idoConfig.gmail_data_path == '' \
                or idoConfig.wallet_path == '' or idoConfig.anti_captcha_path == '' or idoConfig.telegram_data_path == '' or idoConfig.discord_data_path == '' \
                or idoConfig.proxy_data_path == '':
            return 1
        else:
            return idoConfig


def readDataTwitter(TwitterDataPath: str) -> Union[List[TwitterData], int]:
    """
    :param TwitterDataPath: Đường dẫn tới file data
    :return:
    """
    try:
        with open(TwitterDataPath) as fileData:
            lines = fileData.readlines()
            listTwitterData = []
            for line in lines:
                dataLine = line
                twitterData = TwitterData(username=dataLine[0:-1], password='', emailDangKiIDO='')
                listTwitterData.append(twitterData)
            fileData.close()
            return listTwitterData
    except Exception as err:
        print(err)
        traceback.print_exc()
        return -1


def readDataWallet(WalletPath: str) -> Union[int, List[str]]:
    try:
        with open(WalletPath) as fileData:
            lines = fileData.readlines()
            listWalletData = []
            for line in lines:
                listWalletData.append(line)
            fileData.close()
            return listWalletData
    except Exception as err:
        print(err)
        traceback.print_exc()
        return -1


def readDataTelePath(TelePath: str) -> Union[int, List[str]]:
    try:
        with open(TelePath) as fileData:
            lines = fileData.readlines()
            listTeleData = []
            for line in lines:
                listTeleData.append(line)
            fileData.close()
            return listTeleData
    except Exception as err:
        print(err)
        traceback.print_exc()
        return -1


def readDataDiscord(DiscordDataPath: str) -> Union[int, List[DiscordData]]:
    try:
        with open(DiscordDataPath, encoding="utf8") as fileData:
            lines = fileData.readlines()
            listDiscordData = []
            for line in lines:
                dataLine = line
                discordData = DiscordData(username=dataLine[0:-1], password='', emailDiscord='')
                listDiscordData.append(discordData)
            fileData.close()
            return listDiscordData
    except Exception as err:
        print(err)
        traceback.print_exc()
        return -1


def xoaThongTinTwitter(TwitterDataPath: str, username_delete: str) -> Union[int]:
    try:
        with open(TwitterDataPath) as fileData:
            lines = fileData.readlines()
            with open(TwitterDataPath, "w") as f:
                for line in lines:
                    if line.strip("\n") != username_delete.strip("\n"):
                        f.write(line)
                fileData.close()
    except Exception as err:
        print(err)
        traceback.print_exc()
        return -1


def XoaDataWallet(WalletPath: str, wallet_delete: str) -> Union[int, List[str]]:
    try:
        with open(WalletPath) as fileData:
            lines = fileData.readlines()
            with open(WalletPath, "w") as f:
                for line in lines:
                    if line.strip("\n") != wallet_delete.strip("\n"):
                        f.write(line)
                    fileData.close()
    except Exception as err:
        print(err)
        traceback.print_exc()
        return -1


def XoaDataProxy(Proxy_Path: str, proxy_delete: str) -> Union[int, List[str]]:
    try:
        with open(Proxy_Path) as fileData:
            lines = fileData.readlines()
            with open(Proxy_Path, "w") as f:
                for line in lines:
                    if line.strip("\n") != proxy_delete.strip("\n"):
                        f.write(line)
                    fileData.close()
    except Exception as err:
        print(err)
        traceback.print_exc()
        return -1


def xoaThongTinDiscord(DiscordDataPath: str, discord_delete_ID: str) -> Union[int]:
    try:
        with open(DiscordDataPath, encoding="utf8") as fileData:
            lines = fileData.readlines()
        with open(DiscordDataPath, "w", encoding="utf8") as f:
            for line in lines:
                if line.strip("\n") != discord_delete_ID.strip("\n"):
                    f.write(line)
            fileData.close()
    except Exception as err:
        print(err)
        traceback.print_exc()
        return -1


def TimIndexTeleChay():
    with open('index.txt') as indexFile:
        index = indexFile.read()
        indexFile.close()
        return int(index)


def main():
    try:
        # Khởi tạo --------------------------------------------
        print('Tiến hành đọc file config')
        configData = readConfig()
        if configData == 1:
            print('Lỗi file config')
            return
        print('Đọc file config thành công')

        print(configData.twitter_data_path, configData.proxy_data_path,
              configData.discord_data_path, configData.wallet_path)

        # Nhận để lấy data twitter
        print(f'Tiến hành đọc data twitter')
        dataTwitter = readDataTwitter(configData.twitter_data_path)
        if dataTwitter == -1:
            print('Lỗi khi đọc thông tin tài khoản twitter')
            return

        # Đọc thông tin địa chỉ ví
        print('Tiến hành đọc địa chỉ ví')
        dataWallet = readDataWallet(configData.wallet_path)
        if dataWallet == -1:
            print('Lỗi khi đọc thông tin địa chỉ ví')
            return

        # Đọc thông tin tele path
        print('Tiến hành đọc tele path')
        dataTelePath = readDataTelePath('TelePath.txt')
        if dataTelePath == -1:
            print('Lỗi khi đọc thông tin tele path')
            return

        # Đọc thông tin proxy
        print('Tiến hành đọc proxy')
        dataProxy = readDataProxy(configData.proxy_data_path)
        if dataProxy == -1:
            print('Lỗi khi đọc thông tin proxy')
            return

        # Đọc thông tin discord
        print('Tiến hành đọc discord')
        dataDiscord = readDataDiscord(configData.discord_data_path)
        if dataDiscord == -1:
            print('Lỗi khi đọc thông tin discord')
            return

        # Kiểm tra số thư mục trong folder
        soThuMucTelegram = len(getAllSubDir(fr'{os.getcwd()}\Tele\Tele'))

        print('Số thư mục telegram:', soThuMucTelegram)
        print('Số tài khoản Twitter:', len(dataTwitter))
        print('Số Wallet:', len(dataWallet))
        print('Số discord:', len(dataDiscord))

        soLanDungIP = 2

        # Kiểm tra xem số thông tin đầu vào bằng nhau hay không
        number_acc = len(dataTwitter)
        if len(dataTwitter) != number_acc or len(dataWallet) != number_acc or len(
                dataProxy) * soLanDungIP < number_acc or len(
            dataDiscord) != number_acc or soThuMucTelegram < number_acc:
            print(
                'Số thông tin twitter,wallet, discord không bằng nhau hoặc số thư mục telegram ít hơn số account đang có hoặc số proxy không đủ để dùng')
            return
        else:
            if soThuMucTelegram > number_acc:
                print('Warning: Số thư mục telegram nhiều hơn số account đang có')
                time.sleep(10)
                print('Tiếp tục chạy')

        # --------------------------------------------
        index = TimIndexTeleChay()  # 58,59 --  Lỗi sesion,60,61 you are not subcribe
        index_proxy = 0
        index_SoLanChay = 0
        for twitterAcc, discordAcc, wallet_address in zip(dataTwitter, dataDiscord, dataWallet):
            time_try = 0
            while True:
                try:
                    time_try = time_try + 1
                    if time_try == 3:
                        print('Quá số lần chạy process')
                        raise Exception(ProcessError.time_try_error)

                    # Đóng hết telegram
                    try:
                        print('Đóng hết Telegram')
                        os.system("taskkill /f /im Telegram.exe")
                    except:
                        pass
                    time.sleep(2)
                    print('Xóa hết file telegram')
                    XoaHetTeleExe()
                    index_SoLanChay = index_SoLanChay + 1
                    if index_SoLanChay > soLanDungIP:
                        # Đổi proxy với proxifier
                        print('Đổi sang proxy mới')
                        print('Xóa proxy hiện tại')
                        XoaDataProxy(configData.proxy_data_path, proxy_delete=dataProxy[index_proxy])
                        index_proxy = index_proxy + 1
                        index_SoLanChay = 0
                    # Lấy kiểm tra proxy
                    print('Kiểm tra proxy')
                    while not CheckConnectionToProxy(proxy=dataProxy[index_proxy], num_check=3):
                        print('Nâng proxy')
                        print('Xóa proxy hiện tại')
                        XoaDataProxy(configData.proxy_data_path, proxy_delete=dataProxy[index_proxy])
                        index_proxy = index_proxy + 1
                        index_SoLanChay = 0
                    ChangeProxyWithProxifier(proxy=dataProxy[index_proxy], is_auth=True)

                    #
                    print('Đợi 3s')
                    time.sleep(3)

                    print('Tiến hành vào thủ tục')

                    # thủ tục chính

                    # -------------------------------------------
                    # copy telegram.exe
                    print('Copy telegram')
                    CopyTelegram()

                    # Mở telegram ứng với index
                    print('Mở telegram với index')
                    telegramApp = MoTelegramIndex(telepath=dataTelePath[index][0:-1])

                    # Nhấn Hide
                    print('Nhấn HIDE')
                    clickUntilDisapper(imagePath='Image\\HideButton.png', gioiHan=2)

                    # # Minimize
                    # telegramApp.minimize()

                    # Mở chrome và vào link ref
                    # xóa hết data trước khi đăng kí
                    print('xóa hết data')
                    deleteContentFolder(f'{configData.chrome_folder_path}\Data\profile')
                    # Tạo driver
                    print('Đang tạo driver')
                    driver = open_driver(chromePath=configData.chrome_path, driverPath=configData.webdriverPath,
                                         type_proxy=0,
                                         proxy=dataProxy[index_proxy][0:-1],
                                         anti_captcha=None,
                                         chrome_folder_path=configData.chrome_folder_path)
                    driver.set_page_load_timeout(10)
                    WAIT_TIMEOUT = 12
                    print(f'Tạo wait với thời gian chờ {WAIT_TIMEOUT}')
                    wait = WebDriverWait(driver=driver, timeout=WAIT_TIMEOUT)

                    if driver == 1:
                        print('Tạo driver lỗi')
                        return
                    print('Tạo driver thành công')

                    # Tới trang ref
                    driver.get('https://t.me/CHUMBIVALLEY_Bot?start=r04634236800')

                    # Nhấn chọn open in telegram
                    clickUntilDisapper(imagePath='Image\\OpenInTelegramDestop.png')

                    # Thoát chrome
                    quitAllDriver(driver=driver)
                    time.sleep(5)

                    # Vào bot
                    print('Quay về bot')
                    bringToFrontControl(control=telegramApp, tuKhoa='Tele')

                    # # Điền link ref
                    # print('Vào link ref')
                    # TimVaVaoTelegramVoiTuKhoa(telegramApp=telegramApp, tuKhoa='https://t.me/CHUMBIVALLEY_Bot?start=r04634236800')

                    # Nhấn start
                    print('Nhấn start')
                    clickUntilDisapper(imagePath='Image\\StartButton.png')

                    # Vào Group và join
                    print('Tìm vào group')
                    TimVaVaoTelegramVoiTuKhoa(telegramApp=telegramApp, tuKhoa='@chumbivalley02')

                    # nhấn join
                    print('Nhấn join')
                    detectImageAndClickLeftTopNewSingle(imagePath='Image\\JoinButton.png')

                    # Quay trở lại tìm nhấn bot
                    print('Quay về bot')
                    QuayVeBot(telegramApp=telegramApp)

                    # Nhấn check xem hoàn thành chưa
                    print('Nhấn check')
                    detectImageAndClickLeftTopNewSingle(imagePath='Image\\CheckButton.png')

                    # Nhấn continue
                    print('Đợi 5s rồi nhấn continue')
                    time.sleep(5)
                    clickUntilDisapper(imagePath='Image\\ContinueButton.png')

                    # Điền link vào channel
                    print('Vào channel')
                    TimVaVaoTelegramVoiTuKhoa(telegramApp=telegramApp, tuKhoa='Chumbi Valley - Announcements')

                    # nhấn join
                    print('Nhấn Join')
                    clickUntilDisapper(imagePath='Image\\JoinButton.png')

                    # Quay lại bot
                    print('Quay về bot')
                    QuayVeBot(telegramApp=telegramApp)

                    # Submit Detail
                    print('Nhấn submit detail')
                    clickUntilDisapper(imagePath='Image\\SubmitDetailButton.png')

                    # Nhấn Done
                    print('Nhấn Done')
                    clickUntilDisapper(imagePath='Image\\DoneButton.png')

                    time.sleep(5)

                    # Điền twitter username
                    print('Điền twitter username')
                    DienVaoChatEditVaNhanEnter(telegramApp=telegramApp, keys=twitterAcc.username)

                    # Điền discord ID
                    print('Đợi 5s')
                    time.sleep(10)
                    print('Điền discord ID')
                    DienVaoChatEditVaNhanEnter(telegramApp=telegramApp, keys=discordAcc.username)

                    # Điền địa chỉ ví
                    print('Đợi 5s')
                    time.sleep(10)
                    print('Điền wallet')
                    DienVaoChatEditVaNhanEnter(telegramApp=telegramApp, keys=wallet_address)

                    # Kiểm tra thành công
                    if detectImage(imagePath='Image\\DontForget.png', gioiHan=20) == 0:
                        # Thành Công ----------------------------------------
                        print('Thành Công')
                        print('Ghi lại vào file text result')
                        with open('result.txt', 'a') as file:
                            file.writelines(f'{twitterAcc.username}:1\n')
                        captureScreen(number=f'success_{index}')
                    else:
                        print('Không thành công')
                        captureScreen(number=f'failed_{index}')

                    # Nhấn chọn bot
                    print('Xóa các thông tin')

                    xoaThongTinTwitter(TwitterDataPath=configData.twitter_data_path,
                                       username_delete=twitterAcc.username)
                    XoaDataWallet(WalletPath=configData.wallet_path,
                                  wallet_delete=wallet_address)

                    xoaThongTinDiscord(DiscordDataPath=configData.discord_data_path,
                                       discord_delete_ID=discordAcc.username)

                    index = index + 1
                    time.sleep(5)
                    break
                except Exception as err:
                    print(err)
                    traceback.print_exc()
                    # Lỗi phải chạy lại tài khoản khác
                    if err.args[0] in [ProcessError.time_try_error]:
                        # ghi lại lí do lỗi
                        print(err.args[0].value)
                        print('Ghi lại vào file text result')
                        with open('result.txt', 'a') as file:
                            file.writelines(f'{twitterAcc.username}:0:{err}\n')
                            print('Lưu lại ảnh lỗi')
                            captureScreen(number=f'failed_{index}')
                        print('Xóa các thông tin')
                        xoaThongTinTwitter(TwitterDataPath=configData.twitter_data_path,
                                           username_delete=twitterAcc.username)
                        XoaDataWallet(WalletPath=configData.wallet_path,
                                      wallet_delete=wallet_address)
                        xoaThongTinDiscord(DiscordDataPath=configData.discord_data_path,
                                           discord_delete_ID=discordAcc.username)
                        # XoaDataTelegram(TelegramPath=configData.telegram_data_path, telegram_delete=telegramUserName)
                        print('Chuyển sang acc khác')
                        index = index + 1
                        # try:
                        #     quitAllDriver(driver=driver)
                        # except:
                        #     pass
                        # time.sleep(5)
                        # break
                    # Lỗi chạy lại tài khoản hiện tại
                    # if err.args[0] in [LoginTwitterEror.open_div_time_num_out, LoginTwitterEror.time_out,
                    #                    FollowTwiiterError.follow_twitter_time_num_out, CaptchaCloudFareError.time_out,
                    #                    EnterWalletError.enter_wallet_time_num_out]:
                    #     print('Chạy lại tài khoản hiện tại')
                    #     quitAllDriver(driver=driver)
                    #     time.sleep(5)
                    # else:
                    #     # Lỗi khác
                    #     print('Chạy lại tài khoản hiện tại')
                    #     quitAllDriver(driver=driver)
                    #     time.sleep(5)
    except Exception as err:
        print(err)
        traceback.print_exc()
        print('Có lỗi lạ xảy ra! Thoát')
        return


if __name__ == "__main__":
    main()
