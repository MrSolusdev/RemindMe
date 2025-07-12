# Telegram Reminder Bot

**👨‍💻 Author:** MrSolusdev | **Telegram:** [@i_o_ekobo](https://t.me/i_o_ekobo)

## Description

A simple Telegram bot for setting reminders, written in Python using the python-telegram-bot library. The bot allows users to set time-based reminders with flexible time formats and custom reminder messages.

## Features
- Set reminders with flexible time formats:
  - Seconds (e.g., 30s)
  - Minutes (e.g., 5m, 10m)
  - Hours (e.g., 2h, 24h)
- Custom reminder messages
- Simple and intuitive commands
- Real-time notifications
- Error handling and user-friendly messages

## Commands
- `/start` - Get welcome message and usage instructions
- `/remindme <time> <message>` - Set a reminder
  - Example: `/remindme 10m Get up and stretch`
  - Example: `/remindme 2h Take a break`
  - Example: `/remindme 30s Check the oven`

## Installation

```bash
git clone https://github.com/MrSolusdev/RemindMe.git
cd RemindMe
```

Install required dependencies:
```bash
pip install python-telegram-bot
```

## Usage

1. Get your Telegram bot token from [@BotFather](https://t.me/BotFather)
2. Replace the `TOKEN` variable in `RemindMe.py` with your bot token
3. Run the bot:
```bash
python RemindMe.py
```

## How it works

The bot uses regular expressions to parse time inputs and converts them to seconds for internal processing. When a user sets a reminder, the bot:
1. Validates the time format
2. Extracts the reminder message
3. Schedules the reminder using `asyncio.sleep()`
4. Sends the reminder message after the specified time

## Requirements
- Python 3.7+
- python-telegram-bot library
- Telegram Bot Token

---

If you have questions or suggestions — feel free to reach out! 