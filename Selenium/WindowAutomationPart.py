import time
import traceback
from Interface.DiscordData import DiscordData
from Interface.Error import ProcessError
from Interface.IDOConfig import IDOConfig
from Interface.TwitterData import TwitterData
from procedure import *
from typing import Union, List
from selenium.webdriver.support.ui import WebDriverWait
from ImageProcessingOCR import solveChallengeTelegram

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


def readDataEmail(EmailPath: str) -> Union[int, List[str]]:
    try:
        with open(EmailPath) as fileData:
            lines = fileData.readlines()
            listEmailData = []
            for line in lines:
                listEmailData.append(line)
            fileData.close()
            return listEmailData
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
        with open(DiscordDataPath, encoding="ISO-8859-1") as fileData:
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


def xoaThongTinEmail(EmailDataPath: str, email: str) -> Union[int]:
    try:
        with open(EmailDataPath) as fileData:
            lines = fileData.readlines()
        with open(EmailDataPath, "w") as f:
            for line in lines:
                if line.strip("\n") != email.strip("\n"):
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
              configData.discord_data_path, configData.wallet_path, configData.gmail_data_path)

        # Nhận để lấy data email
        print(f'Tiến hành đọc data email')
        dataEmail = readDataEmail(configData.gmail_data_path)
        if dataEmail == -1:
            print('Lỗi khi đọc thông tin tài khoản email')
            return

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
        print('Số email:', len(dataEmail))
        print('Số proxy:', len(dataProxy))
        soLanDungIP = 10

        # Kiểm tra xem số thông tin đầu vào bằng nhau hay không
        number_acc = len(dataTwitter)
        if len(dataTwitter) != number_acc or len(dataWallet) != number_acc or len(dataEmail) != number_acc or (
                len(dataProxy) * soLanDungIP) < number_acc or len(
            dataDiscord) != number_acc or soThuMucTelegram < number_acc:
            print(
                'Số thông tin twitter,wallet, email, discord không bằng nhau hoặc số thư mục telegram ít hơn số account đang có hoặc số proxy không đủ để dùng')
            return
        else:
            if soThuMucTelegram > number_acc:
                print('Warning: Số thư mục telegram nhiều hơn số account đang có')
                time.sleep(10)
                print('Tiếp tục chạy')

        # --------------------------------------------
        index = TimIndexTeleChay()  # 58,59 --  Lỗi sesion,60,61 you are not subcribe
        # Xóa các folder không chạy tới
        print('Xóa folder không dùng')
        for i, folderPath in enumerate(dataTelePath):
            if i not in range(index, index + number_acc):
                XoaFolder(folderPath[0:-1])

        index_proxy = 0
        index_SoLanChay = 0
        for email, twitterAcc, discordAcc, wallet_address in zip(dataEmail, dataTwitter, dataDiscord, dataWallet):
            time_try = 0
            index_SoLanChay = index_SoLanChay + 1
            while True:
                try:
                    time_try = time_try + 1
                    if time_try == 2:
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
                    CopyTelegram(telepath=rf'{dataTelePath[index][0:-1]}\Telegram.exe')

                    # Mở telegram ứng với index
                    print('Mở telegram với index')
                    telegramApp = MoTelegramIndex(telepath=rf'{dataTelePath[index][0:-1]}\Telegram.exe')

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
                    WAIT_TIMEOUT = 12
                    print(f'Tạo wait với thời gian chờ {WAIT_TIMEOUT}')
                    wait = WebDriverWait(driver=driver, timeout=WAIT_TIMEOUT)

                    if driver == 1:
                        print('Tạo driver lỗi')
                        return
                    print('Tạo driver thành công')

                    # Tới trang ref
                    driver.get('https://t.me/ChumbiValleyAirdropBot?start=1965360781')

                    # Nhấn chọn open in telegram
                    detectImageAndClickLeftTopNewSingle(imagePath='Image\\OpenInTelegramDestop.png', gioiHan=100)

                    # Thoát chrome
                    quitAllDriver(driver=driver)
                    time.sleep(5)

                    # Vào bot
                    print('Quay về bot')
                    bringToFrontControl(control=telegramApp, tuKhoa='Tele')

                    # Nhấn start
                    print('Nhấn start')
                    clickUntilDisapper(imagePath='Image\\StartButton.png', gioiHan=3)

                    # Lỗi 2 lần
                    print('Đưa explore lên đầu')
                    explore = OpenWindow('Sele')
                    bringToFrontControl(control=explore, tuKhoa='Sele')

                    # Kiểm tra captcha
                    print('Kiểm tra giải toán')
                    result = solveChallengeTelegram(fr'{os.getcwd()}\Image\TelegramChallengeStart.png')

                    # Điền vào edit text
                    if result != -1:
                        DienVaoChatEditVaNhanEnter(telegramApp=telegramApp, keys=result)
                        time.sleep(5)

                    # Nhấn submit detail
                    print('Nhấn submit detail')
                    detectImageAndClickLeftTopNewSingle(imagePath='Image\\SubmitDetail_1.png', gioiHan=10)
                    time.sleep(10)

                    # Điền email
                    print('Điền email')
                    DienVaoChatEditVaNhanEnter(telegramApp=telegramApp, keys=email)
                    time.sleep(10)

                    # Điền twitter
                    print('Điền twitter')
                    DienVaoChatEditVaNhanEnter(telegramApp=telegramApp, keys=twitterAcc.username)
                    time.sleep(10)

                    # Nhấn Skip facebook
                    print('Nhấn Skip Facebook')
                    clickUntilDisapper(imagePath='Image\\Skip_FB.png')

                    # Nhấn Skip discord
                    print('Điền discord username')
                    DienVaoChatEditVaNhanEnter(telegramApp=telegramApp, keys=discordAcc.username)
                    time.sleep(10)

                    # Nhấn No
                    print('Nhấn No Youtube')
                    detectImageAndClickLeftTopNewSingle(imagePath='Image\\No_Button.png', gioiHan=10)

                    # Nhấn No
                    print('Nhấn No twitter')
                    detectImageAndClickLeftTopNewSingle(imagePath='Image\\No_Button.png', gioiHan=10)

                    # Tìm Airdrop Detective
                    print('Tìm Airdrop Detective')
                    TimVaVaoTelegramVoiTuKhoa(telegramApp=telegramApp, tuKhoa='Airdrop Detective')

                    # Nhấn Join
                    print('Nhấn Join')
                    clickUntilDisapper(imagePath='Image\\JoinChannel.png')

                    # Về bot
                    print('Về bot')
                    QuayVeBot(telegramApp=telegramApp)

                    # Nhấn Yes
                    print("Nhấn Yes")
                    clickUntilDisapper(imagePath='Image\\Yes_Button.png')

                    # Điền ví
                    time.sleep(5)
                    print('Điền ví')
                    DienVaoChatEditVaNhanEnter(telegramApp=telegramApp, keys=wallet_address)

                    # # Bỏ qua join
                    # print('Bỏ qua join ! Nhấn skip')
                    # clickUntilDisapper(imagePath='Image\\SkipButton.png')

                    # # Nhấn Complete Air Drop
                    # print('Nhấn Complete Airdrop')
                    # clickUntilDisapper(imagePath='Image\\Complete_Air.png')

                    # Tìm Airdrop Detective 5
                    print('Tìm Airdrop Detective')
                    TimVaVaoTelegramVoiTuKhoa(telegramApp=telegramApp, tuKhoa='Airdrop Detective Community 6')

                    # Nhấn join group
                    print('Nhấn join group')
                    clickUntilDisapper(imagePath='Image\\Join_Group.png')

                    #
                    QuayVeBot(telegramApp=telegramApp)

                    # Nhấn Complete Air Drop lần 2
                    print('Nhấn Complete Airdrop')
                    clickUntilDisapper(imagePath='Image\\Complete_Air.png')

                    #

                    # Kiểm tra thành công
                    if detectImage(imagePath='Image\\Finish.png', gioiHan=20) != -1:
                        # Thành Công ----------------------------------------
                        print('Thành Công')
                        print('Ghi lại vào file text result')
                        with open('result.txt', 'a') as file:
                            file.writelines(f'{twitterAcc.username}:1\n')
                        captureScreen(number=f'success_{index}')
                    else:
                        print('Không thành công')
                        with open('result.txt', 'a') as file:
                            file.writelines(f'{twitterAcc.username}:0\n')
                        captureScreen(number=f'failed_{index}')
                    # Nhấn chọn bot
                    print('Xóa các thông tin')

                    xoaThongTinTwitter(TwitterDataPath=configData.twitter_data_path,
                                       username_delete=twitterAcc.username)
                    XoaDataWallet(WalletPath=configData.wallet_path,
                                  wallet_delete=wallet_address)

                    xoaThongTinDiscord(DiscordDataPath=configData.discord_data_path,
                                       discord_delete_ID=discordAcc.username)

                    xoaThongTinEmail(EmailDataPath=configData.gmail_data_path, email=email)

                    # Đóng hết telegram
                    try:
                        print('Đóng hết Telegram')
                        os.system("taskkill /f /im Telegram.exe")
                    except:
                        pass
                    time.sleep(2)

                    print('Xóa folder telegram')
                    XoaFolder(rf'{dataTelePath[index][0:-1]}')

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

                        xoaThongTinEmail(EmailDataPath=configData.gmail_data_path, email=email)

                        # Đóng hết telegram
                        try:
                            print('Đóng hết Telegram')
                            os.system("taskkill /f /im Telegram.exe")
                        except:
                            pass
                        time.sleep(2)

                        print('Xóa folder telegram')
                        XoaFolder(rf'{dataTelePath[index][0:-1]}')

                        # XoaDataTelegram(TelegramPath=configData.telegram_data_path, telegram_delete=telegramUserName)
                        print('Chuyển sang acc khác')
                        index = index + 1
                        break
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
