from datetime import datetime
from whatsapptwilio import alert
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# Schedule job_function to be called every five seconds
sched.add_job(alert, 'interval', seconds=5)

sched.start()
