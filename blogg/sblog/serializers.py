from rest_framework.serializers import ModelSerializer
from sblog.models import Createdata


class CreateDataSerializer(ModelSerializer):
    class Meta:
        model = Createdata
        fields = ('fname','lname','age','email','timestamp')

    #def get_url(self, obj):
        # request
    #    request = self.context.get("request")
    #    return obj.get_api_url(request=request)


