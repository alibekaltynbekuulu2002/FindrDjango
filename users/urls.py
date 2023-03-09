from django.urls import path
from . import views


urlpatterns = [
    path('',views.UserListApiView.as_view()),
    path('<int:id>',views.UserGetApiView.as_view()),
    path('update/<int:id>',views.UserUpdateApiView.as_view()),
    path('delete/<int:id>',views.UserDeleteApiView.as_view())
]