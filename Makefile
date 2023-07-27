start: #start on linux mint
	docker-compose down
	python3 -m venv .venv
	sudo docker-compose up --build -d
	.venv/bin/python3 -m pip install --upgrade pip
	sleep 5
	.venv/bin/pip install -r requirements.txt
	sleep 5
	.venv/bin/python3 manage.py makemigrations
	sleep 5
	.venv/bin/python3 manage.py migrate
	sleep 3
	.venv/bin/python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@admin.by', 'admin')"
	sleep 3
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Интеграции',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Каналы',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Функцилнал для настройки чат-ботов',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='WHATSAPP BUSINESS API',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Работа с подписчиками',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Способы подписки',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Статисткика и аналитика',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Тарифы',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Документальное подтверждение',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Техническая поддержка',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Уровень сложности',)"
	sleep 3
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='CRM', group=PlatformGroup.objects.get(id=1), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Платежные системы', group=PlatformGroup.objects.get(id=1), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Сервисы-интеграторы', group=PlatformGroup.objects.get(id=1), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Работа с API', group=PlatformGroup.objects.get(id=1), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Голосовые помощники', group=PlatformGroup.objects.get(id=1), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Email', group=PlatformGroup.objects.get(id=2), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='SMS', group=PlatformGroup.objects.get(id=2), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Пуши', group=PlatformGroup.objects.get(id=2), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Мессенджеры', group=PlatformGroup.objects.get(id=2), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Конструктор', group=PlatformGroup.objects.get(id=3), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Персонализация контента', group=PlatformGroup.objects.get(id=3), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Прикрепление файлов', group=PlatformGroup.objects.get(id=3), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Ключевые слова', group=PlatformGroup.objects.get(id=3), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Whatsapp Business API - Провайдеры', group=PlatformGroup.objects.get(id=4), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Оплата WhatsApp Business API', group=PlatformGroup.objects.get(id=4), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Работа с подписчиками', group=PlatformGroup.objects.get(id=5), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Возможности массовых рассылок', group=PlatformGroup.objects.get(id=5), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Каналы массовых рассылок', group=PlatformGroup.objects.get(id=5), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Способы подписки', group=PlatformGroup.objects.get(id=6), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Виджет для сайта', group=PlatformGroup.objects.get(id=6), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Статистика', group=PlatformGroup.objects.get(id=7), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Тарифы', group=PlatformGroup.objects.get(id=8), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Триальный период', group=PlatformGroup.objects.get(id=8), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Особенности оплаты', group=PlatformGroup.objects.get(id=8), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Закрывающие документы', group=PlatformGroup.objects.get(id=9), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Техническая поддержка', group=PlatformGroup.objects.get(id=10), )"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Уровень сложности', group=PlatformGroup.objects.get(id=11), )"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='amoCRM',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='Битрикс24',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='RetailCRM',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='1C Битрикс',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='YClients',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='Мегаплан',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='ЮKassa',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Робокасса',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='ЮMoney',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Prodamus',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Stripe',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Paypal',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Тинькофф',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Fondy',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Wayforpay',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Payonline',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=3), properties='Albato',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=3), properties='Make',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=3), properties='Apiway',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=3), properties='Zapier',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=4), properties='Открытое API',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=4), properties='Webhook',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=5), properties='Алиса',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=5), properties='Маруся',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=5), properties='Aimybox Google Assistant',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=5), properties='Салют',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=6), properties='Мультиканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=6), properties='Омниканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=6), properties='Нет',)"
	
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=7), properties='Мультиканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=7), properties='Омниканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=7), properties='Нет',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=8), properties='Мультиканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=8), properties='Омниканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=8), properties='Нет',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Whatsapp (неофициальный)',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Whatsapp Business API',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Telegram',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Viber',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='ВКонтакте',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Facebook Messenger',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Instagram',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=10), properties='Визуальный редактор',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=10), properties='Линейный редактор',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=10), properties='Готовые шаблоны',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По имени',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По полному имени',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По ID получателя',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По e-mail',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По номеру телефона',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По дате подписки',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По времени подписки',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='Пользовательские переменные',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=12), properties='Изображение',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=12), properties='Видео',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=12), properties='Аудио',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=12), properties='Файл',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Запуск/остановка бота',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Добавление/удаление из авторассылки',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Добавление/удаление метки',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Возможность установить/очистить поле',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Увеличить/уменьшить числовое поле',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Подписка/отписка',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Запустить чат с сотрудником',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Произвольные автоответы',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=14), properties='360Dialog',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=14), properties='EDNA',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=14), properties='Gupshup',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=14), properties='Infobip',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=14), properties='Twilio',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=15), properties='Платформе: Безнал',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=15), properties='Платформе: Российской картой',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=15), properties='Провайдеру: Иностранной картой',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=15), properties='Провайдеру: Безнал иностранное ЮЛ',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=16), properties='Загрузка базы по ID',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=16), properties='Выгрузка базы без ID мессенджеров',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=16), properties='Выгрузка базы с ID Телеграма',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=16), properties='Выгрузка базы с ID ВКонтакте',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=16), properties='Чат-панель',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Текстовые сообщения',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Изображения',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Файлы',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Кнопки-действия',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Кнопки с внешней ссылкой',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Массовый запуск воронок',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='Номерной ВК',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='Номерной Viber',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='Whatsapp неофициальный',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='Whatsapp Business API',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='SMS',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='Пуши',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='Минилендинги',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='ВК-лендинги',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='Приложение ВКонтакте',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='QR-код',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='Deeplink',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='Ключевое слово',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=20), properties='Попап',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=20), properties='Встроенный',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=20), properties='Онлайн-чат',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=21), properties='Есть',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=21), properties='Нет',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=22), properties='Есть бесплатный тариф',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=22), properties='Есть триальный период',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=22), properties='Нет бесплатной версии',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=23), properties='До 3 дней',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=23), properties='До 5 дней',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=23), properties='До 7 дней',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=23), properties='До 10 дней',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=23), properties='До 14 дней',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=24), properties='Безналичный расчёт',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=24), properties='Иностранной картой',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=24), properties='Российской картой',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=25), properties='Предоставляются',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=25), properties='Не предоставляются',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=26), properties='24/7',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=26), properties='Только в рабочее время',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=27), properties='Для новичка',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=27), properties='Для опытного специалиста',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=27), properties='Для профессионала',)"

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


