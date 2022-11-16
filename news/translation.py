from modeltranslation.translator import translator, TranslationOptions, register
from .models import News


# @register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description1', 'description2', 'description3', 'description4', 'description5')


translator.register(News, NewsTranslationOptions)