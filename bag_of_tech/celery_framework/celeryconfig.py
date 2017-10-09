import json


with open("application.conf", "r") as fh:
    rabbitmq_conf = json.load(fh)["rabbitmq_mgmt"]

broker_url = "pyamqp://{}@{}//".format(rabbitmq_conf["user"], rabbitmq_conf["host"])

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'America/New_York'
enable_utc = True

imports = ["bag_of_tech.celery_framework.stackoverflow",
           "bag_of_tech.celery_framework.word_cloud"]
