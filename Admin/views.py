from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from User.views import *
from datetime import date

# Create your views here.
def district(request):
    disdata=tbl_district.objects.all()
    if request.method=='POST':
        districtname=request.POST.get('txt_district')
        tbl_district.objects.create(district_name=districtname)
        return render(request, 'Admin/District.html',{'dis':disdata})
    else:
        return render(request, 'Admin/District.html',{'dis':disdata})

def deletedis(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:District')

def editdis(request,eid):
    edata=tbl_district.objects.get(id=eid)
    if request.method=='POST':
        edata.district_name=request.POST.get('txt_district')
        edata.save()
        return redirect('Admin:District')
    else:
        return render(request,'Admin/District.html',{'data':edata})


def category(request):
    catdata=tbl_category.objects.all()
    if request.method=='POST':
        categoryname=request.POST.get('txt_category')
        tbl_category.objects.create(category_name=categoryname)
        return render(request, 'Admin/Category.html',{'cat':catdata})
    
    return render(request, 'Admin/Category.html',{'cat':catdata})

def deletecat(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect('Admin:Category')

def editcat(request,eid):
    edata=tbl_category.objects.get(id=eid)
    if request.method=='POST':
        edata.category_name=request.POST.get('txt_category')
        edata.save()
        return redirect('Admin:Category')
    else:
        return render(request,'Admin/Category.html',{'data':edata})
        
def place(request):
    disdata=tbl_district.objects.all()#dropdown
    placedata=tbl_place.objects.all()#select
    if request.method=='POST':
        placename=request.POST.get('txt_place')
        districtid=tbl_district.objects.get(id=request.POST.get('district'))
        #insert
        tbl_place.objects.create(place_name=placename,district=districtid)
        return render(request, 'Admin/Place.html',{'dis':disdata,'plc':placedata})
    return render(request, 'Admin/Place.html',{'dis':disdata,'plc':placedata})

def editplace(request,eid):
    edata=tbl_place.objects.get(id=eid)
    disdata=tbl_district.objects.all()
    if request.method=='POST':
        edata.place_name=request.POST.get('txt_place')
        edata.district=tbl_district.objects.get(id=request.POST.get('district'))
        edata.save()
        return redirect('Admin:Place')
    else:
        return render(request,'Admin/Place.html',{'data':edata,'dis':disdata})

def deleteplace(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return redirect('Admin:Place')


def subcategory(request):
    catdata=tbl_category.objects.all()#dropdown
    subcatdata=tbl_subcategory.objects.all()
    if request.method=='POST':
        subcategoryname=request.POST.get('txt_subcategory')
        categoryid=tbl_category.objects.get(id=request.POST.get('category'))
        #insert
        tbl_subcategory.objects.create(subcategory_name=subcategoryname,category=categoryid)
        return render(request,'Admin/Subcategory.html',{'cat':catdata, 'subcat':subcatdata})
    return render(request,'Admin/Subcategory.html',{'cat':catdata, 'subcat':subcatdata})

def deletesubcat(request,scid):
    tbl_subcategory.objects.get(id=scid).delete()
    return redirect('Admin:Subcategory')   

def editsubcat(request,eid):
    edata=tbl_subcategory.objects.get(id=eid)
    catdata=tbl_category.objects.all()
    if request.method=='POST':
        edata.subcategory_name=request.POST.get('txt_subcategory')
        edata.category=tbl_category.objects.get(id=request.POST.get('category'))
        edata.save()
        return redirect('Admin:Subcategory')
    else:
        return render(request,'Admin/Subcategory.html',{'data':edata,'cat':catdata}) 
    
    
def admin(request):
    admindata=tbl_admin.objects.all() #select
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
        return render(request, 'Admin/AdminRegistration.html',{'adata':admindata})
    return render(request, 'Admin/AdminRegistration.html',{'adata':admindata})

def deleteadmin(request,aid):
    tbl_admin.objects.get(id=aid).delete()
    return redirect('Admin:AdminRegistration')

def userdata(request):
    userdata=tbl_user.objects.all()
    return render(request, 'Admin/ViewUsers.html',{'udata':userdata})


def homepage(request):
    return render(request, 'Admin/Homepage.html')

def complaint(request):
    complaintdata=tbl_complaint.objects.all()
    return render(request, 'Admin/Viewcomplaint.html',{'cdata': complaintdata})

def deletecomp(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect('Admin:viewcomplaint')

def replycomp(request, id):
    compdata=tbl_complaint.objects.get(id=id)
    if request.method=='POST':
        compdainte=request.POST.get('txtreply')
        compdata.comp_reply=compdainte
        compdata.comp_status=1
        compdata.comp_reply_date=date.today()
        compdata.save()
        return redirect('Admin:viewcomplaint')
    else:
        return render(request, 'Admin/Reply.html',{'cdata':compdata})