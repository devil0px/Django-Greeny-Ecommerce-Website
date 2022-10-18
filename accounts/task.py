# from project.celery import celery 
from celery import shared_task
import time 


@shared_task
def print_welcome(n):
    time.sleep(n)
    print('welcome')


