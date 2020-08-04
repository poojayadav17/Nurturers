from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# pooja's code
def homepage(request):
	eve = UpcomingEvents.objects.all().order_by('-id')[:3]
	return render(request,'index.html',{'eve':eve})

def register(request):
	allgender = GenderMaster.objects.all()
	allinterest = Interest.objects.all()

	if request.method =='POST':
		form = request.POST

		first_name = form['first_name']
		last_name = form['last_name']
		email = form['email']
		contact = form['contact']
		address = form['address']
		gender = form['gender']
		age = form['age']
		interest = form['interest']
		password = form['password']

		gendermasterobject = GenderMaster.objects.get(id = gender)
		interestobject = Interest.objects.get(id = interest)
		try:
			userObject = User.objects.get(username = email)
			message = 'Email is already registered!!!'

			return render(request,'register.html',{'message':message})
		except:

			users = User.objects.create_user(
				first_name = first_name,
				last_name = last_name,
				username = email,
				email = email,
				password = password
				)


			myuser = MyUser.objects.create(
				user = users,
				mobileNumber = contact,
				address = address,
				gender = gendermasterobject,
				interest = interestobject,
				age = age
				)

			message = "You have been successfully registered....Congratulations."
			return render(request,'register.html',{'allgender':allgender,'allinterest':allinterest,'message':message},)
	else:
		return render(request,'register.html',{'allgender':allgender,'allinterest':allinterest})

def Userlogin(request):

	if request.method == 'POST':
		form = request.POST
		
		username = form['username']
		password = form['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('/home')
		else:
			return HttpResponse('You are not a registered user....')

	else:
		return render(request,'login.html')

def logout_view(request):
	logout(request)

	return redirect('/login')

def contact(request):

	if request.method =='POST':
		form = request.POST

		name = form['name']
		email = form['email']
		message = form['message']

		contactnew = Contact.objects.create(
        	name = name,
        	email = email,
        	message = message,
        	)

		msg = "Your message has been successfully delivered."
		
		return render(request,'contact.html',{'msg':msg})
	else:
		return render(request,'contact.html')
@login_required(login_url='/login/')
def profile(request):
	user = request.user
	myuser = MyUser.objects.get(user = user)
	allgender = GenderMaster.objects.all()
	allinterest = Interest.objects.all()


	if request.method == 'POST':
		form = request.POST

		first_name = form['first_name']
		last_name = form['last_name']
		# email = form['email']
		contact = form['contact']
		address = form['address']
		gender = form['gender']
		age = form['age']
		interest = form['interest']

		gendermasterobject = GenderMaster.objects.get(id = gender)
		interestobject = Interest.objects.get(id = interest)

		#edit it
		user.first_name = first_name
		user.last_name = last_name
		# user.email = email
		# user.username = email

		user.save()

		myuser.mobileNumber = contact
		myuser.gender = gendermasterobject
		myuser.interest = interestobject
		myuser.age = age

		myuser.save()

		mg = "Your Profile is successfully edited...."
		
		return render(request,'profile.html',{'myuser': myuser,'allgender':allgender,'allinterest':allinterest,'mg':mg})

	else:
		return render(request,'profile.html',{'myuser': myuser})

@login_required(login_url='/login/')
def Events(request):
	user = request.user
	myuser = MyUser.objects.get(user = user)
	eve = UpcomingEvents.objects.all() 

	if request.method == 'POST':
		form = request.POST

		eventTitle = form['eventTitle']
		eventDescription = form['eventDescription']
		
		event = UpcomingEvents.objects.create(
			eventTitle = eventTitle,
			eventDescription = eventDescription,
			)

		msg = "Your event has been successfully added....Thank You."
		return render(request,'events.html',{'eve':eve,'msg':msg})
	else:
		return render(request,'events.html',{'eve' :eve})

# pooja's code ends here

# akanksha code starts
def ngodetail(request):
	ngoAre = Ngo.objects.all()
	return render(request,'allngo.html',{'ngoAre':ngoAre})
def fields(request):
	ngoAre1 = Ngo.objects.all().order_by('id')[:3]
	fields = Interest.objects.all()
	return render(request,'ngo_fields.html',{'ngoAre1' :ngoAre1,'fields' :fields})

def NgoFieldDetails(request,id):
	interestIs = Interest.objects.get(id = id)

	ngoIds = NgoInterest.objects.filter(interest = interestIs)


	return render(request,'allngo1.html',{'ngoAre':ngoIds})

def allQuestions(request):
	question = Questions.objects.all().order_by('-id')	
	return render(request,'discussion.html',{'question':question})	


def addQuestion(request):
	user = request.user
	myuser = MyUser.objects.get(user = user)
	
	question =Questions.objects.all().order_by('-id')	

	if request.method=='POST':
		form=request.POST

		questionis = form['questionis']

		questionis=Questions.objects.create(
			questionIs=questionis,
			askedBy = myuser,
			)
		return redirect('/allQuestions/')	
	else:
		return redirect('/allQuestions/')	

def answers(request,ids):

	myquestionIs = Questions.objects.get(id = ids)
	myquestionIs.total_view += 1
	myquestionIs.save()


	answersAre = Answer.objects.filter(questionId = myquestionIs)
	noOfanswer = answersAre.count()


	return render(request,'answers.html',{'myquestionIs':myquestionIs,'answersAre':answersAre,'noOfanswer':noOfanswer})		

def reply(request):
	user = request.user
	myuser = MyUser.objects.get(user = user)

	if request.method=='POST':
		form=request.POST

		qid = form['qid']
		questionis = Questions.objects.get(id = qid)

		answeris = form['answeris']

		answeris=Answer.objects.create(
			questionId = questionis,
			answerIs=answeris,
			answeredBy=myuser,
			)

		questionis.total_answer += 1
		questionis.save()

		url = '/question/answers/'+str(questionis.id)+'/'
		return redirect(url)
	else:
	    return HttpResponse('not done')
