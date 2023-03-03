from rest_framework import serializers

from api.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        exclude = ['date_of_call']
