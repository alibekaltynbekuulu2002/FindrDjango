from django.urls import path
from . import views


urlpatterns = [
    path('',views.get_user_list),
    path('<int:id>',views.get_user),
    path('update/<int:id>',views.update_user),
    path('delete/<int:id>',views.delete_user),
    path('create',views.create_user)
]