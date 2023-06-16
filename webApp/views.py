from django.shortcuts import render,redirect
from credapp.models import categoryDB,poductDB
from webApp.models import usersignupDB,contactDB,cartDB,checkoutBD
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def homepage(req):
    data = categoryDB.objects.all()
    return render(req,"home.html",{'data':data})

def contactpage(req):
    return render(req,"contact.html")

def productpage(req,cateName):
    data = categoryDB.objects.all()
    productdata = poductDB.objects.filter(product_category=cateName)
    return render(req,"Products.html",{'data':data,'productdata':productdata})

def singleProductpage(req,dataid):
    pro = poductDB.objects.get(id=dataid)
    data = categoryDB.objects.all()
    return render(req,"singleProduct.html",{'data':data,'pro':pro})

def loginpage(req):
    return render(req,"login.html")


def userRegData(req):
    if req.method == "POST":
        uname=req.POST.get('uName')
        uemail=req.POST.get('uEmail')
        umobile=req.POST.get('uMobile')
        upassword=req.POST.get('uPassword')
        uimg=req.FILES['uImage']
        obj = usersignupDB(userName=uname,userEmail=uemail,userMobile=umobile,userPassword=upassword,userImage=uimg)
        obj.save()
        messages.success(req,"Registration Successfuly....")
        return redirect(loginpage)

def userLogin(req):
    if req.method=="POST":
        uname = req.POST.get('Username')
        pwd = req.POST.get('Password')
        if usersignupDB.objects.filter(userName=uname,userPassword=pwd).exists():
            req.session['userName']=uname
            req.session['userPassword']=pwd
            messages.success(req,"Login Successfuly....")
            return redirect(homepage)
        else:
            messages.error(req,"Invalid User Name or Password")
            return redirect (loginpage)
    else:
         messages.error(req,"Invalid User Name or Password")
         return redirect (loginpage)
    
def userLogout(req):
        del req.session['userName']
        del req.session['userPassword']
        return redirect(loginpage)


def contactData(req):
    if req.method=="POST":
        name=req.POST.get('cname')
        email=req.POST.get('cemail')
        subject=req.POST.get('csubject')
        message=req.POST.get('cmessage')
        obj = contactDB(contactName=name,contactEmail=email,contactSubject=subject,contactMessage=message)
        obj.save()
        return redirect(contactpage)
    
def cartpage(req):
    data=cartDB.objects.filter(cartUserName=req.session['userName'])
    return render(req,"cart.html",{'data':data})

def cartData(req):
    if req.method=="POST":
        uname=req.POST.get('c_uname')
        pname=req.POST.get('c_pname')
        pdes=req.POST.get('c_pdes')
        pqty=req.POST.get('c_qty')
        pprice=req.POST.get('c_tprice')
        # pimg=req.FILES['c_img']
        obj = cartDB(cartUserName=uname,cartName=pname,cartDescription=pdes,cartQuandity=pqty,cartPrice=pprice)
        obj.save()
        messages.success(req,"Add Cart Successfuly....")
        return redirect(cartpage)
    
def deletecartData(req,dataid):
    data = cartDB.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"Product Deleted Successfuly....")
    return redirect(cartpage)

def checkoutPage(req):
    return render(req,"checkout.html")

def checkoutData(req):
    if req.method == "POST":
        Name=req.POST.get('checkout_Name')
        Email=req.POST.get('checkout_Email')
        Number=req.POST.get('checkout_Number')
        Address=req.POST.get('checkout_Address')
        Country=req.POST.get('checkout_Country')
        State=req.POST.get('checkout_State')
        obj = checkoutBD(checkoutName=Name,checkoutEmail=Email,checkoutNumber=Number,checkoutAddress=Address,checkoutCountry=Country,checkoutState=State)
        obj.save()
        messages.success(req,"Checkout Successfuly....")
        return redirect(homepage)
    

    







