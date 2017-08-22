from __future__ import absolute_import, unicode_literals
import logging
from bag_of_tech.celery_framework.celery_app import app
from pymongo import MongoClient
from stackapi import StackAPI

logger = logging.getLogger("tasks")


@app.task
def get_question():
    api = StackAPI('stackoverflow')
    questions = api.fetch('questions')["items"]

    client = MongoClient()
    db = client.bot
    result = db.question.insert_many(questions)
    logger.info(result.inserted_ids)

    return len(questions)
