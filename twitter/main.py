from internet import InternetSpeedTwitterBot


PROMISED_DOWN = 65
PROMISED_UP = 10
TWITTER_USERNAME = "adamgemechu@gmail.com"
TWITTER_PASSWORD = "<q8z_u!jd3'kDK&)>"

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
print(f"Download speed: {bot.down}")
print(f"Up speed: {bot.up}")
