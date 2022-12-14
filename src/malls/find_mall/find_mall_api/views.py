from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mall
from .serializers import MallSerializer


class MallListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the mall items
        '''
        malls = Mall.objects.all()
        serializer = MallSerializer(malls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MallDetailApiView(APIView):

    def get_object(self, mall_id):
        '''
        Helper method to get the object with given mall_id
        '''
        try:
            return Mall.objects.get(id = mall_id)
        except Mall.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, mall_id, *args, **kwargs):
        '''
        Retrieves the Mall with given mall_id
        '''
        mall_instance = self.get_object(mall_id)
        if not mall_instance:
            return Response(
                {"res": "Object with mall id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MallSerializer(mall_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
