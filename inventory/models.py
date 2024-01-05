from django.db import models
from django_jalali.db import models as jmodels

STATUS = [
    ('I', 'Installation'),
    ('O', 'Opt Out'),
    ('D', 'Defective'),
]

class Device(models.Model):
    objects = jmodels.jManager()
    created_date =  jmodels.jDateTimeField(auto_now_add=True)
    receip_date = jmodels.jDateTimeField(null=True, blank=True)
    staff = models.ForeignKey(to='accounts.Staff', on_delete=models.DO_NOTHING)
    device_code = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=1, choices=STATUS)
    recepted = models.BooleanField(null=True)
    installed = models.BooleanField(null=True)

    def __str__(self):
        return self.device_code
