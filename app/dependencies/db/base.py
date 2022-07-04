import abc

from app import schema


class Database(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_item(self, item_id) -> schema.Items:
        pass

    def __repr__(self) -> str:
        return self.__class__.__name__
