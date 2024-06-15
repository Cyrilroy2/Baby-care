"""
URL configuration for Babycare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# , include
from care import views
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/',{include('admin.urls')} admin.site.urls)
    path('',views.first),
    path('index',views.index),
    path('parentreg',views.parentreg),
    path('addparent',views.addparent),
    path('login',views.login),
    path('addlogin',views.addlogin),
    path('logout',views.logout),
    path('babysitterr',views.babysitterr),
    path('addsitter',views.addsitter),
    path('dctr',views.dctr),
    path('adddctr',views.adddctr),
    path('service',views.service),
    path('addservice',views.addservice),
    path('babyenv',views.babyenv),
    path('addbaby',views.addbaby),  
    path('viewbabies',views.viewbabies), 
    path('babyaccept/<int:id>',views.babyaccept,name='babyaccept'),
    path('babyreject/<int:id>',views.babyreject,name='babyreject'), 
    path('viewdoctors',views.viewdoctors), 
    path('view_doctors',views.view_doctors), 
    path('deletedoctor/<int:id>',views.deletedoctor,name='deletedoctor'), 
    path('viewservices',views.viewservices), 
    path('deleteservice/<int:id>',views.deleteservice,name='deleteservice'),
    path('viewbabysitters',views.viewbabysitters), 
    path('view_babysitters',views.view_babysitters), 
    path('deletesitter/<int:id>',views.deletesitter,name='deletesitter'),
    path('nutritionist',views.nutritionist),
    path('addnutritionist',views.addnutritionist),
    path('viewnutritionist',views.viewnutritionist), 
    path('view_nutritionist',views.view_nutritionist), 
    path('deletenutritionist/<int:id>',views.deletenutritionist,name='deletenutritionist'),
    path('viewsrc',views.viewsrc), 
    path('feedback',views.feedback), 
    path('addfeedback',views.addfeedback), 
    path('v_feedback',views.v_feedback), 
    path('v_reqsitter',views.v_reqsitter), 
    path('reqsitter/addreqsitter',views.addreqsitter), 
    path('reqdoctor/addreqdoctor',views.addreqdoctor), 
    path('reqsitter/<int:id>',views.reqsitter,name='reqsitter'),
    path('reqaccept/<int:id>',views.reqaccept,name='reqaccept'),
    path('reqreject/<int:id>',views.reqreject,name='reqreject'), 
    path('view_reqsitter',views.view_reqsitter), 
    path('reqdoctor/<int:id>',views.reqdoctor,name='reqdoctor'),
    path('reqnutri/<int:id>',views.reqnutri,name='reqnutri'),
    path('reqnutri/addreqnutri',views.addreqnutri), 
    path('v_reqdoctor',views.v_reqdoctor), 
    path('d_reqaccept/<int:id>',views.d_reqaccept,name='d_reqaccept'),
    path('d_reqreject/<int:id>',views.d_reqreject,name='d_reqreject'), 
    path('v_reqnutritionist',views.v_reqnutritionist),
    path('n_reqaccept/<int:id>',views.n_reqaccept,name='n_reqaccept'),
    path('n_reqreject/<int:id>',views.n_reqreject,name='n_reqreject'), 
    path('mark_attendance',views.mark_attendance), 
    

    path('mark/<int:id>',views.mark,name='mark'),
    path('mark/addattendance',views.addattendance,name='attend'), 
    path('view_requests',views.view_requests), 
    path('payment',views.payment), 
    
    path('dpay/<int:id>',views.dpay,name='dpay'),

    path('nsuccess/<int:id>',views.nsuccess, name='nsuccess'),
    path('dsuccess/<int:id>',views.dsuccess, name='dsuccess'),

    path('dpay/addpay',views.addpay), 
    path('success',views.index), 
    path('vac',views.vac), 
    path('addvac',views.addvac), 
    path('viewvac',views.viewvac), 
    path('babyinfo',views.babyinfo), 
    path('addbabyinfo',views.addbabyinfo), 
    path('view_babyinfo',views.view_babyinfo), 
    path('view_attendence',views.view_attendence), 
    path('nupay/<int:id>',views.nupay,name='nupay'),
    path('home1', views.home1, name='home1'),

    path('attendence',views.attend,name='attend')
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)