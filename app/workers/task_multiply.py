from .create_app import app


@app.task(name="mul")
def task_multiply(a, b):
    return a * b
