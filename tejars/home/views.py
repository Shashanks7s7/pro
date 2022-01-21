from .models import Blogs, Messages, Team
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail


# Create your views here.


def home(request):

    team_list = Team.objects.all()
    blog_list=Blogs.objects.all()
    # send an email
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ['subedishashank2@gmail.com'],
            fail_silently=False
        )
        message_update = Messages(
            name=message_name, message=message, senderemail=message_email)
        message_update.save()

        return render(request, 'home.html', {"teamlist": team_list,"bloglist":blog_list})

    else:
        return render(request, 'home.html', {"teamlist": team_list,"bloglist":blog_list})


def extra(request):
    
    return render(request, 'indu.html', {})

def blogdetails(request):
    blog_list=Blogs.objects.all()
    return render(request,'blog-details.html')
   
