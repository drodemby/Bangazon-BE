"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from Bangazonapi.models import Category, User, Product

class ProductView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except product.DoesNotExist:
          return Response({'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
 
       
        sellerId = User.objects.get(uid=request.data["sellerId"])
        catId = Category.objects.get(pk=request.data["categoryId"])

        product = product.objects.create(
            name=request.data["name"],
            image=request.data["image"],
            description=request.data["description"],
            price=request.data["price"],
            isAvailable=request.data["isAvailable"],
            category_id=catId,
            seller_id = sellerId
            
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)  
    
    def update(self, request, pk):

        product = product.objects.get(pk=pk)
        product.name = request.data["name"]
        product.image = request.data["image"]
        product.description=request.data["description"]
        product.price=request.data["price"]
        product.isAvailable=request.data["isAvailable"]
        product.category_id= Category.objects.get(pk=request.data["categoryId"])
        product.seller_id = User.objects.get(uid=request.data["sellerId"])
       

        product.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)   
    
    def destroy(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    
class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'description','category_id', 'price','isAvailable', 'seller_id')
