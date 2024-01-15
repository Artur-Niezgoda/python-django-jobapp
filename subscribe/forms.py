

from django import forms

from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=100)

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        labels={
            'first_name': _('Enter first name'),
            'last_name': _('Enter last name'),
            'email': _('Enter email address'),
        }
        error_messages={
            'first_name':{
                'required': _('You cannot move forward without entering a name.'),
            }
        }
        