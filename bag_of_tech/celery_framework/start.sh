# start rabbitmq
/Users/chenyuan/tools/rabbitmq_server-3.6.10/sbin/rabbitmq-server -detached

# start redis
/Users/chenyuan/tools/redis-4.0.1/src/redis-server /Users/chenyuan/tools/redis-4.0.1/redis.conf

# start celery
celery -A celery_app worker --loglevel=INFO

# start flower
flower -A celery_app --conf=flowerconfig.py