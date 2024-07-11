from django.urls import path
from erp.views import myfirstview

urlpatterns =[
    path("uno/", myfirstview),
    path("dos/", myfirstview),
    path("tres/", myfirstview),
    path("cuatro/", myfirstview)
]