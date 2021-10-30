import time
import time
import traceback
from subprocess import Popen

import pyautogui
from pywinauto import Desktop

from InteractHelper import LayCacTenWindow
from InteractHelper import waitThreadAndJoin, detectImageAndClickCenter, \
    detectImageAndClickLeftTopNew, DoiThoiGian, detectAllImage, clickWithLocation

pyautogui.FAILSAFE = False
cap = 0


# Chọn máy với tên
def chooseComputerWithName(window, tenMay):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        try:
            if str(tenMay) in str(item.texts()):
                print('Đang chọn máy {check}'.format(check=tenMay))
                # Nhấp chuột trái chọn máy
                item.click_input(button='left', coords=(None, None))
        except Exception as err:
            print(err)
            print('Có lỗi xảy ra {err} trong quá trình chọn máy'.format(err=err))


# Mở Remote Destop
def OpenWindow(path, tuKhoa):
    Popen(path, shell=True)
    dlg = None
    # Đợi 5s để cửa sổ mở ra hoàn toàn
    waitThreadAndJoin(5)

    #
    tenCacWindow = LayCacTenWindow()

    for tenWindow in tenCacWindow:
        if tuKhoa in tenWindow:
            print('Thấy cửa sổ khớp {tenWindow}'.format(tenWindow=tenWindow))
            dlg = Desktop(backend="uia")[tenWindow]
            break
    dlg.wait('visible')

    # Trả về cửa sổ sau khi đã mở thành công
    return dlg


# Start Computer theo khoảng
def startComputer(window, gioiHanMay):
    # Đếm số máy mở
    count = 0
    # Lấy treeItems từ các
    TreeItems = window.TreeView.TreeItem
    # Lặp trong các item nằm trong cây
    for item in TreeItems.descendants():
        if count == gioiHanMay:
            break
        else:
            count = count + 1
        print('Đang mở máy {check}'.format(check=item.texts()))
        # Nhấp chuột 2 lần vào item máy tính
        item.double_click_input(button='left', coords=(None, None))


# Copy một file từ trong máy
def copyFile(path, fileName):
    import subprocess
    # mở explorer và chọn path
    subprocess.Popen(r'explorer /select,"{path}"'.format(path=path))
    # Đợi 5s để explorer sẵn sàng
    waitThreadAndJoin(5)
    #
    dlg = Desktop(backend="uia")['Google Drive']
    # Để cửa sổ lên đầu
    dlg.minimize()
    dlg.restore()
    # Chọn file trong cửa sổ explore với path đã mở
    file = dlg[fileName]
    file.click_input()
    # Nhấn Ctrl+C
    file.type_keys('^c')


# paste file
def pasteFile(window, tenMay):
    TreeItems = window.TreeItem
    for item in TreeItems.descendants():
        if str(tenMay) in str(item.texts()):
            print('pasting computer {check}'.format(check=tenMay))
            item.click_input(button='left', coords=(None, None))
            try:
                staticPanel = window['Input Capture WindowPane']
                # staticPanel.move_mouse_input(coords=(400, 400))
                staticPanel.double_click_input(button='left', coords=(1500, 500))
                staticPanel.type_keys('^v')
            except:
                pass
            break


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


def tuoiCay(soLanTuoi, soMay, gioiHan=5):
    lanThu = 0
    while True:
        result = detectImageAndClickLeftTopNew('E:\python\Selenium\PhotosGame\TuoiNuoc.png', dichX=10, dichY=10,
                                               gioiHan=5)
        # Nếu như result = 0 -> Tìm thấy
        # nếu như result = 1 -> không tìm thấy
        if result == 0:
            print('Tìm thấy cây chưa tưới. Đã tiến hành tưới')
            soLanTuoi[soMay] = soLanTuoi[soMay] + 1
            print(f'Số lần tưới thành công {soLanTuoi[soMay]}')
            if soLanTuoi[soMay] == 15:
                print('Đã đủ lượt tưới ! Thoát')
                return 1
            return 0
        else:
            print('Không tìm thấy cây cần tưới ! Thử kéo xuống dưới')
            # Kéo xuống dưới 70
            pyautogui.scroll(-70)
            lanThu = lanThu + 1
            if lanThu == gioiHan:
                print('Vượt quá số lần thử! Bỏ qua')
                return 1


