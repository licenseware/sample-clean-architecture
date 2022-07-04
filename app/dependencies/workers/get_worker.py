import settings
from settings import config

from .base import Worker
from .celery_worker import create_app


def get_worker(env: settings.Environment = config.ENV) -> Worker:
    return {
        settings.Environment.TEST: create_app(),
        settings.Environment.DEV: create_app(),
        settings.Environment.PROD: create_app(),
    }[env]
