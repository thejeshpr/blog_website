from django.contrib import admin

from .models import Article,  Profile, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', 'slug')
admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_at')
    list_filter = ('active', )
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ('name', 'slug')    
admin.site.register(Category, CategoryAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'active', 'created_at')
    list_filter = ('active', )
    # prepopulated_fields = {'slug': ('user', )}
    search_fields = ('user', 'slug')    
admin.site.register(Profile, ProfileAdmin)
