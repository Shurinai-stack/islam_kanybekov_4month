from django.contrib import admin
from posts.models import Post,Categorys,Tag

admin.site.register(Post)
admin.site.register(Categorys)
admin.site.register(Tag)