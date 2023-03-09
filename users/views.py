from .models import User,UserAddress,UserPayment
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser

@api_view(['GET'])
@parser_classes([JSONParser])
def get_user_list(request):
    """
    RETURNS ALL USERS
    """
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)



@api_view(['GET'])
@parser_classes([JSONParser])
def get_user(request,id):
    """
    RETURNS USER BY LOOKING UP IT'S ID
    """
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'message':'User was not found.'},status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)



@api_view(['PATCH','PUT'])
@parser_classes([JSONParser])
def update_user(request,id):
    """
    UPDATES USER -> PATCH & PUT
    """
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'message':'User was not found.'},status=status.HTTP_404_NOT_FOUND)
    partial = True
    if request.method == 'PUT':
        partial = False
    serializer = UserSerializer(user,data=request.data,partial=partial)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_user(request,id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'message':'User was not found.'},status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response({'message':'User DELETED Successfully.'},status=status.HTTP_200_OK)



@api_view(['POST'])
@parser_classes([JSONParser])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

