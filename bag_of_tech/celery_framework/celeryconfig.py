import json


with open("application.conf", "r") as fh:
    conf = json.load(fh)

redis_conf = conf["redis"]
rabbitmq_conf = conf["rabbitmq_mgmt"]

broker_url = "pyamqp://{}@{}//".format(rabbitmq_conf["user"], rabbitmq_conf["host"])
result_backend = "redis://:{}@{}:{}/{}".format(redis_conf["password"], redis_conf["host"], redis_conf["port"],
                                               redis_conf["db"])

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'America/New_York'
enable_utc = True

imports = ["bag_of_tech.celery_framework.tasks"]
