import re
import asyncio
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "TOKEN"

def parse_time(timestr: str) -> int | None:
    match = re.match(r'^(\d+)([smh])$', timestr.lower())
    if not match:
        return None
    value, unit = match.groups()
    value = int(value)
    return {
        's': value,
        'm': value * 60,
        'h': value * 3600
    }.get(unit)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I'm a reminder bot.\n"
        "Use the command /remindme <time>(1s, 1m, 1h) <text> to set a reminder.\n"
        "Example: /remindme 10m Get up and stretch"
    )

async def remindme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 2:
            await update.message.reply_text("❗ Use: /remindme <time> <text>\nExample: /remindme 10m Get up and stretch")
            return

        delay = parse_time(args[0])
        if delay is None:
            await update.message.reply_text("⏳ Time must be in the format: 10s, 5m, 2h")
            return

        reminder_text = ' '.join(args[1:])
        await update.message.reply_text(f"✅ I'll remind you in {args[0]}: {reminder_text}")

        await asyncio.sleep(delay)
        await update.message.reply_text(f"⏰ Reminder: {reminder_text}")

    except Exception as e:
        logging.exception("Error in /remindme")
        await update.message.reply_text("⚠️ Something went wrong. Try again.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("remindme", remindme))
    app.add_handler(CommandHandler("start", start))
    print("bot is running")
    app.run_polling()
