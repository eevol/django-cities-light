"""
Settings for this application. The most important is TRANSLATION_LANGUAGES
because it's probably project specific.

.. py:data:: TRANSLATION_LANGUAGES

    List of language codes. It is used to generate the alternate_names property
    of cities_light models. You want to keep it as small as possible.
    By default, it includes the most popular languages according to wikipedia,
    which use a rather ascii-compatible alphabet. It also contains 'abbr' which
    stands for 'abbreviation', you might want to include this one as well.

    See:

     - http://download.geonames.org/export/dump/iso-languagecodes.txt

    Example::

        CITIES_LIGHT_TRANSLATION_LANGUAGES = ['es', 'en', 'fr', 'abbr']

.. py:data:: INCLUDE_COUNTRIES

    List of country codes to include. It's None by default which lets all
    countries in the database. But if you only wanted French and Belgium
    countries/regions/cities, you could set it as such::

        CITIES_LIGHT_INCLUDE_COUNTRIES = ['FR', 'BE']

.. py:data:: COUNTRY_SOURCES

    A list of urls to download country info from. Default is countryInfo.txt
    from geonames download server. Overridable in
    ``settings.CITIES_LIGHT_COUNTRY_SOURCES``.

.. py:data:: REGION_SOURCES

    A list of urls to download region info from. Default is
    admin1CodesASCII.txt from geonames download server. Overridable in
    ``settings.CITIES_LIGHT_REGION_SOURCES``.

.. py:data:: CITY_SOURCES

    A list of urls to download city info from. Default is cities15000.zip from
    geonames download server. Overridable in
    ``settings.CITIES_LIGHT_CITY_SOURCES``.

.. py:data:: TRANSLATION_SOURCES

    A list of urls to download alternate names info from. Default is
    alternateNames.zip from geonames download server. Overridable in
    ``settings.CITIES_LIGHT_TRANSLATION_SOURCES``.

.. py:data:: SOURCES

    A list with all sources, auto-generated.

.. py:data:: DATA_DIR

    Absolute path to download and extract data into. Default is
    cities_light/data. Overridable in ``settings.CITIES_LIGHT_DATA_DIR``

.. py:data:: INDEX_SEARCH_NAMES

    If your database engine for cities_light supports indexing TextFields (ie.
    it is **not** MySQL), then this should be set to True. You might have to
    override this setting with ``settings.CITIES_LIGHT_INDEX_SEARCH_NAMES`` if
    using several databases for your project.

.. py:data:: CITIES_LIGHT_APP_NAME

    Modify it only if you want to define your custom cities models, that
    are inherited from abstract models of this package.
    It must be equal to app name, where custom models are defined.
    For example, if they are in geo/models.py, then set
    ``settings.CITIES_LIGHT_APP_NAME = 'geo'``.
    Note: you can't define one custom model, you have to define all of
    cities_light models, even if you want to modify only one.
"""
from __future__ import unicode_literals

import os.path

from django.conf import settings

__all__ = ['COUNTRY_SOURCES', 'REGION_SOURCES', 'CITY_SOURCES', 'COMMUNE_SOURCES',
    'TRANSLATION_LANGUAGES', 'TRANSLATION_SOURCES', 'SOURCES', 'DATA_DIR',
    'INDEX_SEARCH_NAMES', 'INCLUDE_COUNTRIES', 'DEFAULT_APP_NAME',
    'CITIES_LIGHT_APP_NAME', 'ICountry', 'IRegion', 'ICity', 'ICommune',
    'IAlternate']

COUNTRY_SOURCES = getattr(settings, 'CITIES_LIGHT_COUNTRY_SOURCES',
    ['http://download.geonames.org/export/dump/countryInfo.txt'])
REGION_SOURCES = getattr(settings, 'CITIES_LIGHT_REGION_SOURCES',
    ['http://download.geonames.org/export/dump/admin1CodesASCII.txt'])
