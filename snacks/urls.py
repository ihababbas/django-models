from django.urls import path
from .views import HomePage,ThingListView

urlpatterns=[
    path('',HomePage.as_view(), name='home'),
    path('snacks/',ThingListView.as_view(), name='snacks' )
]