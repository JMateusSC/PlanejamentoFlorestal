from django.db import models
from django.contrib.auth.models import User

from lands.models import Land

class AnalysisRequest(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=10,
        choices=(
            ('DENIED', 'Recusado'),
            ('QUEUED', 'Na fila'),
            ('STARTED', 'Iniciado'),
            ('PAUSED', 'Pausado'),
            ('FINISHED', 'Finalizado'),
            ('ERROR', 'Erro'),
            ('CANCELLED', 'Cancelado')
        ),
        default='QUEUED'
    )
    process_message = models.TextField()
    request_date = models.DateField()
    finish_date = models.DateField()

class AnalysisResult(models.Model):
    id = models.AutoField(primary_key=True)
    request = models.OneToOneField(AnalysisRequest, on_delete=models.DO_NOTHING)
    report = models.FileField()
    start_date = models.DateField()
    end_date = models.DateField()
    ellapsed_time = models.BigIntegerField()
