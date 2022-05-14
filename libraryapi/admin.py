from django.contrib import admin
from .models import book
# Register your models here.

@admin.register(book)
class libraryadmin(admin.ModelAdmin):
    list_display=['id' , 'nameofbook' ,'statusofbook', 'rollnoburrower']