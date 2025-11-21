"""
Celery Configuration für lorchPro
"""

import os
from celery import Celery

# Django Settings Modul setzen
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.development')

# Celery App erstellen
app = Celery('lorchpro')

# Konfiguration aus Django Settings laden
app.config_from_object('django.conf:settings', namespace='CELERY')

# Tasks automatisch aus allen Apps laden
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Debug-Task für Testing"""
    print(f'Request: {self.request!r}')

