from django import forms
from .models import MonthlySchedule
from .models import ColdSurgerySchedule

class MonthlyScheduleForm(forms.ModelForm):
    class Meta:
        model = MonthlySchedule
        fields = ['image']

class ColdSurgeryScheduleForm(forms.ModelForm):
    class Meta:
        model = ColdSurgerySchedule
        fields = ['image']
