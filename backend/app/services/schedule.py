from celery import Celery
from datetime import datetime

celery = Celery(__name__)
celery.conf.broker_url = "redis://localhost:6379"

@celery.task
def schedule_content_generation(campaign_id: int, schedule_time: datetime):

    pass