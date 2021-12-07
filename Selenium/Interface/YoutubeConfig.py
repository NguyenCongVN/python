class YoutubeConfig:
    def __init__(self, webdriverPath: str, chrome_path: str, chrome_folder_path: str, youtube_email_path: str,
                 youtube_fname_path: str, youtube_lname_path: str, youtube_password_path: str,
                 account_index: int):
        """
        Config dành cho youtube Tool
        :param account_index: Số thứ tự tài khoản
        :param webdriverPath: Đường dẫn tới webdriver
        :param chrome_path: Đường dẫn tới chrome portable
        :param chrome_folder_path: đường dẫn tới folder chứa chrome portable
        :param youtube_data_path: đường dẫn tới youtube data
        """
        self.webdriverPath = webdriverPath
        self.chrome_path = chrome_path
        self.chrome_folder_path = chrome_folder_path
        self.youtube_email_path = youtube_email_path
        self.youtube_fname_path = youtube_fname_path
        self.youtube_lname_path = youtube_lname_path
        self.youtube_password_path = youtube_password_path
        self.account_index = account_index
