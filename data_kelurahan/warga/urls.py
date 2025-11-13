# warga/urls.py
from django.urls import path
from .views import (
    # View untuk Warga
    WargaListView, WargaDetailView, WargaCreateView,
    WargaUpdateView, WargaDeleteView,
    # View untuk Pengaduan
    PengaduanListView, PengaduanCreateView,
    PengaduanUpdateView, PengaduanDeleteView,
    # View API
    WargaListAPIView,   # ✅ tambahkan ini
)

urlpatterns = [
    # ======== WARGA ========
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),

    # ======== PENGADUAN ========
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),

    # ======== API (JSON) ========
    path('api/warga/', WargaListAPIView.as_view(), name='api-warga-list'),
]
