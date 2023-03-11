from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Contact
from api.serializers import ContactSerializer


class ContactAPIView(APIView):

    def get(self, request, format=None):
        if 'non_checked' in request.query_params:
            contacts = Contact.objects.filter(is_checked=False)    
        else:
            contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        ...
