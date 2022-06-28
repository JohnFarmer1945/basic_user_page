from django.contrib import admin
#from blog.models import Taucher, Einsatz
from blog.models import Publication, Article


class PublicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Publication, PublicationAdmin)


class ArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article, ArticleAdmin)
