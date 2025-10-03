from config import OWNER_ID
from database import db

def is_public():
    m = db.settings.find_one({"_id": "bot_mode"})
    return not m or m.get("mode", "public") == "public"

from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS, OWNER_USERNAME

@Client.on_message(filters.private & filters.command("mode") & filters.user(ADMINS))
async def mode_handler(client, message: Message):
    args = message.text.split()
    if len(args) < 2 or args[1].lower() not in ["public", "private"]:
        m = db.settings.find_one({"_id": "bot_mode"})
        mode = m["mode"] if m else "public"
        await message.reply(f"Current bot mode: <b>{mode.upper()}</b>\nUsage: <code>/mode public</code> or <code>/mode private</code>")
        return
    mode = args[1].lower()
    db.settings.update_one({"_id": "bot_mode"}, {"$set": {"mode": mode}}, upsert=True)
    await message.reply(f"Bot mode changed to <b>{mode.upper()}</b>.")