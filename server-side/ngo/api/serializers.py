from rest_framework import serializers
from ngo.models import NGO

#Serializer for scholarship detail
class NGOSerializer(serializers.ModelSerializer):  
    state = serializers.StringRelatedField()            
    religion = serializers.StringRelatedField()
    country = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    stype = serializers.StringRelatedField()
    gender = serializers.StringRelatedField(many=True)
    class Meta:
        model = NGO
        fields = '__all__'


#Serializer for scholarship list
class NGOListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = NGO
        fields = ['title','slug','eligibility','updated_on']