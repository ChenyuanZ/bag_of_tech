# stop rabbitmq
rabbitmqctl stop
pkill -f "rabbitmq"

# stop celery & flower
pkill -9 -f "celery"