from django.shortcuts import render
from inventory.models import Device
from django.db.models import Q
from jdatetime import datetime

from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request, 'inventory/index.html')

@login_required
@permission_required('accounts.view_staff_page', raise_exception=True)
def staff_page(request):

    rows = Device.objects.filter(Q(recepted=None) | Q(installed=None), staff=request.user)
    now = datetime.now()
    context = {'rows':rows, 'now':now}
    return render(request, 'inventory/job.html', context)
