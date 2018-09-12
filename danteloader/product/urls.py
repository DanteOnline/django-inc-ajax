from django.urls import path

from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .views import ItemCreateView, ItemDeleteView, \
    ItemDetailView, ItemListView, ItemUpdateView, ItemTemplateView,\
    ProductTemplateView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductListView, ProductUpdateView

app_name = 'product'

view_list = [
    ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView,
    ItemDeleteView, ProductCreateView, ProductDeleteView,
    ProductDetailView, ProductListView, ProductUpdateView
]

result_patterns = []
for view in view_list:
    view_url = ''
    name = ''
    model_name = view.model._meta.model_name
    if issubclass(view, ListView):
        name = 'list'
        view_url = f'{name}/'
    # добавляем inс и html
    elif issubclass(view, CreateView):
        name = 'create'
        view_url = f'{name}/'
    elif issubclass(view, DetailView):
        name = 'detail'
        view_url = f'{name}/<int:pk>/'
    elif issubclass(view, DeleteView):
        name = 'delete'
        view_url = f'{name}/<int:pk>/'
    elif issubclass(view, UpdateView):
        name = 'update'
        view_url = f'{name}/<int:pk>/'
    view_url = model_name + '/' + view_url
    name = model_name + '_' + name
    print(view_url, name)
    result_patterns.append(path(view_url, view.as_view(), name = name))


urlpatterns = [
    path('', ItemTemplateView.as_view(), name='category'),
    # path('list/', ItemListView.as_view(), name='list'),
    # path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    # path('create/', ItemCreateView.as_view(), name='create'),
    # path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
]

urlpatterns += result_patterns