from django.core.mail import send_mail
from django.db.models import Value, F, Func, JSONField
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from djoser.email import ActivationEmail as BaseActivationEmail
from djoser.email import ConfirmationEmail as BaseConfirmationEmail
from djoser.email import PasswordResetEmail as BasePasswordResetEmail
from djoser.email import PasswordChangedConfirmationEmail as BasePasswordChangedConfirmationEmail
from djoser.email import UsernameChangedConfirmationEmail as BaseUsernameChangedConfirmationEmail
from djoser.email import UsernameResetEmail as BaseUsernameResetEmail

from accounts.models import User, Role
from config import settings
from orders.models import Order


class ActivationEmail(BaseActivationEmail):
    template_name = "activation.html"


class ConfirmationEmail(BaseConfirmationEmail):
    template_name = 'confirmation.html'
    
    
class PasswordResetEmail(BasePasswordResetEmail):
    template_name = "password_reset.html"
    

class PasswordChangedConfirmationEmail(BasePasswordChangedConfirmationEmail):
    template_name = "password_changed_confirmation.html"


class UsernameChangedConfirmationEmail(BaseUsernameChangedConfirmationEmail):
    template_name = "username_changed_confirmation.html"


class UsernameResetEmail(BaseUsernameResetEmail):
    template_name = "username_reset.html"


class EmailSender:
    USER_MODEL = User
    ORDER_MODEL = Order
    HTML_TEMPLATE = "new_order.html"
    VALID_ROLES = (Role.admin, Role.superadmin, Role.manager)

    def send_message_when_new_order(self, order_id):
        order = self._get_order_data(order_id)
        emails = self._get_email_for_sending()
        html_message = render_to_string(self.HTML_TEMPLATE, context={"order": order})
        plain_message = strip_tags(html_message)
        send_mail(
            subject="New order",
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails,
            fail_silently=False,
            auth_user=None,
            auth_password=None,
            connection=None,
            html_message=html_message,
        )

    def _get_order_data(self, order_id):
        data = (
            self.ORDER_MODEL.objects.annotate(
                json_object=Func(
                    Value("first_name"), F("first_name"),
                    Value("phone_number"), F("phone_number"),
                    Value("comment"), F("comment"),
                    Value("email"), F("email"),
                    function="jsonb_build_object",
                    output_field=JSONField(),
                )
            )
            .values("json_object")
            .get(pk=order_id)["json_object"]
        )
        return data

    def _get_email_for_sending(self):
        emails = list(
            self.USER_MODEL.objects
            .filter(user_role__in=self.VALID_ROLES)
            .values("email")
            .values_list("email", flat=True)
        )
        return emails
