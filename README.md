# bag_of_tech
Bag_of_tech analyzes technology trending from StackExchange API.

## Technologies used

### Data Downloading
* Used Celery to extract data from StackExchange API.
* Used RabbitMQ as Celery message broker.
* Used Flower to monitor Celery workers.

### Data Storage
* Used MongoDB to store metadata, question and answer content.

### Data Analysis
* To be added...