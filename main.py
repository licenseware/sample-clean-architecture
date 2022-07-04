import logging

import settings
from app.api import routers
from settings import config


def get_db(env):
    from app.dependencies.db import memory, mongo, redis

    return {
        settings.Environment.TEST: memory.InMemory,
        settings.Environment.DEV: redis.Redis,
        settings.Environment.PROD: mongo.Mongo,
    }[env]


WebApp = config.webapp_framework.WebApp
app = WebApp()
[app.include_router(router) for router in routers]
logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL.value)


app.state.db = get_db(config.ENV)(**config.db_config)
logger.info("Starting with environment: %s", config.ENV)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=config.PORT,
        reload=config.ENV == settings.Environment.DEV,
    )
