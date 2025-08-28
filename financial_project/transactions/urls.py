from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, TransactionViewSet, UserRegistrationView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
