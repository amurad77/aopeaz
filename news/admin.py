from django.contrib import admin
from .models import News
from modeltranslation.translator import TranslationOptions, register
from modeltranslation.admin import TranslationAdmin
# Register your models here.
# @register(News)

class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'description1', 'created_at', 'updated_at')
    list_filter = ('description1', 'created_at', 'updated_at')
    search_fields = ('description1', 'created_at', 'updated_at')

    # class Media:
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js'
    #         'modeltranslation/js/tabbed_translation_fields.js'
    #     )
    #     css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css')
    #     }
admin.site.register (News, NewsAdmin)