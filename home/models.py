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


class AboutTextBlock(Orderable):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='about_texts')
    text = RichTextField(verbose_name='Текст')

    panels = [FieldPanel('text')]


class HomePage(Page):
    
    hero_title = models.CharField(max_length=200, verbose_name='Заголовок Hero', default='', blank=True)
    hero_subtitle = models.CharField(max_length=300, blank=True, verbose_name='Підзаголовок Hero')
    hero_bg = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
        verbose_name='Фон Hero'
    )

    
    about_title = models.CharField(max_length=200, verbose_name='Заголовок "Про нас"', default='', blank=True)
    about_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+',
        verbose_name='Фото "Про нас"'
    )

    
    achievements_title = models.CharField(max_length=200, verbose_name='Заголовок досягнень', default='', blank=True)

    
    contact_address = models.CharField(max_length=300, verbose_name='Адреса', default='', blank=True)
    contact_phone = models.CharField(max_length=50, verbose_name='Телефон', default='', blank=True)
    contact_email = models.EmailField(verbose_name='Email', default='', blank=True)
    location_subtitle = models.CharField(max_length=200, verbose_name='Підзаголовок адреси', default='', blank=True)
    contact_section_title = models.CharField(max_length=200, verbose_name='Заголовок секції контактів', default='', blank=True)
    contact_btn_text = models.CharField(max_length=100, verbose_name='Текст кнопки запису', default='', blank=True)

    
    footer_title = models.CharField(max_length=200, verbose_name='Заголовок футера', default='', blank=True)
    footer_text = RichTextField(verbose_name='Текст футера', default='', blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
            FieldPanel('hero_bg'),
        ], heading='🥋 Hero секція'),

        MultiFieldPanel([
            FieldPanel('about_title'),
            InlinePanel('about_texts', label='Блок тексту'),
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
            FieldPanel('footer_title'),
            FieldPanel('footer_text'),
        ], heading='📄 Футер'),
    ]