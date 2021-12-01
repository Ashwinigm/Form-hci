from django.forms import ModelForm
from .models import NewForm 
class ContentForm(ModelForm):
    class Meta:
        model = NewForm
        fields = "__all__" 