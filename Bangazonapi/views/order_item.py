from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from Bangazonapi.models import OrderItem, Order, Product

class OrderItemView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            orderitem = OrderItem.objects.get(pk=pk)
            serializer = OrderItemSerializer(orderitem)
            return Response(serializer.data)
        except OrderItem.DoesNotExist:
          return Response({'message': 'Cart is empty'}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        orderitem = OrderItem.objects.all()
        serializer = OrderItemSerializer(post, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
 
       
        orderId = Order.objects.get(uid=request.data["orderId"])
        productId = Product.objects.get(pk=request.data["productId"])

        orderitem = OrderItem.objects.create(
            order = orderId,
            product =productId,
            quantity=request.data["quantity"]   
        )
        serializer = OrderItemSerializer(orderitem)
        return Response(serializer.data)  
    
    def update(self, request, pk):
      
        orderitem = OrderItem.objects.get(pk=pk)
        orderitem.product_id= Product.objects.get(pk=request.data["productId"])
        orderitem.order_id = Order.objects.get(uid=request.data["orderId"])
        
        orderitem.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
class OrderItemSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = OrderItem
        fields = ('id', 'order_id', 'product_id', 'quantity')

    