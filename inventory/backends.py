# backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class NationalIDBackend(ModelBackend):
    def authenticate(self, request, national_id=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(national_id=national_id)
        except UserModel.DoesNotExist:
            return None

        if user and user.check_password(password):
            return user
        return None
