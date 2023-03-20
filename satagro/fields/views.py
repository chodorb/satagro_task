from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from fields.models import Field
from fields.serializers import FieldSerializer

from techlines.serializers import TechlineSerializer
from techlines.models import TechLine


class FieldDetailAPIView(APIView):
    def get_object(self,pk):
        try:
            return Field.objects.get(pk=pk)
        except Field.DoesNotExist:
            return None
        
    def get(self,request,pk):
        field = self.get_object(pk)
        if field is None:
            return Response({'error':"field not found"},status = status.HTTP_404_NOT_FOUND)
        serializer = FieldSerializer(field)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FieldTechlinesDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Field.objects.get(pk=pk)
        except Field.DoesNotExist:
            return None
        
    def get(self,request,pk):
        field = self.get_object(pk)
        techlines = TechLine.objects.filter(field_id=pk)
        
        serializer = FieldSerializer(field)
        data = serializer.data
        
        data['techlines'] = TechlineSerializer(techlines, many=True).data
        
        return Response(data,status=status.HTTP_200_OK)