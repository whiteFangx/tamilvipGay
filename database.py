from pymongo import MongoClient

from config import MONGO_DB_URL

kuki_db = MongoClient(MONGO_DB_URL)["KUKI"]["CHATS"]


class Chat:
    def __init__(self, chat_id):
        self.chat_id = chat_id

    def is_ai_chat(self):
        return bool(kuki_db.find_one({"chat_id": self}))

    def add_chat(self):
        if not Chat.is_ai_chat(self):
            kuki_db.insert_one({"chat_id": self})
        else:
            return

    def rm_chat(self):
        if Chat.is_ai_chat(self):
            kuki_db.delete_one({"chat_id": self})
        else:
            return
