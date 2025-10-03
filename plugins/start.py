from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database import add_user, is_banned
from config import START_MSG, START_PHOTO, OWNER_USERNAME

START_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("HELP", callback_data="show_help"),
        InlineKeyboardButton("ABOUT", callback_data="show_about")
    ],
    [InlineKeyboardButton("CHANNELS", callback_data="show_channels")],
    [InlineKeyboardButton("DEVELOPER", url=f"https://t.me/{OWNER_USERNAME}")]
])

@Client.on_message(filters.private & filters.command("start"))
async def start_handler(client, message: Message):
    user_id = message.from_user.id
    add_user(user_id)
    if is_banned(user_id):
        await message.reply("🚫 You are banned from using this bot.")
        return
    await message.reply_photo(
        photo=START_PHOTO,
        caption=START_MSG,
        reply_markup=START_BUTTONS
    )

@Client.on_callback_query(filters.regex("show_help"))
async def help_callback(client, cq):
    from plugins.help import HELP_TEXT
    await cq.message.edit_text(HELP_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="back_to_start")]]))

@Client.on_callback_query(filters.regex("show_about"))
async def about_callback(client, cq):
    await cq.message.edit_text(
        f"<b>About This Bot:</b>\n"
        f"• Developer: <a href='https://t.me/{OWNER_USERNAME}'>@{OWNER_USERNAME}</a>\n"
        "• For PR and its users.\n"
        "• Logs channel: @databaseprlogs\n",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="back_to_start")]])
    )

@Client.on_callback_query(filters.regex("show_channels"))
async def channel_callback(client, cq):
    await cq.message.edit_text(
        "<b>Our Channels & Groups:</b>",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("ABOUT PR", url="https://t.me/PR_LINK_SHARE_BOT?start=req_LTEwMDMwMjA5MDM1ODE")],
            [InlineKeyboardButton("MAIN CHANNEL", url="https://t.me/MAIN_CHANNEL_PR")],
            [InlineKeyboardButton("ALL ONGOING ANIME", url="https://t.me/+aIVAn5vVpqU5ZjU9")],
            [InlineKeyboardButton("HAREM REALM", url="https://t.me/+7FwL6dmXhtIwMzFl")],
            [InlineKeyboardButton("PR ALL BOT", url="https://t.me/+BNhBea8t8RVjODJl")],
            [InlineKeyboardButton("CHATTING GROUP", url="https://t.me/+CzAjQld8eVM4YjA1")],
            [InlineKeyboardButton("BACK", callback_data="back_to_start")]
        ]),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("back_to_start"))
async def back_to_start(client, cq):
    await cq.message.edit_caption(caption=START_MSG, reply_markup=START_BUTTONS)