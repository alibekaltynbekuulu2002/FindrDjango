from django.urls import path
from . import views


urlpatterns = [
    path('/', views.get_users, name='get_users'),
    path('/<int:id>', views.get_user, name='get_user'),
    path('/update/<int:id>', views.update_user, name='update_user'),
    path('/delete/<int:id>', views.delete_user, name='delete_user')
]
