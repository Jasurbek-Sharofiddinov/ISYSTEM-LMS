from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.

def index(request):
	template = loader.get_template('courses/index.html')

	context = {
		'courses': [
			{
				'id': 1,
				'name': 'Course 1'
			},
			{
				'id': 2,
				'name': 'Course 2'
			},
			{
				'id': 3,
				'name': 'Course 3'
			}

		]
	}
	return HttpResponse(template.render(context, request))

def detail(request,course_id):
	template = loader.get_template('courses/detail.html')
	context={
		'course_id':course_id
}
	return HttpResponse(template.render(context, request))
