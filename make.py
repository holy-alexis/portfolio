import sys
import os

if 'win' in sys.platform:
    os.system('python manage.py migrate')
    os.system('python manage.py loaddata dumps/towns.json')
    os.system('python manage.py loaddata dumps/people.json')
else:
    os.system('python3 manage.py migrate')
    os.system('python3 manage.py loaddata dumps/towns.json')
    os.system('python3 manage.py loaddata dumps/people.json')
