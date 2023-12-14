from django.urls import reverse_lazy

from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response

from .forms import *
from django.core.mail import send_mail
from .serializers import KvartiriListSerializer


class ShowIndexView(ListView):
    queryset = Kvartiri.objects.filter(pub='True')
    new = Kvartiri.objects.filter(pub='True').order_by('-created_at')[:3]
    vip = Kvartiri.objects.filter(vip='True').order_by('?')[:3].prefetch_related
    template_name = 'posutochno/index.html'
    context_object_name = 'kvartiri'
    paginate_by = 9

    title = 'Квартиры посуточно в Ростове-на-Дону'
    meta_descr = 'Снять квартиру посуточно в Ростове-на-Дону'
    meta_key = 'Снять квартиру посуточно в Ростове-на-Дону'
    main_title = 'Квартиры посуточно в Ростове-на-Дону'
    main_descr = 'На данном сайте представлен актуальный каталог квартир сдающихся посуточно в Ростове-на-Дону'

    def get_context_data(self, **kwargs):
        context = super(ShowIndexView, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['meta_descr'] = self.meta_descr
        context['meta_key'] = self.meta_key
        context['main_title'] = self.main_title
        context['main_descr'] = self.main_descr
        context['new'] = self.new
        context['vip'] = self.vip
        return context


class DetailsListView(DetailView):
    queryset = Kvartiri.objects.prefetch_related('images')
    vip = Kvartiri.objects.filter(vip='True').order_by('?')[:3]
    template_name = 'posutochno/details.html'
    context_object_name = 'kvartiri'

    title = 'Квартиры посуточно в Ростове-на-Дону'
    meta_descr = 'Снять квартиру посуточно в Ростове-на-Дону'
    meta_key = 'Снять квартиру посуточно в Ростове-на-Дону'
    main_title = 'Квартиры посуточно в Ростове-на-Дону'
    main_descr = 'На данном сайте представлен актуальный каталог квартир сдающихся посуточно в Ростове-на-Дону'

    def get_context_data(self, **kwargs):
        context = super(DetailsListView, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['meta_descr'] = self.meta_descr
        context['meta_key'] = self.meta_key
        context['main_title'] = self.main_title
        context['main_descr'] = self.main_descr
        context['vip'] = self.vip
        return context


fields_kvartiri = [
    'title',
    'city',
    'district',
    'address',
    'phone',
    'rooms',
    'stage',
    'place',
    'guest',
    'time_in',
    'time_out',
    'price',
    'description',
    'main_image',
    'image_1',
    'image_2',
    'image_3',
    'image_4',
    'image_5',
    'image_6',
    'image_7',
    'image_8',
    'image_9',
    'wifi',
    'kond',
    'tv',
    'holodilnik',
    'micro',
    'tea',
    'utug',
    'tehnika',
    'posuda',
    'stiralka',
]


class CreateKvartiriView(LoginRequiredMixin, CreateView):
    model = Kvartiri
    fields = fields_kvartiri

    # form_class = ImageForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UpdateKvartiriView(LoginRequiredMixin, UpdateView):
    model = Kvartiri
    fields = fields_kvartiri
    # form_class = ImageForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('profile')

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)


class KvartiriDeleteView(DeleteView):
    model = Kvartiri
    success_url = reverse_lazy('profile')


class ContactsView(CreateView):
    model = Contact
    template_name = "posutochno/contacts.html"
    success_url = reverse_lazy('index')
    fields = ['name', 'email', 'phone', 'message']

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Сообщение с формы от {data["name"]} Почта отправителя: {data["email"]} Телефон: {data["phone"]}'
        email(subject, data['message'])
        return super().form_valid(form)

    # Функция отправки сообщения


def email(subject, content):
    send_mail(subject,
              content,
              '',
              ['']
              )


# Функция, которая вернет сообщение в случае успешного заполнения формы


def success(request):
    return HttpResponse('Письмо отправлено!')


class RazmeshenieView(TemplateView):
    template_name = "posutochno/razmeshenie.html"


class PoliticView(TemplateView):
    template_name = "posutochno/politika.html"


class KvartiriListView(ListModelMixin, GenericAPIView):
    queryset = Kvartiri.objects.all()
    serializer_class = KvartiriListSerializer
    filters_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter
    ]
    search_fields = [
        'title',
        'description',

    ]
    filterset_fields = [
        'title',
    ]
    ordering_fields = [
        'title',
        'description',
        'created_at'
    ]

    def get(self, request: Request) -> Response:
        return self.list(request)

