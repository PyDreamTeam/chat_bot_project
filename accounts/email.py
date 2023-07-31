from djoser.email import ActivationEmail as BaseActivationEmail
from djoser.email import ConfirmationEmail as BaseConfirmationEmail
from djoser.email import PasswordResetEmail as BasePasswordResetEmail
from djoser.email import PasswordChangedConfirmationEmail as BasePasswordChangedConfirmationEmail
from djoser.email import UsernameChangedConfirmationEmail as BaseUsernameChangedConfirmationEmail
from djoser.email import UsernameResetEmail as BaseUsernameResetEmail


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
    
    