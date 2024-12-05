from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type_primary = models.CharField(max_length=50)
    type_secondary = models.CharField(max_length=50, blank=True, null=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
