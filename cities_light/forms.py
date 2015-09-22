from __future__ import unicode_literals

from django import forms

from .loading import get_cities_models

Country, Region, City, Commune = get_cities_models()

__all__ = ['CountryForm', 'RegionForm', 'CityForm', 'CommuneForm']


class CountryForm(forms.ModelForm):
    """
    Country model form.
    """
    class Meta:
        model = Country
        exclude = ('name_ascii', 'slug', 'geoname_id')


class RegionForm(forms.ModelForm):
    """
    Region model form.
    """
    class Meta:
        model = Region
        exclude = ('name_ascii', 'slug', 'geoname_id', 'display_name',
                   'geoname_code')


class CityForm(forms.ModelForm):
    """
    City model form.
    """
    class Meta:
        model = City
        exclude = ('name_ascii', 'search_names', 'slug', 'geoname_id',
                   'display_name', 'feature_code')


class CommuneForm(forms.ModelForm):
    """
    Commune model form.
    """
    class Meta:
        model = Commune
        exclude = ('name_ascii', 'search_names', 'slug', 'geoname_id',
                   'display_name', 'feature_code')
