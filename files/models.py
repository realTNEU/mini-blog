from django.db import models
from django.conf import settings
import os
import pandas as pd

class UploadedFile(models.Model):
    FILE_TYPE_CHOICES = [
        ('excel', 'Excel'),
        ('csv', 'CSV'),
        ('pdf', 'PDF'),
        ('image', 'Image'),
        ('other', 'Other'),
    ]
    
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES)
    file_size = models.BigIntegerField(help_text='File size in bytes')
    upload_date = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uploaded_files')
    
    # Excel-specific fields
    excel_rows = models.IntegerField(null=True, blank=True)
    excel_columns = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['-upload_date']
    
    def __str__(self):
        return self.file_name
    
    def save(self, *args, **kwargs):
        if self.file:
            self.file_name = self.file.name
            self.file_size = self.file.size
            
            # Determine file type
            ext = os.path.splitext(self.file.name)[1].lower()
            if ext in ['.xlsx', '.xls']:
                self.file_type = 'excel'
            elif ext == '.csv':
                self.file_type = 'csv'
            elif ext == '.pdf':
                self.file_type = 'pdf'
            elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                self.file_type = 'image'
            else:
                self.file_type = 'other'
            
            # Analyze Excel files
            if self.file_type in ['excel', 'csv']:
                try:
                    if self.file_type == 'excel':
                        df = pd.read_excel(self.file)
                    else:
                        df = pd.read_csv(self.file)
                    self.excel_rows = len(df)
                    self.excel_columns = len(df.columns)
                except Exception:
                    pass
        
        super().save(*args, **kwargs)
