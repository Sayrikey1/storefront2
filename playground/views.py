from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage

# def say_hello(request):
#     try:
#         send_mail('subject', 'the message', 'octavedev01@gmail.com', ['kamalseriki49@gmail.com'])
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Mosh'})

def say_hello(request):
    try:
        
        message = BaseEmailMessage()

    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
