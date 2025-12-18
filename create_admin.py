import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopkart.settings')
django.setup()

from account.models import User

email = 'admin@gmail.com'
password = 'password123'
contact = '1234567890'

if not User.objects.filter(email=email).exists():
    print(f"Creating user {email}...")
    User.objects.create_superuser(email=email, contact_number=contact, password=password, first_name='Admin', last_name='User')
    print(f"Superuser created.\nEmail: {email}\nPassword: {password}")
else:
    print(f"User {email} already exists.\nPassword: {password} (if not changed)")
