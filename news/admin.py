from django.contrib import admin
from .models import Editor, Article, tags

# Register your models here.

class ArticleAdmiin(admin.ModelAdmin):
    filter_horizonttal = ('tag',)

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)


