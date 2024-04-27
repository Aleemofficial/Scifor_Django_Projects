# views.py

from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

def send_email(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email = EmailMessage(
            subject,
            message,
            'aleemofficial2000@gmail.com',  # Replace with your email address
            [recipient_email],  # List of recipients
            reply_to=['aleemofficial2000@gmail.com'],  # Optional: Reply-to email address
        )
        email.send()

        return HttpResponse('Email sent successfully!')
    else:
        return render(request, 'email_sender/send_email_form.html')
