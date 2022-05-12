from django import forms
from .models import SiteData


class SiteCreateForm(forms.ModelForm):
  class Meta:
    model = SiteData
    fields = ('created_user','site_data')
