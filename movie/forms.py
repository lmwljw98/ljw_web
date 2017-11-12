from django.forms import ModelForm
from .models import Tv_choice

class Tform(ModelForm):

    class Meta:
        model = Tv_choice
        fields = ('tv', 'num', )