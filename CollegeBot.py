import datetime
import os
import telegram
from telegram.ext import Updater, CommandHandler

# Get the bot token and chat ID from environment variables
TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

# Initialize the bot
bot = telegram.Bot(token=TOKEN)

# Define the labs and their corresponding days
labs = {
    'Network Programming Lab': [4],
    'Advance Java Programming Lab': [2, 4],
    'Mobile Programming Lab': [1, 3]
}

# Define the message to be sent
message = "Reminder: {} today."

# Define a function to check if today is a lab day
def is_lab_day(day, lab_days):
    return day.weekday() in lab_days

# Define a function to send the reminder message
def send_reminder(context):
    now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=45)
    for lab, days in labs.items():
        if is_lab_day(now, days):
            text = message.format(lab)
            bot.send_message(chat_id=CHAT_ID, text=text)

# Set up the job queue
updater = Updater(TOKEN, use_context=True)
job_queue = updater.job_queue

# Add the job to send the reminder message at 8am Nepal time every weekday
job = job_queue.run_daily(send_reminder, time=datetime.time(hour=2, minute=45), days=(0, 1, 2, 3, 4))

# Start the bot
updater.start_polling()
updater.idle()
