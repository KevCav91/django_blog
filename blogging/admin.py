from django.contrib import admin
from blogging.models import Post
from blogging.models import Category

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