COMMUNE_SOURCES = getattr(settings, 'CITIES_LIGHT_COMMUNE_SOURCES',
    ['http://download.geonames.org/export/dump/cities15000.zip'])
CITY_SOURCES = getattr(settings, 'CITIES_LIGHT_CITY_SOURCES',
    ['http://download.geonames.org/export/dump/cities15000.zip'])
TRANSLATION_SOURCES = getattr(settings, 'CITIES_LIGHT_TRANSLATION_SOURCES',
    ['http://download.geonames.org/export/dump/alternateNames.zip'])
TRANSLATION_LANGUAGES = getattr(settings, 'CITIES_LIGHT_TRANSLATION_LANGUAGES',
    ['es', 'en', 'pt', 'de', 'pl', 'abbr'])

SOURCES = list(COUNTRY_SOURCES) + list(REGION_SOURCES) + list(COMMUNE_SOURCES) + list(CITY_SOURCES)
SOURCES += TRANSLATION_SOURCES

DATA_DIR = getattr(settings, 'CITIES_LIGHT_DATA_DIR',
    os.path.normpath(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'data')))

INCLUDE_COUNTRIES = getattr(settings, 'CITIES_LIGHT_INCLUDE_COUNTRIES', None)

# MySQL doesn't support indexing TextFields
INDEX_SEARCH_NAMES = getattr(settings, 'CITIES_LIGHT_INDEX_SEARCH_NAMES', None)
if INDEX_SEARCH_NAMES is None:
    INDEX_SEARCH_NAMES = True
    for database in list(settings.DATABASES.values()):
        if 'mysql' in database['ENGINE'].lower():
            INDEX_SEARCH_NAMES = False

DEFAULT_APP_NAME = 'cities_light'
CITIES_LIGHT_APP_NAME = getattr(settings, 'CITIES_LIGHT_APP_NAME',
    DEFAULT_APP_NAME)


class ICountry:
    """
    Country field indexes in geonames.
    """
    code = 0
    code3 = 1
    codeNum = 2
    fips = 3
    name = 4
    capital = 5
    area = 6
    population = 7
    continent = 8
    tld = 9
    currencyCode = 10
    currencyName = 11
    phone = 12
    postalCodeFormat = 13
    postalCodeRegex = 14
    languages = 15
    geonameid = 16
    neighbours = 17
    equivalentFips = 18


class IRegion:
    """
    Region field indexes in geonames.
    """
    code = 0
    name = 1
    asciiName = 2
    geonameid = 3


class ICommune:
    """
    Commune field indexes in geonames.
    """
    geonameid = 0
    name = 1
    asciiName = 2
    alternateNames = 3
    latitude = 4
    longitude = 5
    featureClass = 6
    featureCode = 7
    countryCode = 8
    cc2 = 9
    admin1Code = 10
    admin2Code = 11
    admin3Code = 12
    admin4Code = 13
    population = 14
    elevation = 15
    gtopo30 = 16
    timezone = 17
    modificationDate = 18


class ICity:
    """
    City field indexes in geonames.
    Description of fields: http://download.geonames.org/export/dump/readme.txt
    """
    geonameid = 0
    name = 1
    asciiName = 2
    alternateNames = 3
    latitude = 4
    longitude = 5
    featureClass = 6
    featureCode = 7
    countryCode = 8
    cc2 = 9
    admin1Code = 10
    admin2Code = 11
    admin3Code = 12
    admin4Code = 13
    population = 14
    elevation = 15
    gtopo30 = 16
    timezone = 17
    modificationDate = 18


class IAlternate:
    """
    Alternate names field indexes in geonames.
    Description of fields: http://download.geonames.org/export/dump/readme.txt
    """
    nameid = 0
    geonameid = 1
    language = 2
    name = 3
    isPreferred = 4
    isShort = 5
    isColloquial = 6
    isHistoric = 7
