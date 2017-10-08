import json


with open("application.conf", "r") as fh:
    rabbitmq_conf = json.load(fh)["rabbitmq_mgmt"]

# RabbitMQ management api
broker_api = 'http://{}:{}@{}:port/api/'.format(rabbitmq_conf["password"], rabbitmq_conf["user"], rabbitmq_conf["host"],
                                                rabbitmq_conf["port"])
logging = 'DEBUG'
port = 5555
