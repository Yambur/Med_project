from .models import *
from django import forms


class AppointmentForm(forms.ModelForm):
    readonly_fields = ('doctor', 'diagnostic')

    class Meta:
        model = Appointment
        fields = ('user',)
