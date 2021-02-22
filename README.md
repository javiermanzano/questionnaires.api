# Run the app

```
python manage.py runserver
```

Server will run on port 8000

# Migrations
Postgres Database has been used for this simple example. There is a docker-compose.yaml file to get the infra up.

```
docker-compose up -d
```

You can run migrations with these commands:

```
python manage.py makemigrations
python manage.py migrate
```

# Interaction
```
python manage.py shell
python manage.py createsuperuser --email admin@example.com --username admin
```

```
>> from questionnaires.models import CollectedData
>> cd = CollectedData(first_name="Javier", last_name="Manzano", email="jmanzano@gmail.com", providers="Spotify,Google", created=timezone.now())
```