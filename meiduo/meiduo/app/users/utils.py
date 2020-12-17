from django.contrib.auth.backends import ModelBackend
import re
from users.models import User
def get_user_by_account(account):
    try:
        if re.match(r'^1[3-9]/d{9}', account):
            User.objects.get(mobile=account)
        else:
            user = User.objects.get(username=account)

    except User.DoesNotExist:
            return None
    else:
        return user

class UsernameMobileBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user=get_user_by_account(username)
        if user and user.check_password(password):
            return user
        else:
            return None