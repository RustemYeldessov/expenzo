from dataclasses import fields

from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_user_section')
        ]
        verbose_name_plural = "Sections"

    def __str__(self):
        return self.name
