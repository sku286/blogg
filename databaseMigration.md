# blogg
1.  execute : python3 manage.py dumpdata > datadump.json
2.  Install postgres
3.  Change settings.py file:
           DATABASES = {
				'default': {
					'ENGINE': 'django.db.backends.sqlite3',
					'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
							}
						}
		new code:
		    DATABASES = {
				'default': {
					'ENGINE': 'django.db.backends.postgresql_psycopg2',
					'NAME': os.path.join(BASE_DIR, 'myproject'),
					'USER': 'postgres',
					'PASSWORD': '',
					'HOST': 'localhost',
					'PORT': '5432',
    }
}
4.  python manage.py migrate --run-syncdb // syncdb and migrating the db
    OR
	python manage.py --run-syncdb
	python manage.py migrate 
 4.1(optional) //Django shell to exclude contentype data
     python manage.py shell
	 from django.contrib.contenttypes.models import ContentType
     ContentType.objects.all().delete()

5. python manage.py loaddata datadump.json
