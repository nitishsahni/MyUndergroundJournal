from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logoutView, name='logout'),
    path('entries', views.entries, name='entries'),
    path('post', views.post, name='post')
]