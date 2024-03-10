from django.urls import path

from users.views import AboutUsView

urlpatterns = [
    path('', AboutUsView.as_view())
]
