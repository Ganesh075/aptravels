from django.shortcuts import render,redirect
from django.http import HttpResponse
from Myways.forms import Usregis,Upd,Pad,Busdata,usdate
from aptravels import settings 
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from Myways.models import Exfd,Data


# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/cabs.html')

def contact(request):
	return render(request,'html/contact.html')

def lm(request):
	return render(request,'html/learnmore.html')
def bt(request):
	return render(request,'html/bookticket.html')

# def register(request):
# 	if request.method=='POST':
# 		t=Usregis(request.POST)
# 		if t.is_valid():
# 			user=t.save()
# 			adml = user.email
#  			#pas = user.password
# 			msg = "Hi {}  register successfully your email is {} and password is {}".format(user.username,user.email,user.password)
# 			sub = "Test mail"
# 			sd = settings.EMAIL_HOST_USER
# 			to = send_mail(sub,msg,sd,[adml])
# 			if to == 1:
# 				messages.success(request,"mail sent successfully")
# 				return render(request,'html/login.html')
# 	t=Usregis()
# 	return render(request,'html/register.html',{'y':t})



# def register(request):
# 	if request.method == "POST":
# 		i = Usregis(request.POST)
# 		if i.is_valid():
# 			user=t.save()
# 			messages.success(request,"User registered Successfully")
# 			#return redirect('/login')
# 			adml = user.email
# 			pas = user.password
# 			msg = "Hi {}  register successfully your email is {} and password is {}".format(user.username,user.email,user.password)
# 			sub = "Test mail"
# 			sd = settings.EMAIL_HOST_USER
# 			to = send_mail(sub,msg,sd,[adml])
# 			if to == 1:
# 				return messages.primary("A mail sent to your account")
# 				return redirect('/lg')
# 				return messages.primary("A mail sent to your account")
# 		messages.warning(request,'mail not sent')
# 	messages.error(request,'Registration Failed')
# 	i = Usregis()
# 	return render(request,'html/register.html',{'y':i})




def register(request):
	if request.method == "POST":
		y = Usregis(request.POST)
		if y.is_valid():
			p = y.save(commit=False)
			rc = p.email
			# print(rc)
			sb = "Testing Email to register for Worklog Project"
			mg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				p.save()
				messages.success(request,"Please check your {} for login creadentials".format(rc))
				return redirect('/lg')
			messages.danger(request,"please enter correct emailid or username or password")
			# print(p.username,p.email)
	y = Usregis()
	return render(request,'html/register.html',{'t':y})

@login_required
def dashboard(request):
	return render(request,'html/dashboard.html')

@login_required
def prfle(request):
	return render(request,'html/profile.html')

@login_required
def updf(request):
	if request.method == "POST":
		p=Upd(request.POST,instance=request.user)
		t=Pad(request.POST,request.FILES,instance=request.user.exfd) 
		if p.is_valid() and t.is_valid():
			p.save()
			t.save()
			messages.success(request,"{} your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p = Upd(instance=request.user)
	t = Pad(instance=request.user.exfd)
	return render(request,'html/updateprofile.html',{'r':p,'q':t})


@login_required
def addbus(request):
	if request.method == "POST":
		w = Busdata(request.POST,request.FILES)
		if w.is_valid():
			w.save()
			messages.success(request,"Bus are added successfully")
		else:
			messages.error(request,"Bus added failed")
	w =Busdata()
	return render(request,'html/addbus.html',{'d':w})


def disp(request):
	return render(request,'html/disp.html',{'dis':Data.objects.all()})

@login_required
def bus_search(request):
	return render(request,'html/bus_search.html')

@login_required
def contact(request):
	results = Data.objects.all()
	if request.method == "POST":
		c = usdate(request.POST,instance=request.user)
		print('before c is valid')
		if c.is_valid():
			print('after  c is valid')
			so = request.POST.get('source')
			de = request.POST.get('destination')
			busobj = Data.objects.raw('select * from data where source="'+so+'" and destination="'+de+'"')
			print(busobj)
			c.save()
			return render(request,'html/bus_search.html',{'Data':busobj})
	c = usdate(instance=request.user)
	return render(request,'html/contact.html',{'places':results,'d':c})