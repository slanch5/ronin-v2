from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from modelcluster.fields import ParentalKey


class GalleryImage(Orderable):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name='Фото'
    )
    panels = [FieldPanel('image')]


class HomePage(Page):
    # HERO секція
    hero_title = models.CharField(max_length=200, verbose_name='Заголовок Hero', default='', blank=True)
    hero_subtitle = models.CharField(max_length=300, blank=True, verbose_name='Підзаголовок Hero')
    hero_bg = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
        verbose_name='Фон Hero'
    )

    # ABOUT US секція
    about_title = models.CharField(max_length=200, verbose_name='Заголовок "Про нас"', default='', blank=True)
    about_text_1 = RichTextField(verbose_name='Текст "Про нас" 1', default='', blank=True)
    about_text_2 = RichTextField(verbose_name='Текст "Про нас" 2', default='', blank=True)
    about_text_3 = RichTextField(verbose_name='Текст "Про нас" 3', default='', blank=True)
    about_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
        verbose_name='Фото "Про нас"'
    )

    # ДОСЯГНЕННЯ секція
    achievements_title = models.CharField(max_length=200, verbose_name='Заголовок досягнень', default='', blank=True)

    # КОНТАКТИ секція
    contact_address = models.CharField(max_length=300, verbose_name='Адреса', default='', blank=True)
    contact_phone = models.CharField(max_length=50, verbose_name='Телефон', default='', blank=True)
    contact_email = models.EmailField(verbose_name='Email', default='', blank=True)
    location_subtitle = models.CharField(max_length=200, verbose_name='Підзаголовок адреси', default='', blank=True)
    contact_section_title = models.CharField(max_length=200, verbose_name='Заголовок секції контактів', default='', blank=True)
    contact_btn_text = models.CharField(max_length=100, verbose_name='Текст кнопки запису', default='', blank=True)

    # ФУТЕР
    footer_text = RichTextField(verbose_name='Текст футера', default='', blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
            FieldPanel('hero_bg'),
        ], heading='🥋 Hero секція'),

        MultiFieldPanel([
            FieldPanel('about_title'),
            FieldPanel('about_text_1'),
            FieldPanel('about_text_2'),
            FieldPanel('about_text_3'),
            FieldPanel('about_image'),
        ], heading='📖 Про нас'),

        MultiFieldPanel([
            FieldPanel('achievements_title'),
            InlinePanel('gallery_images', label='Фото галереї'),
        ], heading='🏆 Досягнення клубу'),

        MultiFieldPanel([
            FieldPanel('contact_address'),
            FieldPanel('contact_phone'),
            FieldPanel('contact_email'),
            FieldPanel('contact_section_title'),
            FieldPanel('contact_btn_text'),
            FieldPanel('location_subtitle'),
        ], heading='📞 Контакти'),

        MultiFieldPanel([
            FieldPanel('footer_text'),
        ], heading='📄 Футер'),
    ]