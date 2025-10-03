# PR FILE STORE BOT

A powerful, modern Telegram bot to store files, documents, or media and generate unique download links. Built for PR and its community, this bot supports batch uploads, auto-deletion, admin tools, force subscribe, broadcasts, and more.

![Start Banner](https://res.cloudinary.com/dqs0i4x9y/image/upload/v1756735243/ucigusyujb5bwxsjy1rm.jpg)

---

## Features

- Store any file, document, or media and get a private download link
- Batch upload support (`/batch`, `/custom_batch`)
- Retrieve files by unique code (`/get_xxxxx`)
- Broadcasts, admin controls, auto-delete, ban/unban
- Force subscribe to channels/groups
- Interactive start/help/about/channel buttons
- User statistics and uptime monitoring
- Public/Private mode for full privacy control

---

## Commands

```
/start - Start the bot or get posts
/help - Show all commands and usage
/batch - Create links for multiple posts
/custom_batch - Create custom batch from channel/group
/genlink - (Reply to file) Get a link for that file
/get_xxxxx - Retrieve a file by its unique code

/users - View bot statistics (admin only)
/stats - Check bot uptime and stats (admin only)
/broadcast - Broadcast message to users (admin only)
/dbroadcast - Broadcast message with auto-delete (admin only)
/pbroadcast - Broadcast + pin message to users (admin only)

/dlt_time - Set auto-delete time for files (admin only)
/check_dlt_time - Check current auto-delete setting (admin only)

/ban - Ban a user (admin only)
/unban - Unban a user (admin only)
/banlist - List banned users (admin only)

/add_admin - Add a new admin (owner/admin only)
/deladmin - Remove an admin (owner/admin only)
/admins - List current admins

/addchnl - Add channel for force subscribe (admin only)
/delchnl - Remove force subscribe channel (admin only)
/listchnl - List force subscribe channels (admin only)
/fsub_mode - Toggle force subscribe on/off (admin only)
/delreq - Remove users who left channel (admin only)

/mode public|private - Set bot mode (admins only)
```

---

## Deploy on Render

1. Clone this repository and push your changes.
2. Set these environment variables in Render:
   - `BOT_TOKEN`, `API_ID`, `API_HASH`, `MONGO_URI`, `OWNER_ID`, `OWNER_USERNAME`, etc.
3. Add a `Procfile`:
    ```
    web: python pr_file_store_bot.py
    ```
4. Add a `render.yaml` for easy deployment.

---

## Credits

- Developed by [@OWNER_OF_PR](https://t.me/OWNER_OF_PR)
- Logs Channel: [@databaseprlogs](https://t.me/databaseprlogs)
- [PR ALL BOT Main Channel](https://t.me/PR_ALL_BOT)
- [Support Group](https://t.me/PR_ALL_BOT_SUPPORT)

---

## License

Private. For PR community use only.