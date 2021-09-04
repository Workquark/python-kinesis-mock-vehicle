from apscheduler.schedulers.background import BackgroundScheduler
from .sendmessage import job
import time

def schedule():
    scheduler = BackgroundScheduler()
    scheduler.configure()
    scheduler.add_job(job, 'interval', seconds=1)
    scheduler.start()
    # This is here to simulate application activity (which keeps the main thread alive).
    while True:
        time.sleep(5)