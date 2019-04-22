from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
    return render(request,'Createacc/createacc.html')


def form_name_view(request):
    form = forms.FormName()
    if(request.method == 'POST'):
        form = forms.FormName(request.POST)

        if(form.is_valid()):
            print("Valid")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['contact'])

    else:
        print("Not post")

    return render(request,'Createacc/createacc.html',{'form':form})
