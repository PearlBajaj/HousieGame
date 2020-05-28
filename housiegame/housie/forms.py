from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit,Fieldset,ButtonHolder
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions)
from django.db import models
from .models import Player

class PlayerForm(forms.Form):
    player_name = forms.CharField(label="Name",required=True, max_length = 16)
    player_email = forms.EmailField(label="Email",required=True, max_length=254)
    player_no_tickets = forms.IntegerField(label = "No. Tickets")
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        'player_name',
        'player_email',
        'player_no_tickets',
        FormActions(Submit('Save','Save', css_class='btn-primary'))
    )
