import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
try:
    u = User.objects.get(username='admin')
    u.set_password('admin123')
    u.save()
    print('✓ Admin password set to: admin123')
except User.DoesNotExist:
    print('✗ Admin user not found')
