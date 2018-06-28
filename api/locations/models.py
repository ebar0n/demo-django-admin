from django.db import models


class Country(models.Model):
    AMER = 'AMER'
    EMEA = 'EMEA'
    APAC = 'APAC'

    name = models.CharField(max_length=30)
    zone = models.CharField(
        max_length=4, default=EMEA, choices=(
            (AMER, 'AMER'),
            (EMEA, 'EMEA'),
            (APAC, 'APAC'),
        )
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
