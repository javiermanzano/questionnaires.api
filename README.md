python manage.py runserver

python manage.py makemigrations
python manage.py migrate

python manage.py shell

python manage.py createsuperuser --email admin@example.com --username admin



from questionnaires.models import CollectedData


cd = CollectedData(first_name="Javier", last_name="Manzano", email="jmanzano@soamee.com", providers="Spotify,Google", created=timezone.now())