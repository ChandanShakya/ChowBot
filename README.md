# CollegeBot

CollegeBot is a Python script that sends reminders for college lab classes via Telegram. It uses the python-telegram-bot library to interact with the Telegram Bot API.

## Prerequisites

- Python 3.8 or later
- python-telegram-bot library
- A Telegram bot token and chat ID

## Setup

1. Clone the repository
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Set the environment variables `BOT_TOKEN` and `CHAT_ID` to your Telegram bot token and chat ID, respectively. You can do this by running `export BOT_TOKEN=<your_bot_token>` and `export CHAT_ID=<your_chat_id>`
4. Run the script using `python CollegeBot.py`

## Running the bot automatically

You can also run the bot automatically using GitHub Actions. To do this, follow these steps:

1. Fork the repository
2. Go to the repository settings and click on "Secrets"
3. Add the following secrets:
   - `BOT_TOKEN`: Your Telegram bot token
   - `CHAT_ID`: Your Telegram chat ID
4. Go to the `.github/workflows/main.yml` file and modify the cron schedule to run the job at the desired time. For example, to run the job every weekday at 8am Nepal time, use the following schedule:

```
schedule:
- cron: '0 2 * * 1-5'
```

5. Commit and push your changes. The bot will now run automatically at the specified time.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
