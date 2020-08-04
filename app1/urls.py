from django.urls import path,re_path

from app1 import views

urlpatterns =  [
	path('home/',views.homepage),
	path('register/',views.register),
	path('ngodetail/',views.ngodetail),
	path('fields/',views.fields),
	path('login/',views.Userlogin),
	path('logout/',views.logout_view),
	path('contact/',views.contact),
	path('profile/',views.profile),
	path('events/',views.Events),

	path('allQuestions/',views.allQuestions),
	path('addQuestion/',views.addQuestion),
	path('answers/',views.answers),
	re_path('question/answers/(?P<ids>[\\w-]+)/$',views.answers,name='answers1'),
	path('reply/',views.reply),
	re_path('ngofields/details/(?P<id>[\\w-]+)/$',views.NgoFieldDetails,name='ngofields'),

]