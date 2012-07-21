from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from notes.models import Note
from tastypie.api import Api

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']

class NoteResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(NoteResource())
