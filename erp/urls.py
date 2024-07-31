from django.urls import path
from erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
]
