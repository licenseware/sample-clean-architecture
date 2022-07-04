from faker import Faker

from .create_app import app


@app.task(name="emit_log")
def task_emit_log():
    f = Faker()
    return f.text()
