from django.urls import path
from . import views

app_name = 'contact_form_plugin'
urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact'),
]
