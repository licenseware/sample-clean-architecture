from .create_app import app


@app.task(name="add")
def add(a: int, b: int) -> int:
    return a + b
