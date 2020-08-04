from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class GenderMaster(models.Model):
	name = models.CharField(max_length = 20, null = True, blank = True)

	def __str__(self):
		return '%s %s' %(self.id,self.name)

class Interest(models.Model):
	name = models.CharField(max_length = 50,null = True, blank = True)
	imageurl = models.URLField(null = True, blank = True)

	def __str__(self):
		return '%s %s' %(self.id,self.name)	

class MyUser(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE, null = True, blank = True)
	mobileNumber = models.CharField(max_length = 12, null = True, blank = True)
	address = models.TextField(null = True, blank = True)
	gender = models.ForeignKey(GenderMaster, on_delete = models.CASCADE, null = True, blank = True)
	interest = models.ForeignKey(Interest, on_delete = models.CASCADE, null = True, blank = True)
	age = models.IntegerField(null = True, blank = True)
	def __str__(self):
		return '%s %s' %(self.user.username,self.age)

class Ngo(models.Model):
	name = models.CharField(max_length = 250, null = True, blank = True)
	regId = models.CharField(max_length = 100, null = True,blank = True)
	founder = models.CharField(max_length = 250, null = True, blank = True)
	ngoUrl = models.URLField(null = True, blank = True)
	email = models.CharField(max_length = 100, null = True, blank = True)
	contact = models.CharField(max_length = 12, null = True, blank = True)
	about = models.TextField( null = True, blank = True)
	imageurl = models.URLField(null = True, blank = True)

	def __str__(self):
		return '%s' %(self.name)

class NgoInterest(models.Model):
	NgoId = models.ForeignKey(Ngo,on_delete = models.CASCADE, null = True, blank = True)
	interest = models.ForeignKey(Interest, on_delete = models.CASCADE, null = True, blank = True)
	def __str__(self):
		return '%s %s' %(self.NgoId.name,self.interest.name)


class Notification(models.Model):
	notification = models.CharField(max_length = 500, null = True, blank = True)
	notification_date_time = models.DateTimeField(auto_now_add = True)
	category = models.CharField(max_length = 100, null = True, blank = True)
	createdBy = models.ForeignKey(MyUser, on_delete = models.CASCADE, null = True, blank = True)

	def __str__(self):
		return '%s' %(self.id)

class Contact(models.Model):
	name = models.CharField(max_length = 250, null = True, blank = True)
	email = models.CharField(max_length = 250, null = True, blank = True)
	message = models.TextField(null = True, blank = True)
	def __str__(self):
		return '%s' %(self.id)


class Questions(models.Model):
	questionIs = models.TextField(null = True, blank = True)
	askedBy = models.ForeignKey(MyUser, on_delete = models.CASCADE, null = True, blank = True)
	askedDateTime = models.DateTimeField(auto_now_add = True)
	total_view = models.IntegerField(default = 0)
	total_answer = models.IntegerField(default = 0)
	def __str__(self):
		return '%s' %(self.id)


class Answer(models.Model):
	questionId = models.ForeignKey(Questions,on_delete = models.CASCADE, null = True, blank = True)
	answerIs = models.TextField(null = True, blank = True)
	answeredBy = models.ForeignKey(MyUser, on_delete = models.CASCADE, null = True, blank = True)
	answereddDateTime = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s' %(self.id)

class UpcomingEvents(models.Model):
	eventTitle = models.CharField(max_length = 200, null = True, blank = True)
	eventDescription = models.TextField(null = True, blank = True)
	createdDateTime = models.DateTimeField(auto_now_add = True)
	addedBy = models.ForeignKey(MyUser, on_delete = models.CASCADE, null = True, blank = True)

	def __str__(self):
		return '%s' %(self.id)