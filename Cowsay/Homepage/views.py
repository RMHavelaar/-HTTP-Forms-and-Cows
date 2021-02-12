from django.shortcuts import render
from django.http import HttpResponse
from Homepage.models import CowsayDisplay
from Homepage.forms import CowsayDisplayForm

import subprocess


def index(request):
    if request.method == 'POST':
        form = CowsayDisplayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            userInputText = data['userInputText']
            cowsayDisplay = data['cowsayDisplay']
            CowsayDisplay.objects.create(
                userInputText = userInputText,
                cowsayDisplay = cowsayDisplay
            )
            bar = subprocess.check_output(
                ["cowsay", '-f',userInputText, cowsayDisplay]).decode('utf-8')
            return render(request, 'index.html', {'form': CowsayDisplayForm,'bar':bar})
    
    form = CowsayDisplayForm()
    return render(request,'index.html', {'form':form})
