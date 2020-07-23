from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),#앞의 ''은 url치고 들어오자마자 라는 뜻임. first라는 package 안의 view라는 python파일의 index라는 method를 연결할것임.
    path('select/', views.select, name="select"),
    path('result/', views.result, name="result"),

    # path('select/<int:year>/', .., ..) #숫자가 들어오면 year로 받아서 넣어줘라. ex select/2019/ int, slug, str 등 datatype으로 보내기 가능
]