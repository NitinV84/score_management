from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, viewsets

from .models import *
from .permissions import *
from .serializers import *


class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.

    AllowAny permission is used to allow any user to register.
    """
    queryset = User.objects.all()
    serializer_class  = UserRegistrationSerializer
    permission_classes  = [permissions.AllowAny]


class ProfileView(generics.RetrieveAPIView):
    """
    API view for retrieving user profile.

    IsAuthenticated permission is used to allow only authenticated users to access their profiles.
    """
    queryset = User.objects.all()
    serializer_class  = UserRegistrationSerializer
    permission_classes  = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filters the queryset to retrieve only the profile of the authenticated user.
        """
        queryset = User.objects.filter(id=self.request.user.id)
        return queryset
    

class ApplicationCreateView(viewsets.ModelViewSet):
    """
    API view for creating, updating, reading, and listing applications.

    CanCreateApplication and CanUpdateApplication permissions are used to control
    create and update actions respectively.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [CanCreateApplication | CanUpdateApplication]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['category__name', 'application_date']
    
    def get_queryset(self):
        """
        Filters the queryset to retrieve only applications belonging to the authenticated user.
        """
        queryset = Application.objects.filter(user=self.request.user)
        return queryset

    def get_permissions(self):
        """
        Assigns specific permissions based on the action being performed.
        """
        if self.action in ['create']:
            return [CanCreateApplication()]
        elif self.action in ['update', 'partial_update']:
            return [CanUpdateApplication()]
        elif self.action in ['list', 'retrieve']:
            return [CanReadApplication()]
        else:
            return super().get_permissions()
