from django.urls import reverse
from pytils.translit import slugify
from PIL import Image
from django.contrib.auth.models import User
from users.models import *


class District(models.Model):
    title = models.CharField('Район', max_length=200)

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.title


class Kvartiri(models.Model):
    vip = models.BooleanField('VIP статус', default=False)
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', unique=False, null=True, blank=True)
    address = models.CharField('Адрес', max_length=200)
    city = models.CharField('Город', max_length=200, default='Ростов-на-Дону')
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Район')
    phone = models.CharField('Телефон', max_length=200)
    rooms = models.SmallIntegerField(
        'Количество комнат', default=1, null=False, blank=True)
    price = models.SmallIntegerField('Цена')
    description = models.TextField('Описание', max_length=5000)
    main_image = models.ImageField(
        'Главное фото', upload_to='media/kvartiri/main_pics/%Y/%m/')

    image_1 = models.ImageField(
        'Дополнительное фото 1', upload_to='media/kvartiri/dop_img/%Y/%m/', null=True, blank=True)
    image_2 = models.ImageField(
        'Дополнительное фото 2', upload_to='media/kvartiri/dop_img/%Y/%m/', null=True, blank=True)
    image_3 = models.ImageField(
        'Дополнительное фото 3', upload_to='media/kvartiri/dop_img/%Y/%m/', null=True, blank=True)
    image_4 = models.ImageField(
        'Дополнительное фото 4', upload_to='media/kvartiri/dop_img/%Y/%m/', null=True, blank=True)
    image_5 = models.ImageField(
        'Дополнительное фото 5', upload_to='media/kvartiri/dop_img/%Y/%m/', null=True, blank=True)
    image_6 = models.ImageField(
        'Дополнительное фото 6', upload_to='media/kvartiri/dop_img/%Y/%m/', null=True, blank=True)
    image_7 = models.ImageField(
        'Дополнительное фото 7', upload_to='media/kvartiri/dop_img/%Y/%m/', null=True, blank=True)
    image_8 = models.ImageField(
        'Дополнительное фото 8', upload_to='media/kvartiri/dop_img/%Y/%m/', null=True, blank=True)
    image_9 = models.ImageField(
        'Дополнительное фото 9', upload_to='media/kvartiri/dop_img/%Y/%m/', null=True, blank=True)

    tehnika = models.BooleanField('Бытовая техника', default=False)
    posuda = models.BooleanField('Столовые принадлежности', default=False)
    stiralka = models.BooleanField('Стиральная машина', default=False)
    wifi = models.BooleanField('Бесплатный WiFi', default=False)
    kond = models.BooleanField('Кондондиционер', default=False)
    tv = models.BooleanField('Телевизор', default=True)
    holodilnik = models.BooleanField('Холодильник', default=True)
    micro = models.BooleanField('Микроволновка', default=False)
    tea = models.BooleanField('Чайник', default=True)
    utug = models.BooleanField('Утюг', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    archived = models.BooleanField('В архив', default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    perm_pub = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                 default=True, verbose_name='Разрешение на публикацию')
    pub = models.BooleanField('Разрешение на публикацию', default=True)

    stage = models.IntegerField('Этаж', default=1, blank=False, null=False)
    place = models.IntegerField(
        'Количество спальных мест', default=1, blank=False, null=False)
    guest = models.IntegerField(
        'Количество гостей', default=1, blank=False, null=False)
    time_in = models.IntegerField(
        'Время заезда', default=12, blank=False, null=False)
    time_out = models.IntegerField(
        'Время выезда', default=14, blank=False, null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("details", kwargs={"slug": self.slug})
        return reverse("details", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save()

        if self.main_image:
            img = Image.open(self.main_image.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                img.save(self.main_image.path)

        if self.image_1:
            img_1 = Image.open(self.image_1.path)
            if self.image_1:
                if img_1.height > 1000 or img_1.width > 1000:
                    output_size = (1000, 1000)
                    img_1.thumbnail(output_size)
                    img_1.save(self.image_1.path)

        if self.image_2:
            img_2 = Image.open(self.image_2.path)
            if self.image_2:
                if img_2.height > 1000 or img_2.width > 1000:
                    output_size = (1000, 1000)
                    img_2.thumbnail(output_size)
                    img_2.save(self.image_2.path)

        if self.image_3:
            img_3 = Image.open(self.image_3.path)
            if self.image_2:
                if img_3.height > 1000 or img_3.width > 1000:
                    output_size = (1000, 1000)
                    img_3.thumbnail(output_size)
                    img_3.save(self.image_3.path)

        if self.image_4:
            img_4 = Image.open(self.image_4.path)
            if self.image_4:
                if img_4.height > 1000 or img_4.width > 1000:
                    output_size = (1000, 1000)
                    img_4.thumbnail(output_size)
                    img_4.save(self.image_4.path)

        if self.image_5:
            img_5 = Image.open(self.image_5.path)
            if self.image_5:
                if img_5.height > 1000 or img_5.width > 1000:
                    output_size = (1000, 1000)
                    img_5.thumbnail(output_size)
                    img_5.save(self.image_5.path)

        if self.image_6:
            img_6 = Image.open(self.image_6.path)
            if self.image_6:
                if img_6.height > 1000 or img_6.width > 1000:
                    output_size = (1000, 1000)
                    img_6.thumbnail(output_size)
                    img_6.save(self.image_6.path)

        if self.image_7:
            img_7 = Image.open(self.image_7.path)
            if self.image_7:
                if img_7.height > 1000 or img_7.width > 1000:
                    output_size = (1000, 1000)
                    img_7.thumbnail(output_size)
                    img_7.save(self.image_7.path)

        if self.image_8:
            img_8 = Image.open(self.image_8.path)
            if self.image_8:
                if img_8.height > 1000 or img_8.width > 1000:
                    output_size = (1000, 1000)
                    img_8.thumbnail(output_size)
                    img_8.save(self.image_8.path)

        if self.image_9:
            img_9 = Image.open(self.image_9.path)
            if self.image_9:
                if img_9.height > 1000 or img_9.width > 1000:
                    output_size = (1000, 1000)
                    img_9.thumbnail(output_size)
                    img_9.save(self.image_9.path)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Квартиру'
        verbose_name_plural = 'Квартиры'
        ordering = ['?']


def images_directory_path(instance: 'Images', filename: str) -> str:
    return 'media/kvartiri/kvartira_dop/images/{filename}'.format(
        filename=filename
    )


class Images(models.Model):
    kv_images = models.ForeignKey(
        Kvartiri, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to=images_directory_path)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Contact(models.Model):
    name = models.CharField('Имя', max_length=255)
    email = models.EmailField('Email', max_length=255)
    phone = models.CharField('Телефон', max_length=255)
    message = models.TextField('Сообщение', blank=True, max_length=5000)
    create_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self) -> str:
        return self.email
