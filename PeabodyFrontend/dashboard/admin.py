from django.contrib import admin

# Register your models here. Username: test. Password: foobar123
from .models import Entry

admin.site.register(Entry)
