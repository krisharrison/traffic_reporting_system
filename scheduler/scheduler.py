from flask import Blueprint
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
import datetime

from ..app.routes import scheduler_test

scheduler = Blueprint('scheduler', __name__)

jobstores = {
    "default": SQLAlchemyJobStore(url="sqlite:///job.sqlite")
}
executors = {
    "default": ThreadPoolExecutor(20),

}
job_defaults = {
    "coalesce":False,
    "max_instance":3
}

scheduler = BackgroundScheduler(jobstores=jobstores,executors=executors,job_defaults=job_defaults)

#JOBS
scheduler.add_job((scheduler_test,'date', datetime.datetime.now))
