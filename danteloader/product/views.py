from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.base import TemplateResponseMixin

from .models import Category, Product

Model = Category
APP_NAME = 'product'


class ItemTemplateResponseMixin(TemplateResponseMixin):

    def get_template_names(self):
        if self.template_name is None:
            # формируем шаблоны сами
            # добавляем название модели
            model_name = ''
            if hasattr(self, 'model'):
                model_name = self.model._meta.model_name
                model_name = f'inc/{model_name}/'

            name = 'empty'
            if isinstance(self, ListView):
                name = 'list'
            # добавляем inс и html
            elif isinstance(self, CreateView):
                name = 'create'
            elif isinstance(self, DetailView):
                name = 'detail'
            elif isinstance(self, DeleteView):
                name = 'delete'
            elif isinstance(self, UpdateView):
                name = 'update'

            self.template_name = f'{APP_NAME}/{model_name}{name}.html'
        return [self.template_name]


class ItemTemplateView(TemplateView, ItemTemplateResponseMixin):
    pass
    # template_name =


class ItemListView(ListView, ItemTemplateResponseMixin):
    model = Model
    paginate_by = 5

# страница с деталями
class ItemDetailView(DetailView, ItemTemplateResponseMixin):
    model = Model


# страница с созданием
class ItemCreateView(CreateView, ItemTemplateResponseMixin):
    model = Model
    # редиректим на себя
    success_url = reverse_lazy(f'{APP_NAME}:category_create')
    fields = '__all__'


class ItemUpdateView(UpdateView, ItemTemplateResponseMixin):
    model = Model
    # редиректим на себя
    success_url = reverse_lazy(f'{APP_NAME}:category_create')
    fields = '__all__'


class ItemDeleteView(DeleteView, ItemTemplateResponseMixin):
    model = Model
    # template_name = self.delete_template_name
    success_url = reverse_lazy(f'{APP_NAME}:category_create')


Model = Product


class ProductTemplateView(TemplateView, ItemTemplateResponseMixin):
    pass
    # template_name =


class ProductListView(ListView, ItemTemplateResponseMixin):
    model = Model
    paginate_by = 100

# страница с деталями
class ProductDetailView(DetailView, ItemTemplateResponseMixin):
    model = Model


# страница с созданием
class ProductCreateView(CreateView, ItemTemplateResponseMixin):
    model = Model
    # редиректим на себя
    success_url = reverse_lazy(f'{APP_NAME}:product_create')
    fields = '__all__'


class ProductUpdateView(UpdateView, ItemTemplateResponseMixin):
    model = Model
    # редиректим на себя
    success_url = reverse_lazy(f'{APP_NAME}:product_create')
    fields = '__all__'


class ProductDeleteView(DeleteView, ItemTemplateResponseMixin):
    model = Model
    # template_name = self.delete_template_name
    success_url = reverse_lazy(f'{APP_NAME}:product_create')