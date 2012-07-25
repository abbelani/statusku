# Create your views here.
from django.shortcuts import *
from notes.models import *
from django.template import RequestContext

def index(request):
    latest_notes_list = Note.objects.all().order_by('-pub_date')[:20]
    return render_to_response('notes/index.html', {'latest_notes_list': latest_notes_list})

def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect('/notes/') # Redirect after POST
    else:
            form = NoteForm() # An unbound form
    return render_to_response('notes/add.html', {'form': form,}, context_instance=RequestContext(request))
