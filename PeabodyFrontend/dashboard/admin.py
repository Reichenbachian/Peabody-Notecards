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
        smart_str(u"Catalog Number"),
        smart_str(u"Accession Number"),
        smart_str(u"Name"),
        smart_str(u"Site"),
        smart_str(u"Site Number"),
        smart_str(u"Locality"),
        smart_str(u"Situation"),
        smart_str(u"Image"),
        smart_str(u"Created At"),
        smart_str(u"Updated At"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.catNumber),
            smart_str(obj.accNum),
            smart_str(obj.name),
            smart_str(obj.site),
            smart_str(obj.siteNumber),
            smart_str(obj.locality),
            smart_str(obj.situation),
            smart_str(obj.fileName),
            smart_str(obj.created_at),
            smart_str(obj.updated_at),
        ])
    return response
export_csv.short_description = u"Export CSV"


class EntryAdmin(admin.ModelAdmin):
    actions = [export_csv]
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Entry, EntryAdmin)
