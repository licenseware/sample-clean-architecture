from celery import Celery

from settings import config


def create_app(
    name=__name__,
    broker=config.celery_broker_uri,
    backend=config.celery_result_backend_uri,
):
    return Celery(name, backend=backend, broker=broker)
