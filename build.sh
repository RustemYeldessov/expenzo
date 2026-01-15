#!/usr/bin/env bash
# exit on error
set -o errexit

# Установка зависимостей
pip install -r requirements.txt

# Сборка статических файлов (CSS, JS)
python manage.py collectstatic --no-input

# Применение миграций в базу данных Neon
python manage.py migrate

python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'MyExpenzo2026!')"