from django.urls import path

from .views import HomePage,SnackListView , SnackDetailView

urlpatterns=[
    path('',HomePage.as_view(), name='home'),
    path('snacks/',SnackListView.as_view(), name='snacks' ),
    path('snacks/<pk>', SnackDetailView.as_view(),name='snack_detail'),
]