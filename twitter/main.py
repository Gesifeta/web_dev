from internet import InternetSpeedTwitterBot


PROMISED_DOWN = 65
PROMISED_UP = 10
TWITTER_EMAIL = "adahu@gmail.com"
TWITTER_USERNAME="adamechu"
TWITTER_PASSWORD = "q8z_ud3'kDK&)"

bot = InternetSpeedTwitterBot()

# bot.get_internet_speed()
bot.twitter_login(TWITTER_EMAIL,TWITTER_USERNAME, TWITTER_PASSWORD)

print(f"Download speed: {bot.down}")
print(f"Up speed: {bot.up}")

