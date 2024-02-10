from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, send_mass_mail, EmailMessage, BadHeaderError
# Create your views here.


def welcome(request):
    return HttpResponse("welcome to django")


def hello_user(request, name):
    try:
        message = f"hello {name}, you have posting rubbish on our platform, we will ban you"
        mail = EmailMessage("warning", message, 'complaints@tweeta.com', ['seyi69@tweeta.com'])
        mail.attach_file('playground/static/images/nelson-mandela.jpeg')
        mail.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {"name": name})
