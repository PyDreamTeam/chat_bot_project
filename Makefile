start: #start on linux mint
	docker-compose down
	python3 -m venv .venv
	sudo docker-compose up --build -d
	.venv/bin/python3 -m pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	.venv/bin/python3 manage.py makemigrations
	.venv/bin/python3 manage.py migrate
	sleep 3
	.venv/bin/python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@admin.by', 'admin')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Filter_1', functionality='Functionality_1', integration='Integration_1', properties={'property_1':'property_1', 'property_2':'property_2'}, image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Filter_2', functionality='Functionality_2', integration='Integration_2', properties={'property_1':'property_1', 'property_2':'property_2', 'property_3':'property_3',}, image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Filter_3', functionality='Functionality_3', integration='Integration_3', properties={'property_1':'property_1', 'property_2':'property_2', 'property_3':'property_3', 'property_4':'property_4', 'property_5':'property_5',}, image=b'')"
	sleep 3
	.venv/bin/python3 manage.py runserver


lint: #format
	.venv/bin/pip freeze > requirements.txt
	# .venv/bin/black .
	# .venv/bin/isort .
	# .venv/bin/autopep8 ./ --recursive --in-place -a
	# .venv/bin/autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./


migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
