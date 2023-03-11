from django.urls import path

from api.views import ContactAPIView

urlpatterns = [
    path('contact/', ContactAPIView.as_view()),
]