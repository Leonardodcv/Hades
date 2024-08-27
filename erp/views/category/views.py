from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from erp.models import Category
from django.db.models.query import QuerySet
from erp.models import Category, Product
from erp.forms import CategoryForm

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category/delete.html"
    success_url = reverse_lazy("erp:category_list")

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,  *args, ** kwargs):
        data= {}
        try:
            self.object.delete()
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["title"] = "Eliminacion de una categoria"
            context["entity"] = "Categorias"
            context["list_url"] = reverse_lazy("erp:category_list")
            return context

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/create.html"
    success_url = reverse_lazy("erp:category_list")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST.get('action')
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()  # Aquí se asegura de que se guarde correctamente.
                    data['success'] = 'Categoría actualizada correctamente.'
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar una categoria"
        context["entity"] = "Categorias"
        context["list_url"] = reverse_lazy("erp:category_list")
        context["action"] = "edit"
        return context

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
            #data = Category.objects.get(pk = request.POST["id"]).toJSON()
            action = request.POST["action"]
            if action == "searchdata":
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data["error"] = "Ha ocurrido un error"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de Categorias"
        context["create_url"] = reverse_lazy("erp:category_create")
        context["list_url"] = reverse_lazy("erp:category_list")
        context["entity"] = "Categorias"
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name= "category/create.html"
    success_url = reverse_lazy("erp:category_list")

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action=request.POST["action"]
            if action == "add":
                form = self.get_form()
                #form = CategoryForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data["error"] = form.errors
            else:
                data["error"] = "No se ha integrado ninguna opción"
        except Exception as e:
            data["error"] = "el error es:"+str(e)
        return JsonResponse(data)
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Crear una categoria"
        context["entity"] = "Categorias"
        context["list_url"] = reverse_lazy("erp:category_list")
        context["action"] = "add"
        return context





