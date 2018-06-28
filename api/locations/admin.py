from django.contrib import admin

from locations.models import City, Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'zone', 'created_at', 'updated_at')
    list_editable = ('name', 'zone')
    list_filter = ('zone',)

    readonly_fields = ('created_at', 'updated_at')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'created_at', 'updated_at')
    list_editable = ('name', 'country')
    list_filter = ('country', 'country__zone')
    search_fields = ('country',)
    # autocomplete_fields = ('country',)
