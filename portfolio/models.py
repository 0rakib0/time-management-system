from django.db import models

# Create your models here.

class Skill(models.Model):
    skill_name = models.CharField(max_length=120)
    skill_icon = models.CharField(max_length=120)
    create_att = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.skill_name