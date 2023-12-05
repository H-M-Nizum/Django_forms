from django.shortcuts import render

from first.forms import studentForm
# Create your views here.
def model_form(request):
   
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = studentForm()
    return render(request, 'home.html', {'form': form}) 