start_db:
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Интеграции',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Каналы',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Функцилнал для настройки чат-ботов',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='WHATSAPP BUSINESS API',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Работа с подписчиками',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Способы подписки',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Статисткика и аналитика',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Тарифы',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Документальное подтверждение',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Техническая поддержка',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformGroup; PlatformGroup.objects.create(title='Уровень сложности',)"
	sleep 3
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='CRM', group=PlatformGroup.objects.get(id=1), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Платежные системы', group=PlatformGroup.objects.get(id=1), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Сервисы-интеграторы', group=PlatformGroup.objects.get(id=1), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Работа с API', group=PlatformGroup.objects.get(id=1), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Голосовые помощники', group=PlatformGroup.objects.get(id=1), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Email', group=PlatformGroup.objects.get(id=2), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='SMS', group=PlatformGroup.objects.get(id=2), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Пуши', group=PlatformGroup.objects.get(id=2), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Мессенджеры', group=PlatformGroup.objects.get(id=2), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Конструктор', group=PlatformGroup.objects.get(id=3), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Персонализация контента', group=PlatformGroup.objects.get(id=3), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Прикрепление файлов', group=PlatformGroup.objects.get(id=3), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Ключевые слова', group=PlatformGroup.objects.get(id=3), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Whatsapp Business API - Провайдеры', group=PlatformGroup.objects.get(id=4), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Оплата WhatsApp Business API', group=PlatformGroup.objects.get(id=4), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Работа с подписчиками', group=PlatformGroup.objects.get(id=5), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Возможности массовых рассылок', group=PlatformGroup.objects.get(id=5), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Каналы массовых рассылок', group=PlatformGroup.objects.get(id=5), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Способы подписки', group=PlatformGroup.objects.get(id=6), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Виджет для сайта', group=PlatformGroup.objects.get(id=6), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Статистика', group=PlatformGroup.objects.get(id=7), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Тарифы', group=PlatformGroup.objects.get(id=8), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Триальный период', group=PlatformGroup.objects.get(id=8), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Особенности оплаты', group=PlatformGroup.objects.get(id=8), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Закрывающие документы', group=PlatformGroup.objects.get(id=9), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Техническая поддержка', group=PlatformGroup.objects.get(id=10), image=b'')"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformFilter, PlatformGroup; PlatformFilter.objects.create(title='Уровень сложности', group=PlatformGroup.objects.get(id=11), image=b'')"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='amoCRM',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='Битрикс24',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='RetailCRM',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='1C Битрикс',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='YClients',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=1), properties='Мегаплан',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='ЮKassa',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Робокасса',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='ЮMoney',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Prodamus',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Stripe',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Paypal',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Тинькофф',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Fondy',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Wayforpay',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=2), properties='Payonline',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=3), properties='Albato',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=3), properties='Make',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=3), properties='Apiway',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=3), properties='Zapier',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=4), properties='Открытое API',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=4), properties='Webhook',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=5), properties='Алиса',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=5), properties='Маруся',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=5), properties='Aimybox Google Assistant',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=5), properties='Салют',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=6), properties='Мультиканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=6), properties='Омниканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=6), properties='Нет',)"
	
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=7), properties='Мультиканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=7), properties='Омниканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=7), properties='Нет',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=8), properties='Мультиканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=8), properties='Омниканально',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=8), properties='Нет',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Whatsapp (неофициальный)',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Whatsapp Business API',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Telegram',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Viber',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='ВКонтакте',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Facebook Messenger',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=9), properties='Instagram',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=10), properties='Визуальный редактор',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=10), properties='Линейный редактор',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=10), properties='Готовые шаблоны',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По имени',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По полному имени',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По ID получателя',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По e-mail',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По номеру телефона',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По дате подписки',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='По времени подписки',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=11), properties='Пользовательские переменные',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=12), properties='Изображение',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=12), properties='Видео',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=12), properties='Аудио',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=12), properties='Файл',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Запуск/остановка бота',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Добавление/удаление из авторассылки',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Добавление/удаление метки',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Возможность установить/очистить поле',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Увеличить/уменьшить числовое поле',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Подписка/отписка',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Запустить чат с сотрудником',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=13), properties='Произвольные автоответы',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=14), properties='360Dialog',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=14), properties='EDNA',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=14), properties='Gupshup',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=14), properties='Infobip',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=14), properties='Twilio',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=15), properties='Платформе: Безнал',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=15), properties='Платформе: Российской картой',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=15), properties='Провайдеру: Иностранной картой',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=15), properties='Провайдеру: Безнал иностранное ЮЛ',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=16), properties='Загрузка базы по ID',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=16), properties='Выгрузка базы без ID мессенджеров',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=16), properties='Выгрузка базы с ID Телеграма',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=16), properties='Выгрузка базы с ID ВКонтакте',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=16), properties='Чат-панель',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Текстовые сообщения',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Изображения',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Файлы',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Кнопки-действия',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Кнопки с внешней ссылкой',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=17), properties='Массовый запуск воронок',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='Номерной ВК',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='Номерной Viber',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='Whatsapp неофициальный',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='Whatsapp Business API',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='SMS',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=18), properties='Пуши',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='Минилендинги',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='ВК-лендинги',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='Приложение ВКонтакте',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='QR-код',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='Deeplink',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=19), properties='Ключевое слово',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=20), properties='Попап',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=20), properties='Встроенный',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=20), properties='Онлайн-чат',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=21), properties='Есть',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=21), properties='Нет',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=22), properties='Есть бесплатный тариф',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=22), properties='Есть триальный период',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=22), properties='Нет бесплатной версии',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=23), properties='До 3 дней',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=23), properties='До 5 дней',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=23), properties='До 7 дней',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=23), properties='До 10 дней',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=23), properties='До 14 дней',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=24), properties='Безналичный расчёт',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=24), properties='Иностранной картой',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=24), properties='Российской картой',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=25), properties='Предоставляются',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=25), properties='Не предоставляются',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=26), properties='24/7',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=26), properties='Только в рабочее время',)"

	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=27), properties='Для новичка',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=27), properties='Для опытного специалиста',)"
	.venv/bin/python3 manage.py shell -c "from platforms.models import PlatformTag, PlatformFilter; PlatformTag.objects.create(title=PlatformFilter.objects.get(id=27), properties='Для профессионала',)"
