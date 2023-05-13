from django.urls import path, include
from rest_framework import routers

from oauth.views import ProfileInfoVIew, CreateStudentUserView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('me/', ProfileInfoVIew.as_view(), name='auth_me'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('registration/', CreateStudentUserView.as_view(), name='registration'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls'))
]
