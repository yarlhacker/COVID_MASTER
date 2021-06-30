from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):

    list_display = ('titre', 'images_view', 'date_add', 'date_update', 'status')
    list_editable = ('status',)

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')

    images_view.short_description = 'Aperçu des images'



@admin.register(models.Protect)
class ProtectAdmin(admin.ModelAdmin):

    list_display = ( 'images_view', 'date_add', 'date_update', 'status')
    list_editable = ('status',)

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')

    images_view.short_description = 'Aperçu des images'



@admin.register(models.Optionprotect)
class OptionprotectAdmin(admin.ModelAdmin):

    list_display = ( 'nom', 'date_add', 'date_update', 'status')
    list_editable = ('status',)


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):

    list_display = ('titre', 'images_view', 'date_add', 'date_update', 'status')
    list_editable = ('status',)

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')

    images_view.short_description = 'Aperçu des images'


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = ('titre', 'images_view','lien','date_add', 'date_update', 'status')
    list_editable = ('status',)

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')

    images_view.short_description = 'Aperçu des images'


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):

    list_display = ('titre', 'images_view','date_add', 'date_update', 'status')
    list_editable = ('status',)

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')

    images_view.short_description = 'Aperçu des images'


@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('email','date_add', 'date_update', 'status')
    list_editable = ('status',)


@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):

    list_display = ('date_add', 'date_update', 'status')
    list_editable = ('status',)


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):

    list_display = ('date_add', 'date_update', 'status')
    list_editable = ('status',)


# Register your models here.
