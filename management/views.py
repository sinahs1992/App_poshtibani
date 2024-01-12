from django.shortcuts import render, redirect
from accounts.models import Staff
from django.contrib import messages
from inventory.models import Device
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from jdatetime import datetime
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('accounts.view_admin_page', raise_exception=True)
def management_select_page(request):
    try:
        context = {}
        return render(request, 'management/origin.html', context)
    except PermissionDenied:
        messages.error(request, "You do not have permission to view this page.")
        return redirect('inventory:index')


@login_required
@permission_required('accounts.view_admin_page', raise_exception=True)
def allocation_page(request):
    try:
        all_staffs = Staff.objects.filter(user_type='S')
        all_devices = Device.objects.all().order_by('-created_date')
        now = datetime.now()
        context = {'all_staffs': all_staffs, 'all_devices': all_devices, 'now':now}
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
    except PermissionDenied:
        messages.error(request, "You do not have permission to view this page.")
        return redirect('inventory:index')


@login_required
@permission_required('accounts.view_admin_page', raise_exception=True)
def inventory_page(request):
    try:
        all_staffs = Staff.objects.filter(user_type='S')
        now = datetime.now()
        all_devices = Device.objects.all().order_by('-created_date')
        context = {'all_devices': all_devices, 'now':now, 'all_staffs': all_staffs}
        if request.method == "POST":
            staff_id = request.POST.get('staff-name')
            sn = request.POST.get('sn')
            print(staff_id)
            print(sn)
            if staff_id and sn:
                try:
                    staff = Staff.objects.get(id=staff_id)
                    Device.objects.create(staff=staff, device_code=sn, status='I')
                    messages.success(request, 'دستگاه نصبی با موفقیت ثبت شد.')
                    return render(request, 'management/inventory.html', context)
                except Staff.DoesNotExist:
                     messages.error(request, 'پشتیبان مورد نظر یافت نشد.')
            else:
                messages.error(request, 'لطفاً تمام فیلدها را پر کنید.')
        return render(request, 'management/inventory.html', context)
    except PermissionDenied:
        messages.error(request, "You do not have permission to view this page.")
        return redirect('inventory:index')

@login_required
@permission_required('accounts.view_admin_page', raise_exception=True)
def recepted(request, device_code):
    try:
        device = Device.objects.get(device_code=device_code)
        device.recepted = True
        device.receip_date = timezone.now()
        device.save()
    except PermissionDenied:
        messages.error(request, "You do not have permission to view this page.")
        return redirect('inventory:index')    
    except Device.DoesNotExist:
        messages.error(request, 'دستگاه مورد نظر در دسترس نیست.')
    return HttpResponseRedirect(reverse('management:inventory-page'))



@login_required
@permission_required('accounts.view_admin_page', raise_exception=True)
def installed(request, device_code):
    try:
        device = Device.objects.get(device_code=device_code)
        device.installed = True
        device.receip_date = timezone.now()
        device.save()
    except PermissionDenied:
        messages.error(request, "You do not have permission to view this page.")
        return redirect('inventory:index')    
    except Device.DoesNotExist:
        print('device does not exist')
        messages.error(request, 'دستگاه مورد نظر در دسترس نیست.')
        return redirect('inventory:index')
    return HttpResponseRedirect(reverse('management:allocation-page'))


def permission_denied_view(request, exception):
    messages.error(request, "You do not have permission to view this page.")
    return redirect('inventory:index')
