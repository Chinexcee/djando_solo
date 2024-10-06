from django.urls import path
from .views import homepage, about_us, blog, dashboard, individual, register, login


urlpatterns = [
    path('', homepage, name='frontview'),
    path('about', about_us, name='aboutus'),
    path('blog', blog, name='blogpost'),
    path('dashboard', dashboard, name='dashboard'),
    path('individual', individual, name='individually'),
    path('register', register, name='signup'),
    path('login', login, name='signin')
]
