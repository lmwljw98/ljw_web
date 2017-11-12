from django.forms import ModelForm
from .models import Mydata

class Linkform(ModelForm):
    class Meta:
        model = Mydata
        fields = ('code', 'page', )