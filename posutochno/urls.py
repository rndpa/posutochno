from django.urls import path
from posutochno.views import *

urlpatterns = [
    # Главная
    path('', ShowIndexView.as_view(), name='index_kvartiri'),

    path('api/', KvartiriListView.as_view(), name='api_kvartiri'),

    # Меню
    path('квартира-посуточно-в-ростове/добавить-квартиру/',
         CreateKvartiriView.as_view(), name='create_kvartiri'),
    path('размещение/',
         RazmeshenieView.as_view(), name='razmeshenie'),
    path('контакты/',
         ContactsView.as_view(), name='contacts'),
    path('политика-конфеденциальности/',
         PoliticView.as_view(), name='politica'),
    
    # Детали
    path('квартира-посуточно-в-ростове/<slug:pk>/',
         DetailsListView.as_view(), name='details'),
    path('квартира-посуточно-в-ростове/<slug:pk>/обновить/',
         UpdateKvartiriView.as_view(), name='update_kvartiri'),
    path('квартира-посуточно-в-ростове/<slug:pk>/удалить/',
         KvartiriDeleteView.as_view(), name='delete_kvartiri'),
]
