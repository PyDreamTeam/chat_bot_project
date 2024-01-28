from celery import shared_task

from accounts.email import EmailSender
from accounts.services import (
    add_solution_in_history,
    remove_unnecessary_solution_history,
    add_platform_in_history,
    remove_unnecessary_platform_history,
)
from config.celery import app


#Solution history
@shared_task
def add_solution_in_history_task(user_id, solution_id):
    add_solution_in_history(user_id=user_id, solution_id=solution_id)


@app.task
def remove_unnecessary_solution_history_task():
    remove_unnecessary_solution_history()


#Platform history
@shared_task
def add_platform_in_history_task(user_id, platform_id):
    add_platform_in_history(user_id=user_id, platform_id=platform_id)


@app.task
def remove_unnecessary_platform_history_task():
    remove_unnecessary_platform_history()


@shared_task
def send_message_when_new_order_task(order_id):
    EmailSender().send_message_when_new_order(order_id=order_id)
