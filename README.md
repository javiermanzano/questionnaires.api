# Run the app
python manage.py runserver

Server will run on port 8000

# Migrations
SQLITE Database has been used for this simple example, although We've prepared a docker-compose.yaml to start using Postgres. That should be pretty straightforward to do just changing config files

python manage.py makemigrations
python manage.py migrate

# Interaction
python manage.py shell

python manage.py createsuperuser --email admin@example.com --username admin

>> from questionnaires.models import CollectedData
>> cd = CollectedData(first_name="Javier", last_name="Manzano", email="jmanzano@gmail.com", providers="Spotify,Google", created=timezone.now())