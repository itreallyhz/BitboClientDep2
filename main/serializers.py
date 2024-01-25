from rest_framework.serializers import ModelSerializer
from . models import ResidentInformation

class ResidentInformationSerializer(ModelSerializer):
    class Meta:
        model = ResidentInformation
        fields = '__all__'

        #You can also serialize specific data only 
        #eg.: fields = ['first_name']
        #