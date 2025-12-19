from django.test import Client
c=Client()
paths=['/','/attendance/students/','/attendance/mark/','/attendance/records/']
for p in paths:
    r=c.get(p)
    print(p, r.status_code)
    if r.status_code!=200:
        print('Location:', r.get('Location'))
