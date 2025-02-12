from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns = [
    
    path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
    path('Login/',views.login,name='login'),
    path('Signup/',views.Signup,name='signup'),
    path('Index/',views.homepage, name='index'),
    path('Index-2/',views.homepage2, name='index2'),
]
