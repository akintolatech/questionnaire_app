from django.urls import path
from .views import questionnaire_view, app_landing, success

urlpatterns = [
    path('', app_landing, name='landing'),
    path('questionnaire', questionnaire_view, name='questionnaire'),
    path('success/', success, name='success'),
]