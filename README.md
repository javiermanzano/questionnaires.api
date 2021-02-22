# Run the app
python manage.py runserver

# Migrations
python manage.py makemigrations
python manage.py migrate

# Interaction
python manage.py shell

python manage.py createsuperuser --email admin@example.com --username admin

>> from questionnaires.models import CollectedData
>> cd = CollectedData(first_name="Javier", last_name="Manzano", email="jmanzano@gmail.com", providers="Spotify,Google", created=timezone.now())