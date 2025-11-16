# data_kelurahan/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')),
    
    path('api/', include('warga.api_urls')),


    # 🔹 JWT Token Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 🔹 Redirect '/' ke halaman warga
    path('', RedirectView.as_view(url='/warga/')),
]
