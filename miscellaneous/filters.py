from rest_framework import filters
from miscellaneous.models import Matches


__author__ = 'Mushahid'



class MatchFilterByName(filters.FilterSet):
    """
        Based on the user_id male measurement retrieve
    """
    class Meta:
        model = Matches
        fields = ('name',)