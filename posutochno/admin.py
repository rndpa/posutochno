from django.contrib import admin
from .models import *


# class KvartiriInline(admin.StackedInline):
#     '''Stacked Inline View for '''

#     model = Images

@admin.register(Kvartiri)
class KvartiriAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'price', 'created_by', 'pub', 'vip', 'created_at')
    list_display_links = ('title',)

    search_fields = ('title', 'address', 'price')

    prepopulated_fields = {'slug': ('title',)}

    # inlines = [KvartiriInline]

    fieldsets = (
        (None, {
            "fields": (
                'title', 
                'pub', 
                'vip', 
                'price', 
                'slug', 
                'address', 
                'city', 
                'district', 
                'phone', 
                'rooms', 
                'stage', 
                'place', 
                'guest',
                'time_in',
                'time_out',
                'created_by'
            ),
        }),
        ('Описание', {
            "fields": ('description',),
        }),
        ('Главное фото', {
            "fields": ('main_image',),
        }),
        ('Дополнительное фото №1', {
            'fields': ('image_1',), }),
        ('Дополнительное фото №2', {
            'fields': ('image_2',), }),
        ('Дополнительное фото №3', {
            'fields': ('image_3',), }),
        ('Дополнительное фото №4', {
            'fields': ('image_4',), }),
        ('Дополнительное фото №5', {
            'fields': ('image_5',), }),
        ('Дополнительное фото №6', {
            'fields': ('image_6',), }),
        ('Дополнительное фото №7', {
            'fields': ('image_7',), }),
        ('Дополнительное фото №8', {
            'fields': ('image_8',), }),
        ('Дополнительное фото №9', {
            'fields': ('image_9',), }),
        ('Дополнительные услуги и устройства', {
            "fields": (
                'tehnika',
                'posuda',
                'stiralka',
                'wifi',
                'kond',
                'tv',
                'holodilnik',
                'micro',
                'tea',
                'utug'
            ),
        }),
        # ('Архивирование', {
        #     "fields": ('archived',),
        # })
    )


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('title', 'pk')
    list_display_links = ('title',)
    search_fields = ('title',)
