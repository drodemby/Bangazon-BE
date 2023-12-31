"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from Bangazonapi.models import Order, User

class OrderView(ViewSet):
    """Level up Categories view"""

    def create(self, request):
        """Handle GET requests for single Category

        Returns:
            Response -- JSON serialized Category
        """

        customerId = User.objects.get(uid=request.data["customerId"])
        order = Order.objects.create(
            status=request.data["status"],
            customer_id=customerId
            
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data)
  
    def retrieve(self, request, pk):
      try:
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
      except order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk):
        """Handle PUT requests for a order

        Returns:
            Response -- Empty body with 204 status code
        """

        order = order.objects.get(pk=pk)
        order.label = request.data["label"]
        order.customer_id = User.objects.get(uid=request.data["customerId"])
        order.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    def list(self, request):
        """Handle GET requests to get all category

        Returns:
            Response -- JSON serialized list of category
        """
        Order = Order.objects.all()
        serializer = OrderSerializer(Order, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        Order = Order.objects.get(pk=pk)
        Order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      

class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Order
        fields = ('id', 'customer_id', 'status')
