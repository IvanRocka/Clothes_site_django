from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000/
    path('cats/<slug:cat_name>/', categories), # http://127.0.0.1:8000/cats/{1..n}/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]