# Django API seed - (rest_framework, psql, gunicorn)

## Description
Seed for starting a django project.
- Has rest_framework
- Postgresql database
- Dockerfile and docker-compose.yml
- one seed_app installed in the seed_project
- Guincorn WSGI server implementation

## Usage
You will want to rename your project and rename your application. This is a process more involved than just renaming the directories.

### Renaming your project - [Easy way to rename a django project](https://stackoverflow.com/questions/18293875/easy-way-to-rename-a-django-project)
1. Rename the seed_project directory to your new project's name.

2. In manage.py: Change os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seed_project.settings')

3. In project directory /wsgi.py: Change os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seed_project.settings')

4. In project directory /settings.py: Change ROOT_URLCONF = 'seed_project.urls' and change WSGI_APPLICATION = 'seed_project.wsgi.application'

5. In docker-compose.yml line 6: Change seed_project.wsgi:application --bind 0.0.0.0:8000

### Renaming your app - [How to change the name of a django app](https://stackoverflow.com/questions/8408046/how-to-change-the-name-of-a-django-app)
1. Rename seed_app to your new app name

2. In project directory /urls.py: Change path('api/v1/', include('seed_app.urls')), to include 'your_new_app.urls'

3. Edit the database table django_content_type with the following command: UPDATE django_content_type SET app_label='<NewAppName>' WHERE app_label='<OldAppName>'
