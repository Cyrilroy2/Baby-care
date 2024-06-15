from django.db import models

class parent_reg(models.Model):
    name=models.CharField(max_length=150)
    mname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)

class babysitter(models.Model):
    name=models.CharField(max_length=150)
    mname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    age=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)

class doctor(models.Model):
    name=models.CharField(max_length=150)
    mname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    designation=models.CharField(max_length=150)

class services(models.Model):
    name=models.CharField(max_length=150)
    typee=models.CharField(max_length=150)
    description=models.CharField(max_length=200)

class baby_enroll(models.Model):
    name=models.CharField(max_length=150)
    age=models.CharField(max_length=150)
    description=models.CharField(max_length=150)
    pid=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

class nutritionists(models.Model):
    name=models.CharField(max_length=150)
    mname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    email=models.EmailField(max_length=150,default='babycare@gmail.com')
    gender=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)

class feedbacks(models.Model):
    pid=models.CharField(max_length=150)
    feedback=models.CharField(max_length=150)

class sitter_request(models.Model):
    name=models.CharField(max_length=150)
    bs_id=models.CharField(max_length=150)
    age=models.IntegerField()
    gender=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    date_frm=models.CharField(max_length=150)
    date_to=models.CharField(max_length=150)
    message=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    p_id=models.CharField(max_length=150)

class doctor_request(models.Model):
    name=models.CharField(max_length=150)
    d_id=models.CharField(max_length=150)
    p_id=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    age=models.IntegerField()
    gender=models.CharField(max_length=150)
    message=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    basicpay=models.CharField(max_length=150)

class nutrition_request(models.Model):
    name=models.CharField(max_length=150)
    n_id=models.CharField(max_length=150)
    p_id=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    age=models.IntegerField()
    gender=models.CharField(max_length=150)
    message=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    basicpay=models.CharField(max_length=150)

class attendance(models.Model):
    b_id=models.CharField(max_length=150)
    p_id=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

class payments(models.Model):
    s_id=models.CharField(max_length=150)
    basicpay=models.CharField(max_length=150)
    name=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    cvv=models.IntegerField()

class vacinations(models.Model):
    bname=models.CharField(max_length=150)
    vaccine=models.CharField(max_length=150)
    description=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    p_id=models.CharField(max_length=150)

class baby_info(models.Model):
    bname=models.CharField(max_length=150)
    description=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
  