start: #start on linux mint
	docker-compose down
	python3 -m venv .venv
	sudo docker-compose up --build -d
	.venv/bin/python3 -m pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	sleep 3
	.venv/bin/python3 manage.py makemigrations
	sleep 3
	.venv/bin/python3 manage.py migrate
	sleep 3
	.venv/bin/python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@admin.by', 'admin')"
	sleep 3
	.venv/bin/python3 manage.py runserver


lint: #format
	.venv/bin/pip freeze > requirements.txt
	.venv/bin/black .
	.venv/bin/isort .
	.venv/bin/autopep8 ./ --recursive --in-place -a
	.venv/bin/autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./


migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate




