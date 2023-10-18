import os

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.test import TestCase

from accounts.email import EmailSender
from accounts.models import ALL_ROLES
from tests import FIXTURES_PATH
from tests.mixins import AuthTestMixin

pytestmark = [pytest.mark.django_db]


class EmailSenderTestCase(AuthTestMixin, TestCase):
    fixtures = (os.path.join(FIXTURES_PATH, "order.json"),)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email_sender = None
        self.invalid_roles = ()

    def setUp(self):
        self.email_sender = EmailSender()
        self.invalid_roles = tuple(
            str(role) for role in ALL_ROLES if role not in self.email_sender.VALID_ROLES
        )

        for role in ALL_ROLES:
            password = "12345qwerty"
            hash_password = make_password(password)
            get_user_model().objects.create(
                first_name=f"user",
                last_name=f"user",
                email=f"{role}@mail.com",
                user_role=role,
                password=hash_password,
                get_email_notifications=False,
            )

    def test_get_order_data(self):
        order = self.email_sender._get_order_data(order_id=1)
        self.assertIsInstance(order, dict)
        self.assertSetEqual(
            set(order.keys()), {"first_name", "phone_number", "comment", "email"}
        )

        for field in order:
            self.assertIsInstance(field, str)

        try:
            validate_email(order["email"])
        except ValidationError:
            pytest.fail(
                f"Email '{order['email']}' не должен вызывать ошибку валидации."
            )

    def test_get_email_for_sending(self):
        emails = self.email_sender._get_email_for_sending()
        self.assertIsInstance(emails, list)

        try:
            for email in emails:
                self.assertIsInstance(email, str)
                validate_email(email)
        except ValidationError:
            pytest.fail(f"Email '{email}' не должен вызывать ошибку валидации.")

        test_roles = tuple(role.rstrip("@mail.com") for role in emails)
        for role in test_roles:
            self.assertNotIn(role, self.invalid_roles)
