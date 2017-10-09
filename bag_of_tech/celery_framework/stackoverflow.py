from __future__ import absolute_import, unicode_literals
import json
import logging
import requests
from bag_of_tech.celery_framework.celery_app import app
from pymongo import MongoClient

LOGGER = logging.getLogger("stackoverflow")
CLIENT = MongoClient()
MONGO_CONN = CLIENT.bot
URL = "https://api.stackexchange.com/2.2/{}?order=desc&sort=activity&site=stackoverflow&filter=withbody"


@app.task
def get_answer(q_ids):
    """Retrieve accepted answers by question id"""
    answers = json.loads(requests.get(URL.format("/questions/{ids}/answers".format(ids=";".join(q_ids)))).text)["items"]
    answers_accepted = [a for a in answers if a["is_accepted"] is True]
    result = MONGO_CONN.answer.insert_many(answers_accepted)
    LOGGER.debug("Answers: {}".format(str(result.inserted_ids)))

    return len(answers_accepted)


@app.task
def get_question():
    """Retrieve answered questions"""
    questions = json.loads(requests.get(URL.format("questions")).text)["items"]
    questions_answered = [q for q in questions if q["is_answered"] is True]
    result = MONGO_CONN.question.insert_many(questions_answered)
    LOGGER.debug("Questions: {}".format(str(result.inserted_ids)))

    question_ids = [str(q["question_id"]) for q in questions_answered]
    get_answer.delay(question_ids)

    return len(questions_answered)
