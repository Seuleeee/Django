from django.contrib import admin
from django.urls import path, include
from first import views

urlpatterns = [
    path('', include('first.urls')), # first라는 webapp별로 다른 urls를 관리하기위함
    path('admin/', admin.site.urls),
]
