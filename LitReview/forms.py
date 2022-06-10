from django.forms import BaseModelForm
from django.forms.models import ModelFormMetaclass


class ModelForm(BaseModelForm, metaclass=ModelFormMetaclass):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

