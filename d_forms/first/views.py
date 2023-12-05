from django.shortcuts import render
from . forms import PracticeForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def form(request):
    if request.method == 'POST':
        django_form = PracticeForm(request.POST,  request.FILES)
        if django_form.is_valid():
            data = django_form.cleaned_data
            print(data)
    else:
        django_form = PracticeForm()
    return render(request, 'form.html', {'form': django_form})

