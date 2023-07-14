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
	
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='CRM', functionality='Functionality_1', integration='Integration_1', properties={1:'amoCRM', 2:'Битрикс24', 3:'RetailCRM', 4:'1C Битрикс', 5:'YClients', 6:'Мегаплан',}, image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Голосовые помощники', functionality='Functionality_2', integration='Integration_2', properties={1:'Алиса', 2:'Маруся', 3:'Aimybox Google Assistant', 4:'Салют',}, image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties={1:'ЮKassa', 2:'Робокасса', 3:'ЮMoney', 4:'Prodamus', 5:'Stripe', 6:'Paypal', 7:'Тинькофф', 8:'Fondy', 9:'Wayforpay', 10:'Payonline',}, image=b'')"
	
	# sleep 3

	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='CRM', functionality='Functionality_1', integration='Integration_1', properties='amoCRM', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='CRM', functionality='Functionality_1', integration='Integration_1', properties='Битрикс24', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='CRM', functionality='Functionality_1', integration='Integration_1', properties='RetailCRM', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='CRM', functionality='Functionality_1', integration='Integration_1', properties='1C Битрикс', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='CRM', functionality='Functionality_1', integration='Integration_1', properties='YClients', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='CRM', functionality='Functionality_1', integration='Integration_1', properties='Мегаплан', image=b'')"
	
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Голосовые помощники', functionality='Functionality_2', integration='Integration_2', properties='Алиса', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Голосовые помощники', functionality='Functionality_2', integration='Integration_2', properties='Маруся', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Голосовые помощники', functionality='Functionality_2', integration='Integration_2', properties='Aimybox Google Assistant', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Голосовые помощники', functionality='Functionality_2', integration='Integration_2', properties='Салют', image=b'')"
	
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties='ЮKassa', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties='Робокасса', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties='ЮMoney', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties='Prodamus', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties='Stripe', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties='Paypal', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties='Тинькофф', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties='Fondy', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties='Wayforpay', image=b'')"
	# .venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter; PlatformFilter.objects.create(title='Платежные системы', functionality='Functionality_3', integration='Integration_3', properties='Payonline', image=b'')"
	
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
