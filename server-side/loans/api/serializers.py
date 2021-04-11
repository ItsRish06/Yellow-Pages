from rest_framework import serializers
from loans.models import Loan

#Serializer for loan detail
class LoanSerializer(serializers.ModelSerializer): 
    state = serializers.StringRelatedField()            # many=True indicates many to many relation.
    District = serializers.StringRelatedField()
    religion = serializers.StringRelatedField()
    country = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    LoanAmt = serializers.StringRelatedField()
    class Meta:
        model = Loan
        fields = '__all__'


#Serializer for loan list
class LoanListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Loan
        fields = ['title','image','slug','deadline','eligibility','award','updated_on']