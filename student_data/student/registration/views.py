from django.shortcuts import render,redirect
from .models import Student

from django.urls import reverse
from urllib.parse import urlencode

from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def homepage(request):
    return render(request, template_name="registration/registration.html")

def data_encrypt(data):
    encData = fernet.encrypt(data.encode())
    return encData

def data_decrypt(encData):
    decData = fernet.decrypt(encData).decode()
    return decData

def StudentRegistration(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('phone')
        s_class=request.POST.get('class')
        encmobile = data_encrypt(mobile)
        encemail = data_encrypt(email)
        student=Student(name=name,email=encemail,mobile=encmobile,s_class=s_class)
        student.save()
        decMobile = data_decrypt(encmobile)
        decEmail = data_decrypt(encemail)
        subject = 'welcome to AhaGuru '
        message = f'Hi {student.name, student.id}, thank you for registering in student portal.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [decEmail, ]
        send_mail(subject, message, email_from, recipient_list)
        base_url = reverse('dashboard')
        query_string = urlencode({'student': student.id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
    else:
        return render(request, template_name="registration/registration.html")


def dashboard(request):
    if request.method == 'GET':
        id = request.GET.get('student')
        student = Student.objects.filter(id=id)
        context = {'student':student}
        return render(request, template_name="registration/dashboard.html", context=context)
