import os
from time import sleep

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db.models import Count
from django.test import TestCase
from django.urls import reverse

from accounts.models import Role, SolutionHistory
from accounts.services import (
    add_solution_in_history,
    remove_unnecessary_solution_history,
)
from tests import FIXTURES_PATH
from tests.mixins import AuthTestMixin

pytestmark = [pytest.mark.django_db]


class RemoveUnnecessarySolutionHistoryTestCase(AuthTestMixin, TestCase):
    fixtures = (
        os.path.join(FIXTURES_PATH, "solution.json"),
        os.path.join(FIXTURES_PATH, "solutionhistoryconfig_2.json"),
    )

    def setUp(self):
        self.password = "12345qwerty"
        hash_password = make_password(self.password)
        self.user = get_user_model().objects.create(
            first_name=f"user",
            last_name=f"user",
            email=f"user@mail.com",
            user_role=Role.superadmin,
            password=hash_password,
            get_email_notifications=False,
        )

    def test_remove_unnecessary_solution_history(self):
        # Проверяем удаляются ли данные по истечению их срока действия
        for indx in range(1, 201):
            add_solution_in_history(user_id=self.user.id, solution_id=indx)

        sleep(1)

        row_count = SolutionHistory.objects.aggregate(count=Count("*"))["count"]
        self.assertEqual(row_count, 200)

        remove_unnecessary_solution_history()

        row_count = SolutionHistory.objects.aggregate(count=Count("*"))["count"]
        self.assertEqual(row_count, 0)

        # Получаем токен для пользователя и увеличиваем срок действия
        headers = self.get_headers_for_auth(self.user.email, self.password)
        self.client.post(
            reverse("history-solutions-expiry-period"),
            {"expiry_period": "01:00:00"},
            **headers,
        )

        # Проверяем удаляются ли лишние строки в истории
        for indx in range(1, 201):
            add_solution_in_history(user_id=self.user.id, solution_id=indx)

        row_count = SolutionHistory.objects.aggregate(count=Count("*"))["count"]
        self.assertEqual(row_count, 200)

        remove_unnecessary_solution_history()

        row_count = SolutionHistory.objects.aggregate(count=Count("*"))["count"]
        self.assertEqual(row_count, 40)
