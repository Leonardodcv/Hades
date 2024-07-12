from django.urls import path
from erp.views import *

urlpatterns =[
    path("uno/", myfirstview, name="vista"),
    path("dos/", mysecondview, name="vista2"),
    path("tres/", myfirstview),
    path("cuatro/", myfirstview)
]