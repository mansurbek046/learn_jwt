from django.urls import path, include
from .views import *

urlpatterns=[
	path('users/', Register.as_view({'post':'create'}), name='user-create'),
	path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair')
]
