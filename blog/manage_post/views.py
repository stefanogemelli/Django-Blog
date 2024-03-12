from django.views.generic import ListView, DetailView
from manage_post.models import Article, Category

class IndexView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Enviar un articulo: estado=True
        context["articles"] = Article.objects.filter(status=True)

        #Obtener la información de las categorías destacadas
        context["navbar_category"] = Category.objects.filter(featured=True)
        return context

class CategoryDetailView(DetailView):
    model = Category

    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Enviar articulos activos de acuerdo a su categoría
        context["articles"] = Article.objects.filter(status=True).filter(
            catecories=Category.objects.get(slug=self.kwargs["slug"])
            )
        
        #Obtener la información de las categorias destacadas
        context["navbar_category"] = Category.objects.filter(featured=True)
        return context
    
class ListAllCategoriesView(ListView):
    model = Category
    context_object_name = "categories"

class ShowPostDetailView(DetailView):
    model = Article
    context_object_name = "article"
