from django.contrib import admin
from .models import Book, BookContributor, Publisher, Rack

# Register your models here.

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(BookContributor)
admin.site.register(Rack)
