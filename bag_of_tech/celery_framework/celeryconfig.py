import json


with open("application.conf", "r") as fh:
    redis_conf = json.load(fh)["redis"]
    rabbitmq_conf = json.load(fh)["rabbitmq_mgmt"]

broker_url = "pyamqp://{}@{}//".format(rabbitmq_conf["user"], rabbitmq_conf["host"])
result_backend = "redis://:{}@{}:{}/{}".format(redis_conf["password"], redis_conf["host"], redis_conf["port"],
                                               redis_conf["db"])

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'CDT'
enable_utc = True

imports = ["bag_of_tech.celery_framework.tasks"]
