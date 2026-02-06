import json

from django.contrib.auth import get_user_model

from expenzo.expenses.models import Expense
from expenzo.categories.models import Category
from expenzo.sections.models import Section

User = get_user_model()

def run_import():
    target_username = 'rus_yeldessov'

    try:
        user = User.objects.get(username=target_username)
    except User.DoesNotExist:
        print(f"Ошибка: пользователь '{target_username}' не найдет в базе")
        return

    with open('test_json_expenses.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        # 1. Получаем или создаем Раздел (Section)
        section_name = item.get('Section', 'Стандартные расходы')
        section, _ = Section.objects.get_or_create(name=section_name)

        # 2. Получаем или создаем Категорию (Category)
        # Важно: передаем section и в категорию, если она там нужна
        category_name = item.get('Category', 'Прочее')
        category, _ = Category.objects.get_or_create(
            name=category_name,
            defaults={'section': section}
        )

        # 3. Создаем расход
        # Добавляем section_id (или section=section), чтобы избежать ошибки NOT NULL
        Expense.objects.create(
            date=item['Date'],
            description=item['Description'],
            amount=item['Amount'],
            category=category,
            section=section,
            user=user
        )

    print(f"Успешно импортировано {len(data)} записей!")

if __name__ == "__main__":
    run_import()