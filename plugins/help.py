HELP_TEXT = """
<b>PR FILE STORE BOT Commands:</b>
/start - Start the bot or get posts
/help - Show this help
/batch - Create link for more than one post
/custom_batch - Create custom batch from channel/group
/genlink - (reply to file) Create link for one post
/get_xxxxx - Retrieve a file by its unique code

<b>Admin Commands:</b>
/users - View bot statistics
/stats - Check your bot uptime
/broadcast - Broadcast any message to users
/dbroadcast - Broadcast message with auto-delete
/pbroadcast - Broadcast and pin message to all chats
/dlt_time - Set auto-delete time for files
/check_dlt_time - Check auto-delete time setting
/ban - Ban a user
/unban - Unban a user
/banlist - Show banned users
/add_admin - Add an admin
/deladmin - Remove an admin
/admins - List all admins
/addchnl - Add a force subscribe channel
/delchnl - Remove a force subscribe channel
/listchnl - Show all force subscribe channels
/fsub_mode - Toggle force subscribe on/off
/delreq - Remove users left channel/not getting req fsub
/mode - Set bot mode public/private (owner/admin only)

<b>How to use:</b>
• Send any file or document to store and get a link.
• Use /batch to send multiple files at once.
• Reply to a file with /genlink to get a link for that file.
• Use your generated link to retrieve files anytime with /get_xxxxx.
"""

from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.private & filters.command("help"))
async def help_handler(client, message: Message):
    await message.reply(HELP_TEXT)