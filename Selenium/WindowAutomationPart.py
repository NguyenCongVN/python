import traceback
from Interface.DiscordData import DiscordData
from Interface.Error import ProcessError
from Interface.IDOConfig import IDOConfig
from Interface.TwitterData import TwitterData
from procedure import *
from typing import Union, List

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
                idoConfig.webdriverPath = f'{CurrentDirectory}\\{value}'
            if name == 'chrome_path':
                idoConfig.chrome_path = f'{CurrentDirectory}\\{value}'
            if name == 'twitter_data_path':
                idoConfig.twitter_data_path = f'{CurrentDirectory}\\{value}'
            if name == 'gmail_data_path':
                idoConfig.gmail_data_path = f'{CurrentDirectory}\\{value}'
            if name == 'chrome_folder_path':
                idoConfig.chrome_folder_path = f'{CurrentDirectory}\\{value}'
            if name == 'proxy_api_path':
                idoConfig.proxy_path = f'{CurrentDirectory}\\{value}'
            if name == 'wallet_path':
                idoConfig.wallet_path = f'{CurrentDirectory}\\{value}'
            if name == 'anti_captcha_path':
                idoConfig.anti_captcha_path = f'{CurrentDirectory}\\{value}'
            if name == 'telegram_data_path':
                idoConfig.telegram_data_path = f'{CurrentDirectory}\\{value}'
            if name == 'proxy_data_path':
                idoConfig.telegram_data_path = f'{CurrentDirectory}\\{value}'
            if name == 'discord_data_path':
                idoConfig.discord_data_path = f'{CurrentDirectory}\\{value}'
            if name == 'proxy_data_path':
                idoConfig.proxy_data_path = f'{CurrentDirectory}\\{value}'
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


def readDataDiscord(DiscordDataPath: str) -> Union[int, List[DiscordData]]:
    try:
        with open(DiscordDataPath) as fileData:
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


