# git-test

Polling website test using django and git

1. Use `pip install requirements.txt`
2. `python manage.py runserver` to start app and check pending migrations
3. `python manage.py migrate` to create database configured in settings.py according to models in models.py
4. `python manage.py sqlmigrate polls 0001` to see how the models are created in the database
5. `python manage.py createsuperuser` to create admin with access to db
6. Create questions and choices in the database or in the python shell
