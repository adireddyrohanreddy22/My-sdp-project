import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendence_site.settings')
import django
django.setup()
from django.test import Client
c = Client()
paths = ['/', '/attendance/students/', '/attendance/mark/', '/attendance/records/']
for p in paths:
    r = c.get(p)
    print(p, r.status_code)
    if r.status_code != 200:
        print('Location header:', r.get('Location'))
        print('Response snippet:', r.content[:400])
