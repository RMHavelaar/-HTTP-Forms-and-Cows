from django import forms
from django.utils import timezone

import subprocess

CowsaySubProcess = subprocess.check_output(
    ["cowsay", '-l']).decode('utf-8').split()[4:]

CowsayMessageHistory = list(zip(CowsaySubProcess, CowsaySubProcess))

class CowsayDisplayForm(forms.Form):
    userInputText = forms.CharField(max_length = 100)
    cowsayDisplay = forms.CharField(widget = forms.Select(choices=CowsayMessageHistory))
    publishDate = forms.DateTimeField()
