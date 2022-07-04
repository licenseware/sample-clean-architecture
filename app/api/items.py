from app import schema
from app.dependencies.db import Database
from settings import config

webapp = config.webapp_framework
WebRouter = webapp.WebRouter
WebHTTPException = webapp.WebHTTPException
WebRequest = webapp.WebRequest

router = WebRouter()


@router.get("/items/{item_id}", response_model=schema.Items)
async def read_item(item_id: int, request: WebRequest):
    db: Database = request.app.state.db

    item = db.get_item(item_id)
    if item:
        return item

    raise WebHTTPException(status_code=404, detail="Item not found")
