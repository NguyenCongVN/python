class IDOConfig:
    def __init__(self, webdriverPath: str, chrome_path: str, chrome_folder_path: str, twitter_data_path: str,
                 gmail_data_path: str,
                 proxy_path: str, wallet_path: str, anti_captcha_path: str, telegram_data_path: str,
                 discord_data_path: str, proxy_data_path: str):
        """
        Config dành cho IDO Tool
        :param webdriverPath: Đường dẫn tới webdriver
        :param chrome_path: Đường dẫn tới chrome portable
        :param chrome_folder_path: đường dẫn tới folder chứa chrome portable
        :param twitter_data_path: đường dẫn tới twitter data
        """
        self.webdriverPath = webdriverPath
        self.chrome_path = chrome_path
        self.chrome_folder_path = chrome_folder_path
        self.twitter_data_path = twitter_data_path
        self.proxy_path = proxy_path
        self.anti_captcha_path = anti_captcha_path
        self.gmail_data_path = gmail_data_path
        self.wallet_path = wallet_path
        self.telegram_data_path = telegram_data_path
        self.discord_data_path = discord_data_path
        self.proxy_data_path = proxy_data_path
