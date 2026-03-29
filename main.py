# начальный скрипт для запуска
import os
from django.core.management import call_command
import django
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.config.settings')

django.setup()
def init():
    try:
        call_command('migrate', interactive=False)
    except Exception as e:
        print("Ошибка миграции:", e)

init()