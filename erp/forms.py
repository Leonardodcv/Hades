from django.forms import *
from erp.models import Category

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"'''
        self.fields["name"].widget.attrs["autofocus"] = True

    class Meta:
        model= Category
        fields = "__all__"

        widgets = {
            "name" : TextInput(
                attrs={
                    "placeholder":"Ingrese un nombre",
                }
            ),
            "descripcion" : Textarea(
                attrs={
                    "placeholder":"Descripción de la tarea",
                    "rows":3,
                    "cols":1
                }
            ),
        }

        '''def save(self, commit=True):
            data ={}
            form = super()
            try:
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            except Exception as e:
                data['error'] = str(e)
            return data'''