from django.core.management.base import BaseCommand
from files.models import UploadedFile
from io import BytesIO
import pandas as pd
import json


class Command(BaseCommand):
    help = 'Reprocess existing Excel/CSV files to extract rows, columns, and data preview'

    def handle(self, *args, **options):
        files = UploadedFile.objects.filter(file_type__in=['excel', 'csv'])
        
        total = files.count()
        processed = 0
        errors = 0
        
        self.stdout.write(f'Found {total} Excel/CSV files to process...\n')
        
        for file_obj in files:
            try:
                # Open the file
                with file_obj.file.open('rb') as f:
                    file_bytes = f.read()
                    buffer = BytesIO(file_bytes)
                    
                    # Read with appropriate method
                    if file_obj.file_type == 'excel':
                        ext = file_obj.file_name.lower().split('.')[-1]
                        if ext == 'xlsx':
                            df = pd.read_excel(buffer, engine='openpyxl')
                        else:  # xls
                            df = pd.read_excel(buffer, engine='xlrd')
                    else:  # csv
                        df = pd.read_csv(buffer)
                    
                    # Update fields
                    file_obj.excel_rows = len(df)
                    file_obj.excel_columns = len(df.columns)
                    file_obj.excel_columns_list = df.columns.tolist()
                    
                    # Store preview data as JSON
                    preview_rows = df.head(10).replace({pd.NA: None, pd.NaT: None}).fillna('').values.tolist()
                    
                    preview_data = {
                        'columns': df.columns.tolist(),
                        'rows': preview_rows,
                        'total_rows': len(df),
                        'total_columns': len(df.columns)
                    }
                    file_obj.excel_data = json.dumps(preview_data)
                    
                    # Save without triggering the save method again
                    UploadedFile.objects.filter(pk=file_obj.pk).update(
                        excel_rows=file_obj.excel_rows,
                        excel_columns=file_obj.excel_columns,
                        excel_columns_list=file_obj.excel_columns_list,
                        excel_data=file_obj.excel_data
                    )
                    
                    processed += 1
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ Processed: {file_obj.file_name} ({file_obj.excel_rows} rows, {file_obj.excel_columns} cols)')
                    )
                    
            except Exception as e:
                errors += 1
                self.stdout.write(
                    self.style.ERROR(f'✗ Error processing {file_obj.file_name}: {str(e)}')
                )
        
        self.stdout.write('\n' + '='*50)
        self.stdout.write(self.style.SUCCESS(f'\nProcessed: {processed}/{total}'))
        if errors > 0:
            self.stdout.write(self.style.ERROR(f'Errors: {errors}'))
        self.stdout.write('\n')
