# Create your views here.
from django.shortcuts import render_to_response
from notes.models import Note

def index(request):
    latest_notes_list = Note.objects.all().order_by('-pub_date')[:20]
    return render_to_response('notes/index.html', {'latest_notes_list': latest_notes_list})
