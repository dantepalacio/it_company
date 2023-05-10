from .forms import FormContact
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()
        
            template_data = {
                'first_name': form.cleaned_data['first_name'],
                # дополнить другие данные при желании
            }
            msg = render_to_string('email_message/email_answer.html', template_data)
            subject = 'Ответ на заявку'
            sender = settings.EMAIL_HOST_USER
            recipient = form.cleaned_data['email']
            send_mail(subject, msg, sender, [recipient], html_message=msg)

            messages.success(request, "Спасибо за вашу заявку. Ожидайте.") 
            form = FormContact()
    else:
        form = FormContact()
    context= {'form': form}
    return context
