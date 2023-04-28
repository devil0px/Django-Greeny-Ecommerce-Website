from rest_framework import generics
from rest_framework.response import Response
from .serializers import OrderListSerializer
from .models import Order , OrderDetail
from rest_framework.permissions import IsAuthenticated 

class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


    def get_queryset(self):
        user = self.request.user
        print(user)
        return Order.objects.all().filter(user=self.request.user.id)
