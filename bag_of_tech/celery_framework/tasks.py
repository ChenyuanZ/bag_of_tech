from __future__ import absolute_import, unicode_literals
from bag_of_tech.celery_framework.celery_app import app
from stackapi import StackAPI


@app.task
def get_question():
    api = StackAPI('stackoverflow')
    questions = api.fetch('questions')["item"]
    return len(questions)
