import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
API_ID = int(os.getenv("API_ID", "26106561"))
API_HASH = os.getenv("API_HASH", "6bf2b0a825260beafe9955ffed29f978")
MONGO_URI = os.getenv("MONGO_URI", "")
OWNER_ID = int(os.getenv("OWNER_ID", "7753899951"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "OWNER_OF_PR")
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", "-1002751155801"))
LOG_CHANNEL_USERNAME = os.getenv("LOG_CHANNEL_USERNAME", "databaseprlogs")
START_PHOTO = "https://res.cloudinary.com/dqs0i4x9y/image/upload/v1756735243/ucigusyujb5bwxsjy1rm.jpg"
CHANNEL_LINK = os.getenv("CHANNEL_LINK", "https://t.me/PR_ALL_BOT")
SUPPORT_LINK = os.getenv("SUPPORT_LINK", "https://t.me/PR_ALL_BOT_SUPPORT")
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 3600))
FSUB_CHANNELS = os.getenv("FSUB_CHANNELS", "")
ADMINS = [OWNER_ID]
START_MSG = (
    "A powerful, modern Telegram bot to store files, documents, or media and generate unique download links. "
    "Built for PR and its community, this bot supports batch uploads, auto-deletion, admin tools, force subscribe, broadcasts, and more."
)