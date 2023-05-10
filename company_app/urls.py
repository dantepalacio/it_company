from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='base'),
    path('services/', views.show_services, name='services_page'),
    path('projects/', views.ProjectsList, name='projects_page'),
    path('project/<int:pk>/', views.ProjectDetailView, name='project_detail_page'),
    path('news/', views.NewsList, name='news_page'),
    path('news/<int:pk>/', views.NewsDetailview, name='news_detail_page'),
    path('about_company/', views.show_about_company, name='about_company_page'),


    path('answer/', views.TechsupportAnswerView.as_view(), name='answer_message')
]