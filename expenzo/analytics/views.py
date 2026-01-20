from django.utils import timezone

from django.shortcuts import render

from expenzo.expenses.models import Expense
from django.db.models import Sum, Count, Max, Avg


def expenses_statistics_view(request):
    today = timezone.now().date()
    count_today = Expense.objects.filter(date=today).count()
    sum_today = Expense.objects.filter(date=today).aggregate(total=Sum('amount'))['total'] or 0
    total_count = Expense.objects.count()

    context = {
        'count_today': count_today,
        'sum_today': sum_today,
        'total_count': total_count,
        'today': today,
    }

    return render(request, 'analytics/statistics.html', context)
