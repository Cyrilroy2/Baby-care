from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
import datetime
import razorpay


from urllib.parse import urlencode
from .models import *
from datetime import date,datetime,timedelta

today = date.today()

def first(request):
    sel=services.objects.all()
   
    return render(request,'index.html',{'result':sel})

def index(request):
    sel=services.objects.all()
    
    return render(request,'index.html',{'result':sel})




def parentreg(request):
    return render(request,'register.html')

def addparent(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        district=request.POST.get('district')
        email=request.POST.get('email')
        password=request.POST.get('password')

        cus=parent_reg(name=name,mname=mname,lname=lname,address=address,district=district,email=email,password=password)
        cus.save()
        return render(request,'index.html', {'message1':' successfully Registered'})
    
def login(request):
    return render(request,'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return render(request,'index.html')

    elif parent_reg.objects.filter(email=email,password=password).exists():
        userdetails=parent_reg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.name

            request.session['uemail'] = email

            request.session['cus'] = 'cus'


            return render(request,'index.html')



    else:
        return render(request, 'login.html')
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

def babysitterr(request):
    return render(request,'babysitter.html')

def addsitter(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')


    if babysitter.objects.filter(phone= phone).exists():

        return render(request,'index.html', {'message1':' Already Exist'})
    else:

         cus=babysitter(name=name,mname=mname,lname=lname,address=address,age=age,gender=gender,phone=phone)
         cus.save()
       
         return render(request,'index.html', {'message1':' successfully Registered'})

        
    
    
def dctr(request):
    return render(request,'doctor.html')

def adddctr(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        designation=request.POST.get('designation')

    if doctor.objects.filter(email=email).exists():

        return render(request,'index.html', {'message1':' Already Exist'})
    else:

        cus=doctor(name=name,mname=mname,lname=lname,address=address,email=email,gender=gender,phone=phone,designation=designation)
        cus.save()
       
        return render(request,'index.html', {'message1':' successfully Registered'})
    
    
def service(request):
    return render(request,'service.html')

def addservice(request):
    if request.method=="POST":
        name=request.POST.get('name')
        typee=request.POST.get('typee')
        description=request.POST.get('description')
      

        cus=services(name=name,typee=typee,description=description)
        cus.save()
    return render(request,'index.html', {'message1':' successfully Registered'})
    
def babyenv(request):
    return render(request,'enrollment.html')

def addbaby(request):
    if request.method=="POST":
        pid=request.session['uid']
        date=today
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        description =request.POST.get('description')
        status =request.POST.get('status')
    # if not int(age)<=6:
    #     return redirect(babyenv,{'message1':'Age should be less than 6'})

        cus=baby_enroll(pid=pid,date=date,name=name,age=age,gender=gender,description=description,status=status)
        cus.save()
    return render(request,'index.html', {'message1':' successfully Registered'})
    

def viewbabies(request):
    sel=baby_enroll.objects.all()
    user= parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.pid)==str(j.id):
                i.pid=j.name
    return render(request,'viewenv.html',{'result':sel})  
    
def babyaccept(request,id):
    sel=baby_enroll.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return redirect(viewbabies)

def babyreject(request,id):
    sel=baby_enroll.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return redirect(viewbabies)

def viewdoctors(request):
    sel=doctor.objects.all()
    return render(request,'viewdoctors.html',{'result':sel})
 
def deletedoctor(request,id):
	emp=doctor.objects.get(pk=id)
	emp.delete()
	return redirect(viewdoctors)

def viewservices(request):
    sel=services.objects.all()
    return render(request,'viewservices_admin.html',{'result':sel})

def deleteservice(request,id):
	emp=services.objects.get(pk=id)
	emp.delete()
	return redirect(viewservices)

def viewbabysitters(request):
    sel=babysitter.objects.all()
    return render(request,'viewbabysitters.html',{'result':sel})

def deletesitter(request,id):
	emp=babysitter.objects.get(pk=id)
	emp.delete()
	return redirect(viewbabysitters)


def nutritionist(request):
    return render(request,'nutritionist.html')

def addnutritionist(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')

    if nutritionists.objects.filter(email= email).exists():

        return render(request,'index.html', {'message1':' Already Exist'})
    else:

         cus=nutritionists(name=name,mname=mname,lname=lname,address=address,email=email,gender=gender,phone=phone)
         cus.save()
       
         return render(request,'index.html', {'message1':' successfully Registered'})

    
       
        
    
def viewnutritionist(request):
    sel=nutritionists.objects.all()
    return render(request,'viewnutritionist.html',{'result':sel})

def deletenutritionist(request,id):
	emp=nutritionists.objects.get(pk=id)
	emp.delete()
	return redirect(viewnutritionist)

def viewsrc(request):
    sel=services.objects.all()
    return render(request,'viewsrvies.html',{'result':sel})

def view_doctors(request):
    sel=doctor.objects.all()
    return render(request,'view_doctors.html',{'result':sel})

def view_babysitters(request):
    sel=babysitter.objects.all()
    return render(request,'view_babysitters.html',{'result':sel})

def view_nutritionist(request):
    sel=nutritionists.objects.all()
    return render(request,'view_nutritionist.html',{'result':sel})

def feedback(request):
    return render(request,'feedback.html')

def addfeedback(request):
    if request.method=="POST":
        pid=request.session['uid']
        feedback=request.POST.get('feedback')
  
        cus=feedbacks(pid=pid,feedback=feedback)
        cus.save()
    return render(request,'index.html')
    
def v_feedback(request):
    sel=feedbacks.objects.all()
    user=parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.pid)==str(j.id):
                i.pid=j.name
    return render(request,'view_feedback.html',{'result':sel})

def reqsitter(request,id):
    sel=babysitter.objects.get(id=id)
    return render(request,'requestsitter.html',{'result':sel})

def addreqsitter(request):
    if request.method=="POST":
        p_id=request.session['uid']
        name=request.POST.get('name')
        bs_id=request.POST.get('bs_id')
        location=request.POST.get('location')
        date_frm=request.POST.get('date_frm')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        date_to=request.POST.get('date_to')
        message=request.POST.get('message')
        status=request.POST.get('status')
        

        cus=sitter_request(p_id=p_id,status=status,name=name,bs_id=bs_id,location=location,date_frm=date_frm,age=age,gender=gender,date_to=date_to,message=message)
        cus.save()
    return render(request,'index.html', {'message2':' successfully Requested'})
    
def v_reqsitter(request):
    sel=sitter_request.objects.all()
    user=parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.p_id)==str(j.id):
                i.p_id=j.name
    return render(request,'v_requestsitter.html',{'result':sel})

def reqaccept(request,id):
    sel=sitter_request.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return redirect(v_reqsitter)

def reqreject(request,id):
    sel=sitter_request.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return redirect(v_reqsitter)

def view_reqsitter(request):
    sel=sitter_request.objects.all()
    user=parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.p_id)==str(j.id):
                i.p_id=j.name
    return render(request,'view_requestsitter.html',{'result':sel})

def reqdoctor(request,id):
    sel=doctor.objects.get(id=id)
    return render(request,'requestdoctor.html',{'result':sel})

def addreqdoctor(request):
    if request.method=="POST":
        p_id=request.session['uid']
        d_id=request.POST.get('d_id')
        name=request.POST.get('name')
        location=request.POST.get('location')
        date=request.POST.get('date')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        message=request.POST.get('message')
        status=request.POST.get('status')
        basicpay=request.POST.get('basicpay')

        cus=doctor_request(p_id=p_id,d_id=d_id,status=status,name=name,location=location,date=date,age=age,gender=gender,message=message,basicpay=basicpay)
        cus.save()
    return render(request,'index.html', {'message2':' successfully Requested'})
    
def reqnutri(request,id):
    sel=nutritionists.objects.get(id=id)
    return render(request,'requestnutri.html',{'result':sel})

def addreqnutri(request):
    if request.method=="POST":
        p_id=request.session['uid']
        n_id=request.POST.get('n_id')
        name=request.POST.get('name')
        location=request.POST.get('location')
        date=request.POST.get('date')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        message=request.POST.get('message')
        status=request.POST.get('status')
        basicpay=request.POST.get('basicpay')

        cus=nutrition_request(p_id=p_id,n_id=n_id,status=status,name=name,location=location,date=date,age=age,gender=gender,message=message,basicpay=basicpay)
        cus.save()
    return render(request,'index.html', {'message2':' successfully Requested'})
    
def v_reqdoctor(request):
    sel=doctor_request.objects.all()
    user=doctor.objects.all()
    for i in sel:
        for j in user:
            if str(i.d_id)==str(j.id):
                i.d_id=j.name
    return render(request,'v_requestdoctor.html',{'result':sel})

def d_reqaccept(request,id):
    sel=doctor_request.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return redirect(v_reqdoctor)

def d_reqreject(request,id):
    sel=doctor_request.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return redirect(v_reqdoctor)

def v_reqnutritionist(request):
    sel=nutrition_request.objects.all()
    user=nutritionists.objects.all()
    for i in sel:
        for j in user:
            if str(i.n_id)==str(j.id):
                i.n_id=j.name
    return render(request,'v_requestnutritionist.html',{'result':sel})

def n_reqaccept(request,id):
    sel=nutrition_request.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return redirect(v_reqnutritionist)

def n_reqreject(request,id):
    sel=nutrition_request.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return redirect(v_reqnutritionist)

def mark_attendance(request):
    sel=baby_enroll.objects.filter(status='accepted')
    user=parent_reg.objects.all()
    for i in sel:
        for j in user:
            if str(i.pid)==str(j.id):
                i.pid=j.name
    return render(request,'mark_attendance.html',{'result':sel})

def mark(request,id):
    sel=baby_enroll.objects.get(id=id)
    return render(request,'attendance.html',{'result':sel})

def addattendance(request):
    if request.method=="POST":
        b_id=request.POST.get('b_id')
        p_id=request.POST.get('p_id')
        date=request.POST.get('date')
        status=request.POST.get('status')

        cus=attendance(b_id=b_id,status=status,p_id=p_id,date=date)
        cus.save()
    return render(request,'index.html', {'message2':' successfully Added'})
    
def view_requests(request):
    user=request.session['uid']
    sel=doctor_request.objects.filter(p_id=user)
    sel1=nutrition_request.objects.filter(p_id=user)
    return render(request,'view_requests.html',{'result':sel,'result1':sel1})

def payment(request):
    user=request.session['uid']
    sel=doctor_request.objects.filter(status='accepted',p_id=user)
    sel1=nutrition_request.objects.filter(status='accepted',p_id=user)
    return render(request,'payments.html',{'result':sel,'result1':sel1})





def dpay(request,id):
    sel=doctor_request.objects.get(id=id)
    
    return render(request,'pay.html',{'result':sel})


def nsuccess(request,id):
    sel=nutrition_request.objects.get(id=id)
    sel.status='Paid'
    sel.save()
    return redirect(payment)

def dsuccess(request,id):
    sel=doctor_request.objects.get(id=id)
    sel.status='Paid'
    sel.save()
    return redirect(payment)

  
def addpay(request):
   s_id=request.POST.get('s_id')
  


   
    


   if request.method=="POST":
        amount = 500*100
        order_currency = 'INR'
        client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        doctor_request.objects.filter(id=s_id).update(status='Paid')
        cus=payments(s_id=s_id)
        cus.save()
        return render(request, "pay.html",{'payment':payment}, {'message2':' successfully Paid'})
        # s_id=request.POST.get('s_id')
        # basicpay=request.POST.get('basicpay')
        # name=request.POST.get('name')
        # date=request.POST.get('date')
        # cvv=request.POST.get('cvv')



        # cus=payments(s_id=s_id,basicpay=basicpay,name=name,date=date,cvv=cvv)
        # doctor_request.objects.filter(id=s_id).update(status='Paid')
        # cus.save()
        # return render(request,'index.html', {'message2':' successfully Paid'})
    
def nupay(request,id):
    if request.method=="POST":
        s_id=request.POST.get('s_id')
        
        nutrition_request.objects.filter(id=s_id).update(status='Paid')
        return render(request,'index.html', {'message2':' successfully Paid'})
    else:
        sel=nutrition_request.objects.get(id=id)
        return render(request,'npay.html',{'result':sel})


def vac(request):
    return render(request,'vaccine.html')

def addvac(request):
    if request.method=="POST":
        p_id=request.session['uid']
        bname=request.POST.get('bname')
        vaccine=request.POST.get('vaccine')
        date=request.POST.get('date')
        description=request.POST.get('description')

        cus=vacinations(p_id=p_id,bname=bname,vaccine=vaccine,description=description,date=date)
        cus.save()
    return render(request,'index.html', {'message2':' successfully added'})
    
    
def viewvac(request):
    sel=vacinations.objects.all()
    return render(request,'view_vaccine.html',{'result':sel})

def babyinfo(request):
    sel=baby_enroll.objects.all()
    return render(request,'babyinfo.html',{'result':sel})


def addbabyinfo(request):
    if request.method=="POST":
      
        bname=request.POST.get('bname')
        date=request.POST.get('date')
        description=request.POST.get('description')

        cus=baby_info(bname=bname,description=description,date=date)
        cus.save()
    return render(request,'index.html', {'message2':' successfully added'})
    
def view_babyinfo(request):
    sel=baby_enroll.objects.filter(pid=request.session['uid'])
    return render(request,'view_babyinfo.html',{'result':sel})

def view_attendence(request):
    user1=request.session['uid']
    sel=attendance.objects.filter(p_id=user1)
    user=baby_enroll.objects.all()
    for i in sel:
        for j in user:
            if str(i.b_id)==str(j.id):
                i.b_id=j.name
    
    return render(request,'view_attendance.html', {'result':sel})




def attend(request):
    # user1=request.session['uid']
    sel=attendance.objects.all()
    # user=baby_enroll.objects.all()
    # for i in sel:
    #     for j in user:
    #         if str(i.b_id)==str(j.id):
    #             i.b_id=j.name
    return render(request,'attend.html',{'sel':sel})





def home1(request):
    return render(request, 'master/home1.html')

