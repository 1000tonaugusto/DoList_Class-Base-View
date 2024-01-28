from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Titulo')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False, verbose_name='Data de entrega')
    finished_at = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ['deadline']
