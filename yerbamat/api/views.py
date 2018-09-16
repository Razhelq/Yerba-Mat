from yerba_mat.models import Product
from api.models import Log
from api.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse


class ProductListView(APIView):

    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True, context={"request": request})
        response = Response(serializer.data)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            Log.objects.create(request=request.get_full_path, response=response)
            return response
        response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response


class ProductView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        product = self.get_object(id)
        serializer = ProductSerializer(product, context={"request": request})
        response = Response(serializer.data)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def delete(self, request, id, format=None):
        product = self.get_object(id)
        product.delete()
        response = Response(status=status.HTTP_204_NO_CONTENT)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def put(self, request, id, format=None):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data)
            Log.objects.create(request=request.get_full_path, response=response)
            return response
        response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def post(self, request, id, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            Log.objects.create(request=request.get_full_path, response=response)
            return response
        response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response


class WrongEndpointView(APIView):

    def get(self, request, format=None):
        response = Http404
        Log.objects.create(request=request.get_full_path, response=response)
        raise Http404

    def delete(self, request, format=None):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def put(self, request, format=None):
        response = Response(status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def post(self, request, format=None):
        response = Response(status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def patch(self, request, format=None):
        response = Response(status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response
