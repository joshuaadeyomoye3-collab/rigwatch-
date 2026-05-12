from django.db import models

class Well(models.Model):
    STATUS_CHOICES = [
        ('NORMAL',       'Normal'),
        ('LOW',          'Low Pressure'),
        ('CRITICAL',     'Critical'),
        ('OVERPRESSURE', 'Overpressure'),
        ('OFFLINE',      'Offline'),
    ]

    name         = models.CharField(max_length=50, unique=True)
    pressure     = models.IntegerField()
    temp         = models.FloatField()
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NORMAL')
    active       = models.BooleanField(default=True)
    engineer     = models.CharField(max_length=100, blank=True, null=True)
    location     = models.CharField(max_length=100, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} — {self.status}'

    class Meta:
        ordering = ['name']