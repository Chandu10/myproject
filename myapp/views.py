from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from forms import MyRegistrationForm
from .models import myapp
#from myproject.myapp.models import Document
#from myproject.myapp.forms import DocumentForm
from .forms import DocumentForm
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm



def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = myapp.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def index(request):
    return render_to_response('myapp/index.html')


def home(request):
   return  render_to_response('home.html',
                    {'Testing' : 'Django Template Inheritance ',
                    'HelloHello' : 'Hello World - Django'})
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/dj/accounts/loggedin')
    else:
        return HttpResponseRedirect('/dj/accounts/invalid')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def loggedin(request):
    return render_to_response('loggedin.html',
                               {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def register_user(request):
    # 2nd time around
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dj/accounts/register_success')

    # 1st time visit
    args = {}
    args.update(csrf(request))

    # form with no input
    args['form'] = UserCreationForm()
    print args
    
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

