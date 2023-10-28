import os

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse

from accounts.models import ALL_ROLES
from accounts.permissions import IsAdminOrSuperAdmin
from tests import FIXTURES_PATH
from tests.mixins import AuthTestMixin

pytestmark = [pytest.mark.django_db]


class HistorySolutionConfigTestCaseMixin(AuthTestMixin):
    fixtures = (
        os.path.join(FIXTURES_PATH, "solution.json"),
        os.path.join(FIXTURES_PATH, "solutionhistoryconfig.json"),
    )
    URL_NAME = None
    FIELD = None
    INITIAL_VALUE = None
    FINALLY_VALUE = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_users = []
        self.INITIAL_REQUEST_BODY = {self.FIELD: self.INITIAL_VALUE}
        self.FINALLY_REQUEST_BODY = {self.FIELD: self.FINALLY_VALUE}
        self.url = reverse(self.URL_NAME)

    def setUp(self):
        # Создаем по пользователю на каждую роль
        for indx, role in enumerate(ALL_ROLES):
            password = f"12345qwerty{indx}"
            hash_password = make_password(password)
            usr = get_user_model().objects.create(
                first_name=f"user{indx}",
                last_name=f"user{indx}",
                email=f"user{indx}@mail.com",
                user_role=role,
                password=hash_password,
                get_email_notifications=False,
            )
            self.test_users.append((usr, password))

    def test_role_access(self):
        for usr, pswd in self.test_users:
            # Получаем токен для очередного пользователя
            headers = self.get_headers_for_auth(usr.email, pswd)
            # Если роль пользователя дает пользователю полномочия
            if usr.user_role in IsAdminOrSuperAdmin.VALID_ROLES:
                # Получаем по GET запросу исходное значение поля в таблице
                initial_response = self.client.get(self.url, **headers)
                self.assertEqual(initial_response.status_code, 200)

                # Изменяем POST запросом значение поля в таблице
                response = self.client.post(
                    self.url, self.FINALLY_REQUEST_BODY, **headers
                )
                self.assertEqual(response.status_code, 200)

                # Получаем по GET запросу измененное значение поля в таблице
                finally_response = self.client.get(self.url, **headers)
                self.assertEqual(finally_response.status_code, 200)
                self.assertNotEquals(
                    initial_response.json()[self.FIELD],
                    finally_response.json()[self.FIELD],
                )
                self.assertEqual(
                    self.FINALLY_VALUE, finally_response.json()[self.FIELD]
                )

                # Сбрасываем настройки до изначальных
                self.client.post(self.url, self.INITIAL_REQUEST_BODY, **headers)
            else:  # Если роль пользователя НЕ дает пользователю полномочия
                initial_response = self.client.get(self.url, **headers)
                self.assertEqual(initial_response.status_code, 403)

                response = self.client.post(
                    self.url, self.FINALLY_REQUEST_BODY, **headers
                )
                self.assertEqual(response.status_code, 403)

    def test_unauthenticated_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

        response = self.client.post(self.url, self.FINALLY_REQUEST_BODY)
        self.assertEqual(response.status_code, 401)

        # Проверям не поменялось ли значение поля в таблице
        # Получаем токен для пользователя-админа
        usr, pswd = [
            (usr, pswd)
            for (usr, pswd) in self.test_users
            if usr.user_role in IsAdminOrSuperAdmin.VALID_ROLES
        ][0]

        data = {"email": usr.email, "password": pswd}
        response = self.client.post("/api/auth/jwt/create", data)
        token = response.json()["access"]
        headers = {
            "HTTP_CONTENT_TYPE": "application/json",
            "HTTP_AUTHORIZATION": f"JWT {token}",
        }
        finally_response = self.client.get(self.url, **headers)
        self.assertNotEquals(
            self.FINALLY_VALUE,
            finally_response.json()[self.FIELD],
        )
        self.assertEqual(self.INITIAL_VALUE, finally_response.json()[self.FIELD])


class ExpiryPeriodTestCase(HistorySolutionConfigTestCaseMixin, TestCase):
    URL_NAME = "history-solutions-expiry-period"
    FIELD = "expiry_period"
    INITIAL_VALUE = "00:10:00"
    FINALLY_VALUE = "00:00:20"


class MaxViewRecordsTestCase(HistorySolutionConfigTestCaseMixin, TestCase):
    URL_NAME = "history-solutions-max-view-records"
    FIELD = "max_view_records"
    INITIAL_VALUE = 40
    FINALLY_VALUE = 20
