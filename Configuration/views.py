from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from cv.models import Home,Category, Skills, Portfolio,Experience


from django.http import HttpResponse,HttpResponseRedirect
from cv.forms import ExperienceForm,CertificateForm,SkillsForm
def index(request):

    home=Home.objects.all()
    categories=Category.objects.all()
    experience=Experience.objects.all()
    skills=Skills.objects.all()
    portfolio=Portfolio.objects.all()
  
    context={
        'home':home,
        'categories':categories,
        'experience':experience,
        'portfolio':portfolio,
        'skills':skills
    }
    return render(request,'authenticate/configurations.html',context)

	 


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('config')
		else:
			messages.error(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	


	else:
		return render(request, 'authenticate/login.html', {})

	
def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('login')

#!delete Certificate
def delete_certif(request, event_id):
	event = Portfolio.objects.get(pk=event_id)
	event.delete()
	return redirect('config')	

#!delete Skill
def delete_Skill(request, event_id):
	event = Skills.objects.get(pk=event_id)
	event.delete()
	return redirect('config')		

#!delete Experience
def delete_Exp(request, event_id):
	event = Experience.objects.get(pk=event_id)
	event.delete()
	messages.success(request, ("Experience Deleted!!"))
	return redirect('config')	


#?Add Skill
def add_Skill(request):
	submitted=False
	if request.method =="POST":
		form=SkillsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('config')
	else:
		form=SkillsForm
		if 'submitted' in request.GET:
			submitted=True
	return render(request, 'authenticate/AddSkill.html',
				 {'form':form,
				 'submitted':submitted})


#?Add Certificate
def add_certif(request):
	submitted=False
	if request.method =="POST":
		form=CertificateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('config')
	else:
		form=CertificateForm
		if 'submitted' in request.GET:
			submitted=True
	return render(request, 'authenticate/AddCertif.html',
				 {'form':form,
				 'submitted':submitted})


#?Add Experience
def add_exp(request):
	submitted=False
	if request.method =="POST":
		form=ExperienceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('config')
	else:
		form=ExperienceForm
		if 'submitted' in request.GET:
			submitted=True
	return render(request, 'authenticate/AddExp.html',
				 {'form':form,
				 'submitted':submitted})







#*Update Certificate
def update_Certif(request,event_id):
	certif = Portfolio.objects.get(pk=event_id)
	form = CertificateForm(request.POST or None, instance=certif)
	if form.is_valid():
		form.save()
		return redirect('config')
	return render(request, 'authenticate/updateCertif.html', 
		{'certif': certif,
		'form':form})

#* Update Skill
def update_Skill(request,event_id):
	skill = Skills.objects.get(pk=event_id)
	form = SkillsForm(request.POST or None, instance=skill)
	if form.is_valid():
		form.save()
		return redirect('config')
	return render(request, 'authenticate/updateSkill.html', 
		{'skill': skill,
		'form':form})
	
#*Update Experience
def update_Exp(request,event_id):
	exp = Experience.objects.get(pk=event_id)
	form=ExperienceForm(request.POST or None,instance=exp)
	if form.is_valid():
		form.save()
		return redirect('config')
	return render(request, 'authenticate/updateExp.html', 
		{'exp': exp,
		'form':form})