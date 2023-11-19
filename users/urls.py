from django.urls import path
from users.views import RegisterView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register'),
    path('get/<int:pk>/', UserView.as_view(), name='user_get')
]
