from django.db import models

# Create your models here.

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

TASK_TYPE = (
    ('I', 'Income'),
    ('O', 'Outcome'),
)

class MoneyFlowRecord(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    task_type = models.CharField(max_length=1, choices=TASK_TYPE)
    
    class Meta:
        ordering = ('created',)