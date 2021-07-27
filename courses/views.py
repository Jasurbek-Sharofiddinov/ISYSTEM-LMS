from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


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

	return render('templates/courses/index.html')
