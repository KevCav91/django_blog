from django.contrib import admin
from blogging.models import Post
from blogging.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    exclude = ('posts',)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    fields = ('title', 'text', 'author', 'published_date')
    list_display = ('title', 'author', 'created_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
