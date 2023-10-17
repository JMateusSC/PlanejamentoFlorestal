from django.db import models
from django.contrib.auth.models import User

class Signature(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=10,
        choices=(
            ('TRIAL', 'Versão trial'),
            ('MONTHLY', 'Plano mensal'),
            ('ANUAL', 'Plano anual')
        ),
        default='QUEUED'
    )
    start_date = models.DateField()
    expiration_date = models.DateField()
    is_expired = models.BooleanField()
    