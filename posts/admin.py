from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "last_updated", "timestamp", "id"]
    list_display_links = ["last_updated"]
    list_filter = ["title", "last_updated", "timestamp"]
    search_fields = ["title", "content"]
    list_editable = ["title"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
