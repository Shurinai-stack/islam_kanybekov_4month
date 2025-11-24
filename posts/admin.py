from django.contrib import admin
from posts.models import Post,Categorys,Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author' , 'category', 'rate')
admin.site.register(Categorys)
admin.site.register(Tag)