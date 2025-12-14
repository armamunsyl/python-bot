import asyncio
import os
from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = os.getenv("8418386453:AAF9Vwja5xTdBYPJKXr_0FJb6-pfryhFU5I")
CHANNEL_ID = os.getenv("-1003687897949")

messages = [
    "আজকের AI টিপ: ছোট কাজ অটোমেট করলেই সময় বাঁচে",
    "Automation টিপ: বারবার করা কাজ স্ক্রিপ্টে রূপান্তর করো",
    "AI শেখা মানেই ভবিষ্যতের জন্য প্রস্তুতি",
    "প্রতিদিন ১% উন্নতি করলেই বড় পরিবর্তন আসে",
    "টেকনোলজি ব্যবহার করো স্মার্টভাবে"
]

async def send_messages():
    bot = Bot(token=BOT_TOKEN)
    index = 0

    while True:
        try:
            await bot.send_message(chat_id=CHANNEL_ID, text=messages[index])
            index = (index + 1) % len(messages)
            await asyncio.sleep(60)

        except TelegramError as e:
            print("Telegram error:", e)
            await asyncio.sleep(120)

asyncio.run(send_messages())
