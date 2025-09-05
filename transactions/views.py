from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserRegistrationSerializer, AccountSerializer, TransactionSerializer
from .models import Account, Transaction
from .permissions import IsAdminOrReadOnly, IsFinancialAnalystOrReadOnly, IsAuditorReadOnly

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAdminOrReadOnly | IsFinancialAnalystOrReadOnly | IsAuditorReadOnly]

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        kwargs['context']['changed_by'] = self.request.user
        return super().get_serializer(*args, **kwargs)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAdminOrReadOnly | IsFinancialAnalystOrReadOnly | IsAuditorReadOnly]

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        kwargs['context']['changed_by'] = self.request.user
        return super().get_serializer(*args, **kwargs)
