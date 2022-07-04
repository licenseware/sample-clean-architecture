import redis

from .base import Database


class Redis(Database):
    def __init__(self, host="localhost", port=6379, db=0, password=None):
        self._db = redis.Redis(host=host, port=port, db=0, password=password)
        self._db.ping()

    def get_item(self, item_id):
        item = self._db.hget(item_id, "name")
        if item:
            return {"name": item}
