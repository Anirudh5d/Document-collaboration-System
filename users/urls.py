from django.urls import path
from .views import (
    UserProfileListCreateView,
    UserProfileRetrieveUpdateDestroyView,
    UserRoleListCreateView,
    UserRoleRetrieveUpdateDestroyView,
     RegisterView, LoginView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)
urlpatterns = [
    path('api/userprofiles/', UserProfileListCreateView.as_view(), name='userprofile-list-create'),
    path('api/userprofiles/<int:pk>/', UserProfileRetrieveUpdateDestroyView.as_view(), name='userprofile-detail'),
    path('api/userroles/', UserRoleListCreateView.as_view(), name='userrole-list-create'),
    path('api/userroles/<int:pk>/', UserRoleRetrieveUpdateDestroyView.as_view(), name='userrole-detail'),
    path('api/users/register/', RegisterView.as_view(), name='register'),
    path('api/users/login/', LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
