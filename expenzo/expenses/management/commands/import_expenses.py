import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from expenzo.categories.models import Category
from expenzo.expenses.models import Expense
from expenzo.sections.models import Section


class Command(BaseCommand):
    help = 'Импорт расходов из очищенного CSV'

    def handle(self, *args, **options):
        # Берем первого юзера (обычно это ты/админ)
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('Пользователь не найден!'))
            return

        file_path = 'test_expenses.csv'
        count = 0

        try:
            with open(file_path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Пропускаем пустые строки, если они есть
                    if not row['Сумма'] or not row['Дата']:
                        continue

                    # 1. Получаем/создаем Раздел и Категорию
                    section, _ = Section.objects.get_or_create(
                        name=row['Раздел'].strip(),
                        user=user
                    )
                    category, _ = Category.objects.get_or_create(
                        name=row['Категория'].strip(),
                        user=user
                    )

                    # 2. Очищаем сумму от возможных пробелов (на всякий случай)
                    clean_amount = row['Сумма'].replace(' ', '').replace('\xa0', '')

                    # 3. Создаем запись
                    Expense.objects.create(
                        user=user,
                        category=category,
                        date=datetime.strptime(row['Дата'].strip(), '%Y-%m-%d').date(),
                        description=row['Наименование'].strip(),
                        amount=int(clean_amount)
                    )
                    count += 1

            self.stdout.write(self.style.SUCCESS(f'Успешно импортировано {count} записей!'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Файл {file_path} не найден в корне проекта.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка в строке {count + 1}: {e}'))