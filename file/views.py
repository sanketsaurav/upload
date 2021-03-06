from file.models import file_file
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from file.forms import file_fileForm


def home(request):
    return render(request, 'file/home.html')

def about(request):
    return render(request, 'file/about.html')


def add_file(request):
    context = RequestContext(request)

    if request.method == 'POST': # If the form has been submitted...
        form = file_fileForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            # file is saved
            newfile = file_file(docfile = request.FILES['files'])
            newfile.save()
            return HttpResponseRedirect('/file/home') # Redirect after POST

        else:
            form = file_fileForm() # An unbound form

    else:
        form = file_fileForm()
  
    docs = file_file.objects.all()
   
    return render_to_response('file/add_file.html', {'docs': docs, 'form': form}, context)







