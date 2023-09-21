from celery import shared_task

from config.celery import app
from accounts.services import add_solution_in_history, remove_unnecessary_solution_history


@shared_task
def add_solution_in_history_task(user_id, solution_id):
    add_solution_in_history(user_id=user_id, solution_id=solution_id)


@app.task
def remove_unnecessary_solution_history_task():
    remove_unnecessary_solution_history()
