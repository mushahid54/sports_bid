from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from rest_framework import viewsets, generics, status, mixins
from rest_framework.viewsets import GenericViewSet

from miscellaneous.filters import MatchFilterByName

from miscellaneous.models import Matches
from rest_framework.response import Response
from miscellaneous.serializers import  MatchSerializer, MatchKeywordSerializer, MatchCreateSerializer


class MatchViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,

                   GenericViewSet):

    queryset = Matches.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MatchFilterByName

    def get_serializer_class(self):
        name = self.request.query_params.get('name', None)
        if name:
            return MatchKeywordSerializer

        elif self.request.method == "POST":
            return MatchCreateSerializer

        elif self.request.method == "PATCH":
            return None

        else:
            return MatchSerializer


        # if len(self.request.path.split('/')) == 7:
        #     return Matches.objects.filter(sport__name__iexact=self.request.path.split('/')[5])
        # else:
        #     return super(MatchViewSet, self).get_queryset()
