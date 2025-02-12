from django.urls import path,include
from django.contrib.auth.views import LogoutView
from User import views
from Guest import views as guest_views
app_name="User"


urlpatterns = [
    
    path('Homepage/',views.homepage,name='homepage'),
    path('Homepage2/',views.homepage2,name='homepage2'),
    path('Myprofile/',views.myprofile,name='myprofile'),
    path('Editprofile/',views.editprofile,name='editprofile'),
    path('Changepassword/',views.changepassword,name='changepassword'),
    path('Bmiindex/',views.bmiindex,name='bmiindex'),
    path('Complaint/',views.complaint,name='complaint'),
    path('logout/', views.logout, name='logout'),
    # path('deletecomp/<int:did>',views.deletecomp,name="deletecomp"),
]