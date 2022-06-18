from django.db import models


class dojos(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    desc = models.TextField(max_length=45)

class ninjas(models.Model):
    dojo_id = models.ForeignKey(dojos, blank=True, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
