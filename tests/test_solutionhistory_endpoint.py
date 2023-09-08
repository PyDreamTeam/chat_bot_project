import os
from random import shuffle

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse

from accounts.models import Role
from accounts.services import add_solution_in_history
from tests import FIXTURES_PATH
from tests.mixins import AuthTestMixin

pytestmark = [pytest.mark.django_db]


class HistorySolutionTestCase(AuthTestMixin, TestCase):
    fixtures = (
        os.path.join(FIXTURES_PATH, "solution.json"),
        os.path.join(FIXTURES_PATH, "solutionhistoryconfig.json"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_users = []
        self.url = reverse('history-solutions')

    def setUp(self):
        # Создаем пользователей
        for indx in range(10):
            password = f"12345qwerty{indx}"
            hash_password = make_password(password)
            usr = get_user_model().objects.create(
                first_name=f"user{indx}",
                last_name=f"user{indx}",
                email=f"user{indx}@mail.com",
                user_role=Role.user,
                password=hash_password,
                get_email_notifications=False,
            )

            history_ordering = list(range(2, 42))
            shuffle(history_ordering)

            self.test_users.append((usr, password, history_ordering))

    def test_unauthenticated_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    def test_history_ordering(self):
        # Имитируем просмотры
        for usr, _, hst_ord in self.test_users:
            for indx in hst_ord:
                add_solution_in_history(user_id=usr.id, solution_id=indx)

        for usr, pswd, hst_ord in self.test_users:
            headers = self.get_headers_for_auth(usr.email, pswd)
            response = self.client.get(self.url, **headers)
            data = [dct["id"] for dct in response.json()["results"]]
            hst_ord.reverse()
            self.assertEqual(data, hst_ord)
