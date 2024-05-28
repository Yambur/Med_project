from users.forms import StyleFormMixin
from .models import *
from django import forms


class AppointmentForm(forms.ModelForm, StyleFormMixin):
    readonly_fields = ('doctor', 'diagnostic')

    class Meta:
        model = Appointment
        fields = ('user',)