def xoaThongTinDiscord(DiscordDataPath: str, discord_delete_ID: str) -> Union[int]:
    try:
        with open(DiscordDataPath) as fileData:
            lines = fileData.readlines()
        with open(DiscordDataPath, "w") as f:
            for line in lines:
                if line.strip("\n") != discord_delete_ID.strip("\n"):
                    f.write(line)
            fileData.close()
    except Exception as err:
        print(err)
        traceback.print_exc()
        return -1


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
        import os
        files = folders = 0
        for _, dirnames, filenames in os.walk(fr'{os.getcwd()}\2936 Tele ChưaDùng\ChưaDùng'):
            files += len(filenames)
            folders += len(dirnames)

        soThuMucTelegram = folders

        print('Số thư mục telegram:', soThuMucTelegram)
        print('Số tài khoản Twitter:', len(dataTwitter))
        print('Số Wallet:', len(dataWallet))
        print('Số discord:', len(dataDiscord))

        # Kiểm tra xem số thông tin đầu vào bằng nhau hay không
        number_acc = len(dataTwitter)
        if len(dataTwitter) != number_acc or len(dataWallet) != number_acc or len(
                dataProxy) != number_acc or len(dataDiscord) != number_acc or soThuMucTelegram < number_acc:
            print(
                'Số thông tin twitter,wallet, discord và proxy không bằng nhau hoặc số thư mục telegram ít hơn số account đang có')
            return
        else:
            if soThuMucTelegram > number_acc:
                print('Warning: Số thư mục telegram nhiều hơn số account đang có')
                time.sleep(10)
                print('Tiếp tục chạy')

        # --------------------------------------------

        # Khởi tạo list proxy
        # Proxy TinSoft
        # listProxy = list()
        # for proxy in proxyApi:
        #     item6 = TinSoftProxy(proxy, typeProxy=0, limit_theads_use=0, location_id=0)
        #     listProxy.append(item6)
        acc_ip_change = 0
        index = 0
        for twitterAcc, discordAcc, wallet_address, proxy in zip(dataTwitter, dataDiscord, dataWallet, dataProxy):
            time_try = 0
            while True:
                try:
                    time_try = time_try + 1
                    if time_try == 2:
                        print('Quá số lần chạy process')
                        raise Exception(ProcessError.time_try_error)

                    # Lấy kiểm tra proxy
                    print('Kiểm tra proxy')

                    # Đổi proxy với proxifier
                    ChangeProxyWithProxifier(proxy=proxy, is_auth=True)

                    #
                    print('Đợi 5s')
                    time.sleep(5)

                    acc_ip_change = acc_ip_change + 1

                    print('Tiến hành vào thủ tục')

                    # thủ tục chính

                    # -------------------------------------------
                    # copy telegram.exe
                    print('Copy telegram')
                    CopyTelegram()

                    # Mở telegram ứng với index
                    print('Mở telegram với index')
                    telegramApp = MoTelegramIndex(index=index)

                    # Vào bot
                    print('Quay về bot')
                    QuayVeBot(telegramApp=telegramApp)

                    # # Nhấn start
                    # print('Nhấn start')
                    # StartElemt = telegramApp.GroupBox18
                    # click_input(StartElemt)

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
                    detectImageAndClickLeftTopNewSingle(imagePath='Image\\ContinueButton.png')

                    # Điền link vào channel
                    print('Vào channel')
                    TimVaVaoTelegramVoiTuKhoa(telegramApp=telegramApp, tuKhoa='https://t.me/chumbivalleychannel')

                    # nhấn join
                    print('Nhấn Join')
                    detectImageAndClickLeftTopNewSingle(imagePath='Image\\JoinButton.png')

                    # Quay lại bot
                    print('Quay về bot')
                    QuayVeBot(telegramApp=telegramApp)

                    # Nhấn Done
                    print('Nhấn Done')
                    detectImageAndClickLeftTopNewSingle(imagePath='Image\\DoneButton.png')

                    # print_control_identifiers(control=StartElemt)

                    # Nhấn chọn bot

                    print('Xóa các thông tin')

                    time.sleep(5)
                    break
                except Exception as err:
                    print(err)
                    # # Lỗi phải chạy lại tài khoản khác
                    # if err.args[0] in [ProcessError.time_try_error]:
                    #     # ghi lại lí do lỗi
                    #     print(err.args[0].value)
                    #     print('Ghi lại vào file text result')
                    #     with open('result.txt', 'a') as file:
                    #         file.writelines(f'{twitterAcc.username}:0:{err}\n')
                    #
                    #     print('Xóa các thông tin')
                    #     xoaThongTinTwitter(TwitterDataPath=configData.twitter_data_path,
                    #                        username_delete=twitterAcc.username)
                    #     XoaDataWallet(WalletPath=configData.wallet_path,
                    #                   wallet_delete=wallet_address)
                    #     xoaThongTinDiscord(DiscordDataPath=configData.discord_data_path,
                    #                        discord_delete_ID=discordAcc.username)
                    #     # XoaDataTelegram(TelegramPath=configData.telegram_data_path, telegram_delete=telegramUserName)
                    #     print('Chuyển sang acc khác')
                    #     # try:
                    #     #     quitAllDriver(driver=driver)
                    #     # except:
                    #     #     pass
                    #     # time.sleep(5)
                    #     # break
                    # # Lỗi chạy lại tài khoản hiện tại
                    # # if err.args[0] in [LoginTwitterEror.open_div_time_num_out, LoginTwitterEror.time_out,
                    # #                    FollowTwiiterError.follow_twitter_time_num_out, CaptchaCloudFareError.time_out,
                    # #                    EnterWalletError.enter_wallet_time_num_out]:
                    # #     print('Chạy lại tài khoản hiện tại')
                    # #     quitAllDriver(driver=driver)
                    # #     time.sleep(5)
                    # # else:
                    # #     # Lỗi khác
                    # #     print('Chạy lại tài khoản hiện tại')
                    # #     quitAllDriver(driver=driver)
                    # #     time.sleep(5)
    except Exception as err:
        print(err)
        traceback.print_exc()
        print('Có lỗi lạ xảy ra! Thoát')
        return


if __name__ == "__main__":
    main()
