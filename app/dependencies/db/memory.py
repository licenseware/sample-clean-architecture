from .base import Database


class InMemory(Database):
    def __init__(self):
        self._db = {}

    def get_item(self, item_id):
        return self._db.get(item_id)
