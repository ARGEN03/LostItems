from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# установите модуль настроек Django по умолчанию для программы 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# создайте экземпляр Celery и настройте его, используя настройки из Django.
app = Celery('config')

# namespace='CELERY' означает, что все ключи конфигурации, связанные с Celery, должны иметь префикс 'CELERY_'.
app.config_from_object('django.conf:settings', namespace='CELERY')

# загрузите модули задач из всех зарегистрированных конфигураций приложений Django.
app.autodiscover_tasks()