def XuLyMainProcess(remoteWindow, gioiHanMay):
    # Cho rằng đang ở màn hình: Destop
    # 1. Chọn folder để vào telegram
    # 2. Chạy telegram.exe
    # 3. Search Link Bot
    # 4. Start Bot
    # 5. ......

    # 1. Chọn folder để vào telegram
    count = 0
    # Lấy treeItems từ các
    TreeItems = remoteWindow.TreeView.TreeItem
    # Lặp trong các item nằm trong cây
    for item in TreeItems.descendants():
        if count == gioiHanMay:
            break
        else:
            count = count + 1
        # Delay để đợi remote window sẵn sàng
        DoiThoiGian(3)
        print('Đang mở máy {check}'.format(check=item.texts()))
        # Nhấp chuột 1 lần vào item máy tính
        item.click_input(button='left', coords=(None, None))

        # Đợi 2s để remote destop load
        DoiThoiGian(2)

        # Tìm vị trí tất cả các folder
        print('Tìm vị trí tất cả các folder')
        folderLocations = detectAllImage(r'E:\python\Selenium\folderTelegram\folder.png')

        print('foler Locations ', folderLocations)

        # Mở folder
        print('Đang mở folder đầu tiên')
        for location in folderLocations:
            print('Location : ', location)
            clickWithLocation(location)

    #     # Đợi 5s để chrome tắt hẳn
    #     DoiThoiGian(5)
    #
    #     # Mở lại google chrome
    #     print('Mở lại google chrome')
    #     detectImageAndClickLeftTopNew('E:\python\Selenium\PhotosGame\MoChrome.png', dichX=2, dichY=3)
    #
    #     # Đợi 5s để google chrome mở
    #     DoiThoiGian(5)
    #
    #     # Nhập link
    #     print('Đang nhập link')
    #     detectImageAndClickLeftTopNew(r'E:\python\Selenium\PhotosGame\NhapUrl.png', dichX=40, dichY=20)
    #
    #     # Điền Link
    #     print('Đang điền link')
    #     copyStringToClipboard('blockfarm.club')
    #     DoiThoiGian(2)
    #     print('Paste và Enter')
    #     pyautogui.hotkey('ctrl', 'v')
    #     pyautogui.press('enter')
    #
    #     # Nhấn Login
    #     print('Nhấn Login')
    #     detectImageAndClickLeftTopNew(r'E:\python\Selenium\PhotosGame\LoginGame.png', dichX=20, dichY=20)
    #
    #     # Đợi 5s
    #     DoiThoiGian(5)
    #
    #     # Vào Farm
    #     print('Nhấn vào Farm')
    #     detectImageAndClickLeftTopNew(r'E:\python\Selenium\PhotosGame\farm.png', dichX=20, dichY=20)
    #
    #     # Đợi 5s
    #     DoiThoiGian(5)
    #
    #     # Kiểm tra xem MetaMask hiện hay không
    #     print('Kiểm tra MetaMask')
    #
    #     # Nếu như 0 -> Có hiện
    #     # Nếu như 1 -> Không hiện
    #     while detectImage(r'E:\python\Selenium\PhotosGame\CheckMetaMask.png', gioiHan=5) == 0:
    #         print('Có xuất hiện metamask ! Hãy đăng nhập!')
    #
    #     print('Đã tắt metamask ! Tiếp tục')
    #
    #     # Nhấn vào map
    #     print('Nhấn vào maps')
    #     detectImageAndClickLeftTopNew('E:\python\Selenium\PhotosGame\maps.png', dichX=20, dichY=20)
    #
    # # --------------------------------------------------------------------------------------------------
    #
    # # 2. Tới phần mở world map
    # # Lặp trong các item nằm trong cây
    # print('Tiến hành mở world map')
    # for i in range(15):
    #     for link in linkWorldMap:
    #         while True:
    #             vaoLinkMoi = False
    #             count = 0
    #             for item in TreeItems.descendants():
    #                 if count == gioiHanMay:
    #                     print('Xong đợt 1 ! Đợi 30s trước khi tiếp tục')
    #                     DoiThoiGian(30)
    #                 else:
    #                     count = count + 1
    #                 # Delay để đợi remote window sẵn sàng
    #                 print('Đợi 3s để đợi remote window sẵn sàng')
    #                 time.sleep(3)
    #                 print('Đang chọn máy {check}'.format(check=item.texts()))
    #                 # Nhấp chuột 1 lần vào item máy tính
    #                 item.click_input(button='left', coords=(None, None))
    #
    #                 # Đợi 5s để remote destop load
    #                 DoiThoiGian(5)
    #                 # Vào wold map
    #                 print('Nhấn chọn world map')
    #                 detectImageAndClickLeftTopNew('E:\python\Selenium\PhotosGame\worldmap.png', dichX=20, dichY=20)
    #
    #                 # Đợi 5s
    #                 DoiThoiGian(5)
    #
    #                 # Bắt đầu vào link với world map
    #                 print('Vào link world map')
    #
    #                 # Đợi 5s
    #                 DoiThoiGian(5)
    #
    #                 # Vào từng link
    #                 detectImageAndClickLeftTopNew(r'E:\python\Selenium\PhotosGame\NhapLinkMap.png', dichY=20)
    #                 pyautogui.hotkey('ctrl', 'a')
    #
    #                 # Đợi 5s
    #                 DoiThoiGian(5)
    #
    #                 # copy link vào clipboard
    #                 copyStringToClipboard(link)
    #
    #                 # Đợi 5s
    #                 DoiThoiGian(2)
    #
    #                 # paste link và truy cập
    #                 print('Paste và Enter')
    #                 pyautogui.hotkey('ctrl', 'v')
    #                 pyautogui.press('enter')
    #
    #                 # Đợi 5s
    #                 DoiThoiGian(5)
    #
    #                 # Tiến hành tưới cây
    #                 if tuoiCay(soLanTuoiWorldMap, soMay=count - 1, gioiHan=2) == 1:
    #                     print('Hết cây! Chuyển sang link mới')
    #                     vaoLinkMoi = True
    #                     break
    #             if vaoLinkMoi:
    #                 break

    # 2.


if __name__ == "__main__":
    try:
        # Mở remote
        remoteWindow = OpenWindow(r'C:\Users\chubo\Desktop\RDCMan.exe', 'Remote')

        # Khởi động các máy
        # TODO: Fix lỗi một số máy không khởi động
        startComputer(remoteWindow, gioiHanMay=1)

        # Tạm dừng 15s để các máy sẵn sàng
        time.sleep(15)

        # Quá trình xử lý main process
        XuLyMainProcess(remoteWindow, gioiHanMay=1)

    except Exception as err:
        print('Có lỗi xảy ra')
        print(traceback.print_exc())
