from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MonthlySchedule
from .forms import MonthlyScheduleForm
from .models import ColdSurgerySchedule
from .forms import ColdSurgeryScheduleForm

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')  # غيّر الرابط حسب وجهتك بعد تسجيل الدخول
        else:
            return render(request, 'login.html', {'error': 'اسم المستخدم أو كلمة المرور غير صحيحة'})

    return render(request, 'login.html')

@login_required
def home(request):
    if request.method == "POST":
        selected = request.POST.get('department')
        if selected == "جراحة فكية":
            return redirect('jaw_surgery')  # هذا هو اسم المسار الذي سنعرفه
    return render(request, 'home.html')
@login_required
def jaw_surgery_view(request):
    return render(request, 'jaw_surgery.html')

def jaw_surgery_view(request):
    return render(request, 'jaw_surgery.html')


@login_required
def cold_operations_view(request):
    schedule = ColdSurgerySchedule.objects.last()
    is_owner = request.user.username == 'M'

    if request.method == 'POST' and is_owner:
        form = ColdSurgeryScheduleForm(request.POST, request.FILES, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('cold_operations')
    else:
        form = ColdSurgeryScheduleForm(instance=schedule)

    context = {
        'schedule': schedule,
        'form': form,
        'is_owner': is_owner,
    }
    return render(request, 'cold_operations.html', context)


def hot_operations_view(request):
    return render(request, 'hot_operations.html')



@login_required
def monthly_schedule_view(request):
    schedule = MonthlySchedule.objects.first()
    user_is_m = request.user.username == 'M'

    # حذف الجدول
    if request.method == "POST" and 'delete' in request.POST and user_is_m:
        if schedule:
            schedule.image.delete()
            schedule.delete()
        return redirect('monthly_schedule')

    # رفع أو تعديل
    if request.method == "POST" and user_is_m:
        form = MonthlyScheduleForm(request.POST, request.FILES, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('monthly_schedule')
    else:
        form = MonthlyScheduleForm(instance=schedule)

    return render(request, 'monthly_schedule.html', {
        'schedule': schedule,
        'form': form,
        'user_is_m': user_is_m,
    })
