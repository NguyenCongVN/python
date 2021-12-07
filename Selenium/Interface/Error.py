import enum


class ProcessError(enum.Enum):
    time_try_error = 'Quá số lần xử lý process'


class CaptchaCloudFareError(enum.Enum):
    time_out = 'Quá số thời gian chờ giải captcha cloud fare'
    not_solving = 'Đang không giải'
    time_num_out = 'Quá số lần xử lý giải captcha cloud fare'


class LoginTwitterEror(enum.Enum):
    time_out = 'Quá thời gian chờ bước đăng nhập twitter'
    time_num_out = 'Quá số lần thử bước đăng nhập twitter'
    open_div_time_num_out = 'Quá số thời gian thử mở lại div để connect twitter'
    sign_in_time_num_out = 'Quá số lần thử đăng nhập twitter'
    twitter_auth_need_error = 'Tài khoản cần xác thực'
    twitter_die_error = 'Tài khoản twitter die'


class FollowTwiiterError(enum.Enum):
    follow_twitter_time_num_out = 'Quá số lần thử follow twitter'
    follow_twitter_authorize_time_out = 'Quá số thời gian thử authorize twitter'


class JoinTelegramError(enum.Enum):
    join_telegram_time_num_out = 'Quá số lần thử join telegram'


class DiscordError(enum.Enum):
    captcha_discord_time_out = 'Quá thời gian giải captcha discord'
    time_out = 'Quá thời gian chờ discord'
    time_num_out = 'Quá số thời gian thử join discord'


class EnterWalletError(enum.Enum):
    enter_wallet_time_num_out = 'Quá số lần thử điền ví'


class TelegramError(enum.Enum):
    time_num_out = 'Quá số thời gian thử mở telegram'
