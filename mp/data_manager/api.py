from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie import fields, utils

from data_manager.models import Layer, Theme


class ThemeResource(ModelResource):
    class Meta:
        queryset = Theme.objects.all()
        resource_name = 'theme'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True


class LayerResource(ModelResource):
    themes = fields.ToManyField(ThemeResource, 'themes', null=True, full=True)
    
    class Meta:
        queryset = Layer.objects.all()
        resource_name = 'layer'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
