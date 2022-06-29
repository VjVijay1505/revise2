import imp
from pyexpat import model
from django.forms import ModelForm
from .models import Site, Upload

class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = '__all__'

class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'