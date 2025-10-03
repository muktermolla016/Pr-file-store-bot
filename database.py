from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["filestorebot"]

def add_user(user_id):
    db.users.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)

def user_exists(user_id):
    return db.users.find_one({"_id": user_id}) is not None

def get_users():
    return [u["_id"] for u in db.users.find()]

def ban_user(user_id):
    db.bans.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)

def unban_user(user_id):
    db.bans.delete_one({"_id": user_id})

def is_banned(user_id):
    return db.bans.find_one({"_id": user_id}) is not None

def add_admin(user_id):
    db.admins.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)

def remove_admin(user_id):
    db.admins.delete_one({"_id": user_id})

def get_admins():
    return [a["_id"] for a in db.admins.find()]

def add_file(unique_id, file_id, owner_id, expire=None):
    db.files.update_one(
        {"_id": unique_id},
        {"$set": {"file_id": file_id, "owner_id": owner_id, "expire": expire}},
        upsert=True
    )

def get_file(unique_id):
    return db.files.find_one({"_id": unique_id})

def delete_file(unique_id):
    db.files.delete_one({"_id": unique_id})

def set_auto_delete_time(seconds):
    db.settings.update_one({"_id": "auto_delete"}, {"$set": {"seconds": seconds}}, upsert=True)

def get_auto_delete_time():
    doc = db.settings.find_one({"_id": "auto_delete"})
    return doc["seconds"] if doc else 3600

def add_fsub_channel(channel):
    db.fsub.update_one({"_id": channel}, {"$set": {"_id": channel}}, upsert=True)

def remove_fsub_channel(channel):
    db.fsub.delete_one({"_id": channel})

def get_fsub_channels():
    return [c["_id"] for c in db.fsub.find()]