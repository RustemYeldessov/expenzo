#!/usr/bin/env bash
# exit on error
set -o errexit

# Установка зависимостей
pip install -r requirements.txt

# Сборка статических файлов (CSS, JS)
python manage.py collectstatic --no-input

# Применение миграций в базу данных Neon
python manage.py migrate