from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
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
        
        message = BaseEmailMessage(
            template_name = 'emails/hello.html',
            context = {'name': 'Kamal'}
        ) 
        message.send(['octavedev01@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})


# docker run -d -p 6379:6379 redis