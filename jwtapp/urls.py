from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns=[
	path('users/', Register.as_view({'post':'create'}), name='user-create'),
	path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh', TokenRefreshView.as_view(), name='token-refresh')
]
