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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['country__name', 'name']
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
