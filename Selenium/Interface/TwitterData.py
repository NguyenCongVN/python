class TwitterData:
    def __init__(self, username: str, password: str, emailDangKiIDO: str, HoVaTenDangKiIDO: str = ""):
        """
        Config dành cho IDO Tool
        :param HoVaTenDangKiIDO:
        :param username: Tên tài khoản twitter
        :param password: mật khẩu đăng nhập twitter
        :param emailDangKiIDO: Email đăng kí IDO
        """
        self.username = username
        self.password = password
        self.emailDangKiIDO = emailDangKiIDO
        self.HoVaTenDangKiIDO = HoVaTenDangKiIDO
