from django import forms
from .models import TextModel
from django.utils.translation import ugettext_lazy as _


# class TextBubbleWizardForm(forms.ModelForm):
#     class Meta:
#         model = TextModel    # change this to something correct
#         fields = ['title', 'text']
#         # exclude = []


class BubbleWizardForm(forms.Form):
    title = forms.CharField(label=_('Title wqerewq:'), max_length=100, required=False)
    content = forms.CharField(label='Content sadfdsaf:', max_length=1000, widget=forms.Textarea)
