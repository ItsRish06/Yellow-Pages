from rest_framework import serializers
from scholarships.models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):
    sclass = serializers.StringRelatedField(many=True)
    state = serializers.StringRelatedField()
    course = serializers.StringRelatedField()
    religion = serializers.StringRelatedField()
    country = serializers.StringRelatedField()
    gender = serializers.StringRelatedField(many=True)
    class Meta:
        model = Scholarship
        fields = '__all__'

class ScholarshipListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Scholarship
        fields = ['title','image','slug','deadline','eligibility','award','updated_on']