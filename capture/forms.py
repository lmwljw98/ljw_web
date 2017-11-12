from django.forms import ModelForm
from .models import Capture, Export

class Captureform(ModelForm):
    class Meta:
        model = Capture
        fields = ('imglink',)

class Exportform(ModelForm):
    class Meta:
        model = Export
        fields = ('src',)