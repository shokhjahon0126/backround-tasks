import time
from celery import shared_task


@shared_task
def long_task(number):
    print("Task boshlandi...")

    for i in range(1, number):
        print(f"{i}/10 - ishlayapti...")
        time.sleep(2)

    return  "tugatildi"
