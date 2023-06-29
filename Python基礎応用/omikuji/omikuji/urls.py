
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('kanri/', admi.site.urls),
    path('', include('omikuji.urls')),
]
