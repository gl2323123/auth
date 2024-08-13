import django_filters

from advertisements.models import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    """Фильтры для объявлений."""
    creator = django_filters.ModelMultipleChoiceFilter(to_field_name='creator_id', queryset=Advertisement.objects.all())
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'status']
