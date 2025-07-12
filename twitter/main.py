from internet import InternetSpeedTwitterBot


PROMISED_DOWN = 65
PROMISED_UP = 10
TWITTER_USERNAME = "adahu@gmail.com"
TWITTER_PASSWORD = "q8z_ukDK&)"

bot = InternetSpeedTwitterBot()

# bot.get_internet_speed()
bot.twitter_login(TWITTER_USERNAME, TWITTER_PASSWORD)
print(f"Download speed: {bot.down}")
print(f"Up speed: {bot.up}")

