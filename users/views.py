from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


@api_view(['GET'])
def get_users(request, *args, **kwargs):
    pass


@api_view(['GET', 'POST'])
def get_user(request, id):
    pass


@api_view(['DELETE'])
def delete_user(request, id):
    pass


@api_view('PUT', 'PATCH')
def update_user(request, id):
    pass
