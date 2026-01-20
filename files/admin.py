from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'file_type', 'file_size_display', 'excel_rows', 'excel_columns', 'uploader', 'upload_date')
    list_filter = ('file_type', 'upload_date')
    search_fields = ('file_name', 'uploader__username')
    date_hierarchy = 'upload_date'
    
    def file_size_display(self, obj):
        size = obj.file_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} TB"
    file_size_display.short_description = 'File Size'
