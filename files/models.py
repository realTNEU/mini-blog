from django.db import models
from django.conf import settings
from io import BytesIO
import os
import pandas as pd
import json

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
    excel_data = models.JSONField(null=True, blank=True, help_text='Stores Excel data preview as JSON')
    excel_columns_list = models.JSONField(null=True, blank=True, help_text='Stores column names')
    
    class Meta:
        ordering = ['-upload_date']
    
    def __str__(self):
        return self.file_name
    
    def get_excel_preview(self, max_rows=10):
        """Get a preview of the first N rows of the Excel file"""
        if not self.excel_data:
            return None
        try:
            data = json.loads(self.excel_data) if isinstance(self.excel_data, str) else self.excel_data
            return {
                'columns': data.get('columns', []),
                'rows': data.get('rows', [])[:max_rows],
                'total_rows': data.get('total_rows', 0),
                'total_columns': data.get('total_columns', 0)
            }
        except (json.JSONDecodeError, TypeError):
            return None
    
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
            
            # Analyze Excel/CSV files without consuming the upload stream
            if self.file_type in ['excel', 'csv']:
                try:
                    # Read the entire file into memory
                    self.file.seek(0)
                    file_bytes = self.file.read()
                    buffer = BytesIO(file_bytes)
                    
                    # Read with appropriate engine
                    if self.file_type == 'excel':
                        if ext == '.xlsx':
                            df = pd.read_excel(buffer, engine='openpyxl')
                        else:  # .xls
                            df = pd.read_excel(buffer, engine='xlrd')
                    else:  # csv
                        df = pd.read_csv(buffer)
                    
                    self.excel_rows = len(df)
                    self.excel_columns = len(df.columns)
                    self.excel_columns_list = df.columns.tolist()
                    
                    # Store preview data as JSON (convert NaN to None for JSON serialization)
                    preview_rows = df.head(10).replace({pd.NA: None, pd.NaT: None}).fillna('').values.tolist()
                    
                    preview_data = {
                        'columns': df.columns.tolist(),
                        'rows': preview_rows,
                        'total_rows': len(df),
                        'total_columns': len(df.columns)
                    }
                    self.excel_data = json.dumps(preview_data)
                    
                    # Reset file pointer for saving
                    self.file.seek(0)
                except Exception as e:
                    print(f"Error processing file: {e}")
                    import traceback
                    traceback.print_exc()
                finally:
                    # Ensure file pointer is at the beginning for saving
                    try:
                        self.file.seek(0)
                    except:
                        pass
        
        super().save(*args, **kwargs)

