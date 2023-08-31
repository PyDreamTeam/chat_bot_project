from django.db.models import Count, F, Q, Subquery
from django.utils import timezone

from accounts.models import SolutionHistory, SolutionHistoryConfig


def remove_unnecessary_solution_history():
    # Получаем максимальное количество сохраненных записей на одного пользователя
    max_records_subquery = (
        SolutionHistoryConfig.objects.filter(id=1)
        .values("max_view_records")[:1]
    )

    # Получаем список пользователей у которых привешено максимальное количество сохраненных записей
    users_to_exclude = (
        SolutionHistory.objects.values("user_id")
        .annotate(entry_count=Count("id"), max_records=Subquery(max_records_subquery))
        .filter(entry_count__gt=F("max_records"))
    )

    # Получаем список последних сохраненных записей в количестве max_view_records
    ids_to_include = (
        SolutionHistory.objects.order_by("-action_time")
        .values("id")[:max_records_subquery[0]["max_view_records"]]
    )

    # Получаем список истекших сохраненных записей
    expired_records = SolutionHistoryConfig.objects.filter(pk=1)

    # Удаляем истекшие и лишние записи
    SolutionHistory.objects.annotate(
        time_difference=timezone.now() - F("action_time")
    ).filter(
        (
            Q(user_id__in=Subquery(users_to_exclude.values("user_id")))
            & ~Q(id__in=Subquery(ids_to_include.values("id")))
        )
        | Q(time_difference__gte=Subquery(expired_records.values("expiry_period")[:1])
        )
    ).delete()


def add_solution_in_history(*, user_id, solution_id):
    SolutionHistory.objects.create(user_id=user_id, solution_id=solution_id)


def get_solution_history(*, user):
    # Получаем максимальное количество сохраненных записей на одного пользователя
    max_view_records = SolutionHistoryConfig.objects.get(pk=1).max_view_records

    # Получаем историю просмотров готовых решений
    queryset = SolutionHistory.objects.select_related("solution").annotate(
        time_difference=timezone.now() - F('action_time')
    ).filter(
        user=user,
        time_difference__lte=Subquery(
            SolutionHistoryConfig.objects.filter(pk=1)
            .values('expiry_period')[:1]
        )
    ).order_by('-action_time').all()[:max_view_records]
    return queryset
