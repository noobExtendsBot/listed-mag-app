from django.contrib import admin
from .models import Post, Categories, Comment
# Register your models here.


class AdminPost(admin.ModelAdmin):
	list_display = ('title', 'post_cat', 'author', 'created_at', 'updated_at')
	ordering = ('-updated_at',)
	list_filter = ('author', 'updated_at', 'post_cat')
	search_fields = ('title', 'content',)


class AdminCategories(admin.ModelAdmin):
	list_display = ('cat_name', 'thumbnail')
	search_fields = ('cat_name',)


class AdminComment(admin.ModelAdmin):
	list_display = ('text', 'post', 'author', 'create_date')
	ordering = ('-create_date',)
	search_fields = ('text', 'post', 'author')
	list_filter = ('post', 'create_date')


admin.site.site_header = "Listed Magazine Administration"
admin.site.register(Post, AdminPost)
admin.site.register(Categories, AdminCategories)
admin.site.register(Comment, AdminComment)


