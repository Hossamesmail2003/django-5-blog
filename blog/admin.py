from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post,Comment

# Register your models here.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display =['title','draft','author']
    list_filter = ['draft','author']
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)