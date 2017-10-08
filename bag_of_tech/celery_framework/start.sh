source activate env_bot

# start rabbitmq
rabbitmq-server -detached

# start celery
celery -A celery_app worker --loglevel=INFO > worker.log 2>&1 &

# start flower
flower -A celery_app --conf=flowerconfig.py > flower.log 2>&1 &