from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormContact, RequestReviewForm
from .models import *
from django.contrib import messages
from django.views.generic import ListView, DetailView, View
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _, get_language


# def ds(request):
# 	out = _('news')
# 	print(out)
# 	return render(request, 'home_page.html')

# def contact(request):
#     if request.method == 'POST':
#         form = FormContact(request.POST)
#         if form.is_valid():
#             form.save()
		
#             template_data = {
#                 'first_name': form.cleaned_data['first_name'],
#                 # дополнить другие данные при желании
#             }
#             msg = render_to_string('email_answer.html', template_data)
#             subject = 'Ответ на заявку'
#             sender = settings.EMAIL_HOST_USER
#             recipient = form.cleaned_data['email']
#             send_mail(subject, msg, sender, [recipient], html_message=msg)

#             messages.success(request, "Спасибо за вашу заявку. Ожидайте.") 
#             form = FormContact()
#     else:
#         form = FormContact()
#     return render(request, template_name='base.html', context={'form': form})

def main(request):
	out = _('news')
	print(out)
	print(get_language())
	# print(request.)
	# print(request.session['django_language'])
	return render(request, 'home_page.html')

def show_services(request):
	services = Services.objects.all()
	return render(request, 'services_list.html', context={'services':services})

# class ProjectsList(ListView):
# 	model = Projects
# 	template_name = 'projects_page.html'
# 	context_object_name = 'projects'

def ProjectsList(request):
	projects = Projects.objects.all()
	return render(request, 'projects_page.html', context={'projects':projects})

# class ProjectDetailView(DetailView):
# 	model = Projects
# 	template_name = 'projects_detail_page.html'
# 	context_object_name = 'projects'

def ProjectDetailView(request, pk):
	project = get_object_or_404(Projects, pk=pk)
	context = {'projects':project}
	return render(request, 'projects_detail_page.html', context)

# class NewsList(ListView):
# 	model  = News
# 	template_name = 'news_page.html'
# 	context_object_name = 'news'

def NewsList(request):
	news = News.objects.all()
	return render(request, 'news_page.html', context={'news':news})

# class NewsDetailview(DetailView):
# 	model  = News
# 	template_name = 'news_detail_page.html'
# 	context_object_name = 'news'

def NewsDetailview(request, pk):
	news = get_object_or_404(News, pk=pk)
	context = {'news':news}
	return render(request, 'news_detail_page.html', context)


def show_about_company(request):
	info = AboutCompany.objects.all()
	return render(request, 'about_company_page.html', context={'info':info})
	
# проверка статуса заявки и отправка сообщения

class TechsupportAnswerView(LoginRequiredMixin, View):
	template_name = 'email_message/message_request.html'
	form_class = RequestReviewForm

	def get(self, request):
		form = self.form_class()
		print(form)
		contacts = Contact.objects.all()
		return render(request, self.template_name, {'form_answer': form, 'contacts': contacts})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			answer = form.cleaned_data['answer']
			contact_id = form.cleaned_data['contact'].id
			contact = Contact.objects.get(id=contact_id)

			send_mail(
				'Ответ на ваш запрос',
				answer,
				'noreply@example.com',
				[contact.email],
				fail_silently=False,
			)
			
			contact.status = 'reviewed'
			contact.save()

			contacts = Contact.objects.all()

			return render(request, self.template_name, {'form_answer': form, 'contacts': contacts})

		return render(request, self.template_name, {'form_answer': form})
	

