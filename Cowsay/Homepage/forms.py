from django import forms
from django.utils import timezone

import subprocess

# I don't know how or why but the first few selections are local files....
CowsaySubProcess = subprocess.check_output(
    ["cowsay", '-l']).decode('utf-8').split()
activeAvatar = list(zip(CowsaySubProcess, CowsaySubProcess))


# Found out cowsay has a ton of avatar and implemented them into the app with a choice field
class CowsayDisplayForm(forms.Form):
    userInputText = forms.CharField(max_length = 100, label='What would you like to say?')
    cowsayDisplay = forms.CharField(widget = forms.Select(choices=activeAvatar), label='Choose your Avatar')
    # publishDate = forms.DateTimeField()
