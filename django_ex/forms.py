from django.contrib.auth import forms

from .models import MyUser, Ceo, Score


# class CeoForm(forms.Form):
#     ITEM_FIELDS_CHOICES = ('기술분야', 'BM분야')
#     WORK_FIELDS_CHOICES = ('제조업', '서비스업')
#     SETUP_FIELDS_CHOICES = ('기창업', '창업')
#
#     item_fields = forms.CharField(wiget=forms.RadioSelect, choices=ITEM_FIELDS_CHOICES, required=True)
#     work_fields = forms.CharField(wiget=forms.RadioSelect, choices=WORK_FIELDS_CHOICES, required=True)
#     setup_fields = forms.CharField(wiget=forms.RadioSelect, choices=SETUP_FIELDS_CHOICES, required=True)
