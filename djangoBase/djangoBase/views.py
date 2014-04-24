from django.http import HttpResponse
from django.template import loader, RequestContext
import os.path

def home(request):
	
	contexts = RequestContext(request, {
		'title' : 'hello django!',
		'data' : ('Hello', 'django', 'world'),
	})
	
	PROJECT_DIR = os.path.dirname(__file__)
	TESTNAME = os.path.join(PROJECT_DIR, '/templates')

	here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
	PROJECT_ROOT = here('')
	root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

	#return HttpResponse(root('templates/home.html'))
	template = loader.get_template('index.html')
	return HttpResponse(template.render(contexts))
