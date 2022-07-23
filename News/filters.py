from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post
        field = {
            'title_post': ['icontains'],
            'type_post': ['icontains'],
            'date_creation':['gt'],
        }