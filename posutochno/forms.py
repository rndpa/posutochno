from django import forms

from posutochno.models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = Kvartiri
        fields = [
            'title',
            'city',
            'district',
            'address',
            'price',
            'phone',
            'rooms',
            'stage',
            'place',
            'guest',
            'time_in',
            'time_out',
            'description',
            'main_image',
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
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True, }),
        required=False,
        label="Дополнительные фото",
        help_text="<-  Выберите несколько файлов",
    )
