from enum import Enum

from pydantic import BaseSettings as BaseSettings  # noqa: F401


class StrEnum(str, Enum):
    """
    This class doesn't do anything, we're just interested in keeping the base in one
    place so that we can easily change it should we ever want to
    """
