from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *

def homepage(request):
    return render(request, 'Guest/homepage1.html')

def homepage2(request):
    return render(request,'Guest/homepage2.html')


def Signup(request):
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method == 'POST':
        uname=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("pass")
        contact=request.POST.get("contact")
        address=request.POST.get("address")
        img=request.FILES.get("file")
        place=tbl_place.objects.get(id=request.POST.get("selplace"))
        tbl_user.objects.create(user_name=uname,user_email=email,user_password=password,user_contact=contact,user_address=address,user_photo=img,place=place)
        return redirect('Guest:login')
    return render(request,'Guest/Signup.html',{'dis':district,'plc':place})
# Create your views here.

def ajaxplace(request):
    disid=tbl_district.objects.get(id=request.GET.get('did'))
    place=tbl_place.objects.filter(district=disid)
    return render(request,'Guest/Ajaxplace.html',{'place':place})




def login(request):
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("pass")
        
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        
        if usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect('User:homepage')
        elif admincount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('Admin:homepage')
        else:
            return render(request, 'Guest/UserLogin.html',{'msg':"Invalid Data"})
    return render(request, 'Guest/UserLogin.html')
    