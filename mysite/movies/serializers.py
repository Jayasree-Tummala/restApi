from rest_framework import serializers
from .models import Moviedata

class MovieSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length = None,use_url = True )
    class Meta:
        model = Moviedata
        fields = ['id','name','duration','rating','typ','image']
        #Here we are creating a JSON response.