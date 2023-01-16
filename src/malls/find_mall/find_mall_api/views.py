from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Mall, Categories, Item
from .serializers import MallSerializer, CategoriesSerializer, ItemSerializer

def dict2obj(d):
        if isinstance(d, list):
            d = [dict2obj(x) for x in d]
        if not isinstance(d, dict):
            return d
        class C(object):
            pass
        o = C()
        for k in d:
            o.__dict__[k] = dict2obj(d[k])
        return o

class MallListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the mall items
        '''
        malls = Mall.objects.all()
        serializer = MallSerializer(malls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        '''
        Create the mall with given mall data
        '''
        data = {
            'title': request.data.get('title'),
            'location': request.data.get('location')
        }
        serializer = MallSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MallDetailApiView(APIView):

    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
                {"error": "Object with mall id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MallSerializer(mall_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, mall_id, *args, **kwargs):
        '''
        Updates the mall item with given mall_id if exists
        '''
        mall_instance = self.get_object(mall_id)
        if not mall_instance:
            return Response(
                {"error": "Object with mall id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'location': request.data.get('location')
        }
        serializer = MallSerializer(
            instance=mall_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, mall_id, *args, **kwargs):
        '''
        Deletes the mall item with given mall_id if exists
        '''
        mall_instance = self.get_object(mall_id)
        if not mall_instance:
            return Response(
                {"error": "Object with mall id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        mall_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class CategoriesListApiView(APIView):

    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Categories items
        '''
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        '''
        Create the category with given category data
        '''
        data = {
            'title': request.data.get('title')
        }
        serializer = CategoriesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesDetailApiView(APIView):

    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, category_id):
        '''
        Helper method to get the object with given category_id
        '''
        try:
            return Categories.objects.get(id=category_id)
        except Categories.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, category_id, *args, **kwargs):
        '''
        Retrieves the Categories with given Category_id
        '''
        categories_instance = self.get_object(category_id)
        if not categories_instance:
            return Response(
                {"error": "Object with category id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CategoriesSerializer(categories_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, category_id, *args, **kwargs):
        '''
        Updates the category item with given category_id if exists
        '''
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"error": "Object with category id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title')
        }
        serializer = CategoriesSerializer(
            instance=category_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, category_id, *args, **kwargs):
        '''
        Deletes the category item with given category_id if exists
        '''
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"error": "Object with category id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        category_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class ItemsListApiView(APIView):

    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the items
        '''
        items = Item.objects.all()
        #print(items)
        serializer = ItemSerializer(items, many=True)
        arr = []
        arr_mall=[]
        for inst in serializer.data:
            dic = dict(inst)
            for mall in dic.get('malls'):
                arr_mall.append(MallDetailApiView.get_object(MallDetailApiView, mall))
            newdict = {'category':
                CategoriesSerializer(CategoriesDetailApiView.get_object(CategoriesDetailApiView, dic.get('category'))).data,
                'malls':MallSerializer(arr_mall,many=True).data}
            dic.update(newdict)
            arr.append(dic)
        #print(arr)
        return Response(arr, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the item with given item data
        '''
        category_instance = CategoriesDetailApiView.get_object(CategoriesDetailApiView,
            request.data.get('category'))
        if not category_instance:
            return Response(
                {'error': "The category doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        for mall in request.data.get('malls'):
            mall_instance = MallDetailApiView.get_object(MallDetailApiView, mall)
            if not mall_instance:
                return Response(
                    {'error': "The mall doesn't exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        data = {
            'title': request.data.get('title'),
            'malls': request.data.get('malls'),
            'category': request.data.get('category')       
        }
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemsDetailApiView(APIView):

    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, item_id):
        '''
        Helper method to get the object with given item_id
        '''
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, item_id, *args, **kwargs):
        '''
        Retrieves the items with given Items_id
        '''
        item_instance = self.get_object(item_id)
        if not item_instance:
            return Response(
                {"error": "Object with item id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ItemSerializer(item_instance)
        arr = []
        arr_mall=[]
        dic = dict(serializer.data)
        for mall in dic.get('malls'):
                arr_mall.append(MallDetailApiView.get_object(MallDetailApiView, mall))
        newdict = {'category':
                CategoriesSerializer(CategoriesDetailApiView.get_object(CategoriesDetailApiView, dic.get('category'))).data,
                'malls':MallSerializer(arr_mall,many=True).data}
        dic.update(newdict)
        arr.append(dic)
        return Response(arr, status=status.HTTP_200_OK)
    
    # 4. Update
    def put(self, request, item_id, *args, **kwargs):
        '''
        Updates the item with given item_id if exists
        '''
        item_instance = self.get_object(item_id)
        if not item_instance:
            return Response(
                {"error": "Object with item id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        category_instance = CategoriesDetailApiView.get_object(CategoriesDetailApiView, request.data.get('category'))
        if not category_instance:
            return Response(
                {'error': "The category doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        for mall in request.data.get('malls'):
            mall_instance = MallDetailApiView.get_object(
                MallDetailApiView, mall)
            if not mall_instance:
                return Response(
                    {'error': "The mall doesn't exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        data = {
            'title': request.data.get('title'),
            'malls': request.data.get('malls'),
            'category': request.data.get('category')
        }
        serializer = ItemSerializer(
            instance=item_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, item_id, *args, **kwargs):
        '''
        Deletes the item with given item_id if exists
        '''
        item_instance = self.get_object(item_id)
        if not item_instance:
            return Response(
                {"error": "Object with item id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        item_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
