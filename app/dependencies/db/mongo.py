import pymongo

from .base import Database


class Mongo(Database):
    def __init__(
        self,
        host="localhost",
        port=27017,
        db_name="db",
        username=None,
        password=None,
        connect_timeout=1000,
    ):
        self.db_name = db_name
        self._db = pymongo.MongoClient(
            host=host,
            port=port,
            username=username,
            password=password,
            serverSelectionTimeoutMS=connect_timeout,
        )

        self._db.admin.command("ping")

    @property
    def db(self):
        return self._db[self.db_name]

    def get_item(self, item_id):
        return self.db.items.find_one({"item_id": item_id})
