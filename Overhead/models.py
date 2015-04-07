from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=255)
    system_name = models.CharField(max_length=255)
    can_approve = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(UserType)

    @staticmethod
    def get_by_user(user):
        prof = UserProfile.objects.filter(user=user.id).first()
        return prof
