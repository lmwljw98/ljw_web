from django.forms import ModelForm
from .models import Input

class Inputform(ModelForm):

    class Meta:

        model = Input
        fields = ('input',)
