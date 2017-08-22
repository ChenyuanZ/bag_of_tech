# start rabbitmq
rabbitmq-server -detached

# start redis
redis-server /Users/chenyuan/tools/redis-4.0.1/redis.conf

# start celery
celery -A celery_app worker --loglevel=INFO & > worker.log

# start flower
flower -A celery_app --conf=flowerconfig.py & > flower.log