from django.urls import path,include
from Admin import views
app_name="Admin"

urlpatterns = [
    path('District/',views.district,name="District"),
    path('deletedis/<int:did>',views.deletedis, name="deletedis"),
    path('editdis/<int:eid>',views.editdis, name="editdis"),
    
    path('Category/',views.category,name="Category"),
    path('deletecat/<int:cid>',views.deletecat, name="deletecat"),
    path('editcat/<int:eid>',views.editcat, name="editcat"),
    
    path('Place/',views.place, name="Place"),
    path('deleteplace/<int:pid>',views.deleteplace, name="deleteplace"),
    path('editplace/<int:eid>',views.editplace, name="editplace"),
    
    path('Subcategory/',views.subcategory, name="Subcategory"),
    path('deletesubcat/<int:scid>',views.deletesubcat, name="deletesubcat"),
    path('editsubcat/<int:eid>',views.editsubcat, name="editsubcat"),
    
    path('AdminRegistration/',views.admin,name="AdminRegistration"),
    path('deleteadmin/<int:aid>',views.deleteadmin, name="deleteadmin"),
    
     path('Homepage/',views.homepage,name='homepage'),
     path('ViewUsers/',views.userdata,name='userdata'),
     
     path('ViewComplaint/',views.complaint,name='viewcomplaint'),
     path('deletecomplaint/<int:did>',views.deletecomp,name='deletecomplaint'),
     path('reply/<int:id>',views.replycomp,name='replycomplaint'),
]
