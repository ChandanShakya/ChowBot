import datetime
import telegram

# Replace with your bot token and group chat ID
BOT_TOKEN = 'your_bot_token'
CHAT_ID = 'your_chat_id'

# Create a Telegram bot object
bot = telegram.Bot(token=BOT_TOKEN)

# Get the current day of the week and time
today = datetime.datetime.today()
weekday = today.weekday()
time = today.time()

# Send a message if today is Friday at 8am
if weekday == 4 and time.hour == 8:
    message = 'Reminder: Network Programming Lab today!'
    bot.send_message(chat_id=CHAT_ID, text=message)

# Send a message if today is Tuesday or Friday at 8am
if (weekday == 1 or weekday == 4) and time.hour == 8:
    message = 'Reminder: Advance Java Programming Lab today!'
    bot.send_message(chat_id=CHAT_ID, text=message)

# Send a message if today is Monday or Thursday at 8am
if (weekday == 0 or weekday == 3) and time.hour == 8:
    message = 'Reminder: Mobile Programming Lab today!'
    bot.send_message(chat_id=CHAT_ID, text=message)