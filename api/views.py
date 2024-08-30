from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(req):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addData(req):
    serializer = ItemSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
