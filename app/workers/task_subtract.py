from .create_app import app


@app.task(name="sub")
def sub(a: int, b: int) -> int:
    return a - b
