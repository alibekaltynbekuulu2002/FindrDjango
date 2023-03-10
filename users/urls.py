from django.urls import path
from . import views


urlpatterns = [
    path('',views.get_user_list,name='user-list'),
    path('<int:id>',views.get_user,name='user-detail'),
    path('update/<int:id>',views.update_user),
    path('delete/<int:id>',views.delete_user),
    path('create',views.create_user),
    path('<int:id>/address',views.get_user_address),
    path('addresses/',views.get_user_addresses)
]