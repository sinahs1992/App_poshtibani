from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE = [
    ('A', 'Administrator'),
    ('AM', 'Allocation Manager'),
    ('WM', 'Warehouse Manager'),
    ('S', 'Staff'),
]


class User(AbstractUser):
    national_id = models.CharField(max_length=10)
    user_type = models.CharField(max_length=2, choices=USER_TYPE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ("view_staff_page", "Can view staff page"),
        ]

class Staff(User):
    staff_code = models.CharField(max_length=255)



class AllocationManager(User):
    pass

class WarehouseManager(User):
    pass