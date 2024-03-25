from django.contrib import admin
from django.utils.safestring import mark_safe  # Для изображений
from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = (('image_tag', 'image'), 'name', 'description', ('price', 'quantity'), 'category')
    search_fields = ('name',)
    ordering = ('-name',)
    readonly_fields = ("image_tag",)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="100" height="150" />')
        else:
            return 'No Image Found'

    image_tag.short_description = 'Изображение'


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
