from celery import shared_task

@shared_task
def data_task():
    SITE='http://localhost:8001/api/books/'