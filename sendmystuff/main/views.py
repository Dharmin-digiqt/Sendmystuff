from django.shortcuts import render
from .models import Contact, About, MoreAbout


# Create your views here.
def home(request):
    return render(request, 'front/home.html')


def master(request):
    return render(request, 'front/master.html')


def signup(request):
    return render(request, 'front/signup.html')


def driver(request):
    return render(request, 'front/driver.html')


def contact(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        con = Contact(name=name, subject=subject, email=email, message=message)
        con.save()
        thank = True
    return render(request, 'front/contact.html', {'thank': thank})


def about(request):
    # web_about = About.objects.get(pk=1)
    return render(request, 'front/about.html')


def service(request):
    return render(request, 'front/service.html')


def forms(request):
    return render(request, 'front/form.html')

def forms2(request):
    return render(request, 'front/form2.html')
