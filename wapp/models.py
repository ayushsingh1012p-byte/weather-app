from django.db import models


class HotPlace(models.Model):
    city = models.CharField(max_length=100, unique=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city