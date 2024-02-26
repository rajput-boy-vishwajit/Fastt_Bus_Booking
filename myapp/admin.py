from django.contrib import admin
from .models import Bus, User, Book

# Register your models here.
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_name','source', 'dest')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('bus_name', 'name', 'date')

