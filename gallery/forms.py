from django.forms import ModelForm
from .models import Photo

class Gform(ModelForm):
    class Meta:
        model = Photo
        fields = ('start', 'end', )