from django.shortcuts import render
from . forms import contactForm,studentCheck

def home(req):
    return render(req,'home.html')

from django.shortcuts import render

def about(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')
        return render(req, 'about.html', {'email': email, 'password': password})
    else :
       return render(req, 'about.html')

    
def form(req):
    print(req.POST)
    return render(req,'form.html')

def django_form(req):
    if req.method == "POST":
     form = contactForm(req.POST,req.FILES)
     if form.is_valid():
        file = form.cleaned_data['file']
        img = form.cleaned_data['img']

        with open('for_myself/Upload/' + file.name, 'wb+') as destination:
           for chunk in file.chunks():
              destination.write(chunk)

        with open('for_myself/Upload/' + img.name, 'wb+') as destination:
           for chunk in file.chunks():
              destination.write(chunk)

        print(form.cleaned_data)
        return render(req,'django_form.html', {'form' : form })
    else:
       form = contactForm()

    return render(req,'django_form.html', {'form' : form })


def student_form(req):
  
  if req.method == "POST":
    form = studentCheck(req.POST)

    if form.is_valid():
       print(form.cleaned_data)
  else:
    form = studentCheck()
    
  return render(req,'student.html', {'form' : form})