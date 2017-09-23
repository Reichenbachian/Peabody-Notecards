from django.contrib import admin
from django.http import HttpResponse
# Register your models here. Username: test. Password: foobar123
from .models import Entry

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=db.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"catNumber"),
        smart_str(u"siteNumber"),
        smart_str(u"locality"),
        smart_str(u"site"),
        smart_str(u"name"),
        smart_str(u"situation"),
        smart_str(u"accNum"),
        smart_str(u"fileName"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.catNumber),
            smart_str(obj.siteNumber),
            smart_str(obj.locality),
            smart_str(obj.site),
            smart_str(obj.situation),
            smart_str(obj.accNum),
            smart_str(obj.fileName),
        ])
    return response
export_csv.short_description = u"Export CSV"


class EntryAdmin(admin.ModelAdmin):
    actions = [export_csv]

admin.site.register(Entry, EntryAdmin)
