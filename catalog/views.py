from django.shortcuts import render
from .models import Product, Category, Tag


def product_list(request):
    products = Product.objects.all()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    description_query = request.GET.get('description')
    category_id = request.GET.get('category')
    tag_ids = request.GET.getlist('tags')

    if description_query:
        products = products.filter(description__icontains=description_query)

    if category_id:
        products = products.filter(category__id=category_id)

    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
        'selected_category': category_id,
        'selected_tags': tag_ids,
    }
    return render(request, 'catalog/product_list.html', context)
