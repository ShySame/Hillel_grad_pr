from celery import shared_task

@shared_task
def data_task():
    SITE=