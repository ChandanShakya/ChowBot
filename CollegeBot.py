import datetime
import time
import telegram
import os
from telegram.ext import Updater, CommandHandler

# set up the bot
TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
bot = telegram.Bot(token=TOKEN)

# define the labs and their corresponding days
labs = {
    'Network Programming Lab': [4],
    'Advance Java Programming Lab': [2, 4],
    'Mobile Programming Lab': [1, 3]
}

# define the message to be sent
message = "Reminder: {} today at 8am."

# define a function to check if today is a lab day
def is_lab_day(day, lab):
    return day.weekday() in lab

# define a function to send the reminder message
def send_reminder(context):
    now = datetime.datetime.now()
    for lab, days in labs.items():
        if is_lab_day(now, days):
            text = message.format(lab)
            bot.send_message(chat_id=CHAT_ID, text=text)

# set up the job queue
updater = Updater(TOKEN, use_context=True)
job_queue = updater.job_queue

# add the job to send the reminder message at 8am every day
job = job_queue.run_daily(send_reminder, time=datetime.time(hour=8))

# start the bot
updater.start_polling()
updater.idle()
