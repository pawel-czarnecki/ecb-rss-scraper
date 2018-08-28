# ecb-rss-scraper
RSS scraper for downloading exchange rate from European Central Bank.


### Architecture
- Python v3.5
- Django v1.11
- Django Rest Framework v3.8.2
- Beautiful Soup v4.6.3
- Celery v4.2.1
- SQLite


### Installation
Install project requirements in your virtual environment.
```sh
$ pip install -r requirements.txt
```

Apply database migration.
```sh
$ ./manage.py migrate
```

Add initial database data with sample currencies.
```sh
$ ./manage.py loaddata currency
```

Create superuser to be able to login to admin panel.
```sh
$ ./manage.py createsuperuser
```

Install Redis as a Celery “Broker”. Go to Redis [download official page](https://redis.io/download) and install it.


### Running
Fire up the Redis server.
```sh
$ redis-server
```

Start Celery worker which is runnig periodic task each day at 15:16 o'clock.
```sh
$ celery -A ecb worker -l info -B
```

Start server application:
```sh
$ ./manage.py runserver 0.0.0.0:8000
```

REST API endpoint is available on: http://0.0.0.0:8000/v1/api/exchange-rate/


### Todos
- Create filtering query parameters in `exchange_rate_list` endpoint
- Create OAuth 2.0 authentication for REST API
- Create swagger documentation for REST API
- Create unit tests for `exchange_rate` module and REST API
- Add docstrings
- Create connection to PostgreSQL database
- Put application into Docker container
- Create docker-compose.yml for simple run application