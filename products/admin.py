from django.contrib import admin
from .models import Products,NewOffer


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')


class NewOfferAdmin(admin.ModelAdmin):
    list_display=('code','description','discount')


admin.site.register(NewOffer,NewOfferAdmin)
admin.site.register(Products, ProductAdmin)
