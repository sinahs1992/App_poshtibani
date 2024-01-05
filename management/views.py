from django.shortcuts import render
from accounts.models import Staff
from django.contrib import messages
from inventory.models import Device


def management_select_page(request):
    context = {}
    return render(request, 'management/origin.html', context)


def allocation_page(request):
    all_staffs = Staff.objects.filter(user_type='S')
    all_devices = Device.objects.all().order_by('-created_date')
    context = {'all_staffs': all_staffs, 'all_devices': all_devices}
    if request.method == "POST":
        staff_id = request.POST.get('staff-name')
        sn = request.POST.get('sn')
        if staff_id and sn:
            try:
                staff = Staff.objects.get(pk=staff_id)
                Device.objects.create(staff=staff, device_code=sn, status='D')
                messages.success(request, 'دستگاه معیوب با موفقیت ثبت شد.')
                return render(request, 'management/allocation.html', context)
            except Staff.DoesNotExist:
                messages.error(request, 'پشتیبان مورد نظر یافت نشد.')
        else:
            messages.error(request, 'لطفاً تمام فیلدها را پر کنید.')

    return render(request, 'management/allocation.html', context)

def inventory_page(request):
    all_devices = Device.objects.all().order_by('-created_date')
    context = {'all_devices': all_devices}
    return render(request, 'management/inventory.html', context)