from django.urls import path
from .views import Register, MyTokenObtainPairView

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]