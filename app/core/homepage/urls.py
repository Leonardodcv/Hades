from core.homepage.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # otras rutas
]
