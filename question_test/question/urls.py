# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('', views.user_question_counts, name='user_question_counts'),
    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),
]
