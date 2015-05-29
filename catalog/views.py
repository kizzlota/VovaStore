# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Shoes, Category
# Create your views here.


def index(request):
    category = request.GET.get('c', u'Чоботи')

    list_category = Category.objects.all()

    shoes = Shoes.objects.filter(category_name__name = category ).order_by( '-id' )

    return render(request, 'catalog/index.html', {'category': list_category, 'shoes': shoes})