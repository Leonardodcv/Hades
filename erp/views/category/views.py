
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from erp.models import Category
from django.db.models.query import QuerySet
#from django.contrib.auth.decorators import login_required
from erp.models import Category, Product
from erp.forms import CategoryForm

def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = "category/list.html"

    def get_queryset(self):
        return Category.objects.all()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk = request.POST["id"]).toJSON()
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de Categorias"
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name= "category/create.html"
    success_url = reverse_lazy("erp:category_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Crear una categoria"
        return context







