from django.shortcuts import render, redirect
from inventory.models import Device
from django.db.models import Q
from jdatetime import datetime
from django.contrib import messages

from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request, 'inventory/index.html')

@login_required
@permission_required('accounts.view_staff_page', raise_exception=True)
def staff_page(request):
    try:
        rows = Device.objects.filter(Q(recepted=None) & Q(installed=None), staff=request.user).order_by('-created_date')
        now = datetime.now()
        context = {'rows':rows, 'now':now}
        if request.method == "POST":
            staff = request.user.staff
            sn = request.POST.get('sn')
            if staff and sn:
                Device.objects.create(staff=staff, device_code=sn, status='O')
                messages.success(request, 'دستگاه نصبی با موفقیت ثبت شد.')
                return render(request, 'inventory/job.html', context)
            else:
                messages.error(request, 'لطفاً تمام فیلدها را پر کنید.')
                return render(request, 'inventory/job.html', context)

        return render(request, 'inventory/job.html', context)
    except PermissionError:
        messages.error(request, "You do not have permission to view this page.")
        return redirect('inventory:index')

