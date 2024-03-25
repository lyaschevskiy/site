from django.urls import path
from .views import products, product_index, basket_add, basket_remove, basket_update

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:product_id>/', product_index, name='product_index'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_number>', products, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/update/<int:product_id>/', basket_update, name='basket_update'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove')
]
