from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from base.models import Item
from .serializers import ItemSerializer


class ItemViewSet(APIView):
    def get(self, req):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)

        return Response(serializer.data)

    def post(self, req):
        serializer = ItemSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
