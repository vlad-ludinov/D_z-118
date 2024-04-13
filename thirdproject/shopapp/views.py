from django.shortcuts import render
from .models import Product, Client, Order, Photo
from .forms import PhotoProduct
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.core.files.storage import FileSystemStorage



# pip install python-dateutil

import logging


logger = logging.getLogger(__name__)


def client(request, client_id):
    client_v = Client.objects.filter(pk=client_id).first()
    filters = ["all", "week", "month", "year"]
    return render(request, "shopapp/client.html", {"filters": filters, "client": client_v})


def photo_add(request, product_id):
    if request.method == "POST":
        product = Product.objects.filter(pk=product_id).first()
        form = PhotoProduct(request.POST, request.FILES)
        if form.is_valid():
            photo_f = form.cleaned_data.get("photo")
            print(photo_f.name)
            fs = FileSystemStorage()
            fs.save(photo_f.name, photo_f)
            photo_m = Photo(name=photo_f.name)
            photo_m.save()
            product.photo_id = photo_m.pk
            product.save()
    else:

        form = PhotoProduct()

    return render(request, "shopapp/photo.html", {"form": form})


def products(request, client_id, filter):
    time_filter = None
    filters = None
    if filter == "week":
        time_filter = relativedelta(weeks=1)
        filters = ["all", "month", "year"]
    elif filter == "month":
        time_filter = relativedelta(months=1)
        filters = ["all", "week", "year"]
    elif filter == "year":
        time_filter = relativedelta(years=1)
        filters = ["all", "week", "month"]
    products_list = []
    client = Client.objects.filter(pk=client_id).first()
    if filter == "all":
        orders = Order.objects.filter(client=client).all()
        for order in orders:
            for product in order.product.all():
                products_list.append(product)
        filters = ["week", "month", "year"]
    else:
        orders = Order.objects.filter(Q(client=client) & Q(date__gt=date.today()-time_filter)).all() #.filter(date__lt=date.today()-time_filter).all()
        for order in orders:
            for product in order.product.all():
                products_list.append(product)
    # orders = Order.objects.filter(client=client).all()
    # if filter == "all":
    #     for order in orders:
    #         for product in order.product.all():
    #             products_list.append(product)
    #     filters = ["week", "month", "year"]
    # else:
    #     for order in orders:
    #         for product in order.product.filter(date__gt=date.today()-time_filter).all():
    #             products_list.append(product)
    product_list_unique = []
    photos = Photo.objects.all()
    photos_id = []
    if photos:
        for photo in photos:
            photos_id.append(photo.id)
    for product in products_list:
        if product not in product_list_unique:
            product_list_unique.append(product)
    products_list_with_photo = []
    for product in product_list_unique:
        if photos_id:
            if product.photo_id in photos_id:
                photo_need = Photo.objects.filter(pk=product.photo_id).first()
                print(f"product: {product.id}, photo: {photo_need.name}")
                products_list_with_photo.append((product, photo_need))
            else:
                products_list_with_photo.append((product, None))
        else:
            products_list_with_photo.append((product, None))
    return render(request, "shopapp/products.html", {"filters": filters, "products": products_list_with_photo, "client": client})






















