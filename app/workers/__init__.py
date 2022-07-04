import pathlib
import pkgutil

from .create_app import app

tasks_dir = str(pathlib.Path(__file__).parent)


app.autodiscover_tasks(
    packages=[
        f"{__name__}.{pkg.name}"
        for pkg in pkgutil.iter_modules([tasks_dir])
        # if "task" in pkg.name
    ]
)


# from faker import Faker
# from functools import partial

# f = Faker()


# def add_task():
#     return (f.random_int(100, 1000), f.random_int(100, 1000))


# def sub_task():
#     return (f.random_int(1000, 2000), f.random_int(100, 1000))


# def mul_task():
#     return (f.random_int(100, 1000), f.random_int(100, 1000))


# def emit_log_task():
#     return ()


# def get_random_task():
#     tasks = {
#         "add": add_task,
#         "sub": sub_task,
#         "mul": mul_task,
#         "emit_log": emit_log_task,
#     }
#     random_task_id = f.random_int() % len(tasks)
#     task_key = list(tasks.keys())[random_task_id]
#     task_args = tasks[task_key]()
#     # print(task_args)
#     return partial(app.send_task, task_key, args=task_args)
