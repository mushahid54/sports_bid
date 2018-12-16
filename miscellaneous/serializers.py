
from rest_framework.response import Response
from miscellaneous.models import Matches, Sport, Market, Selection

__author__ = 'MushahidKhan'

from rest_framework import serializers, status


class SelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ('id', 'name', 'odds')



class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = ('id', 'name')



class MarketCreateSelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ('id', 'name', 'odds')


class MarketSerializer(serializers.ModelSerializer):
    selections = MarketCreateSelectionSerializer(many=True)

    class Meta:
        model = Market
        fields = ('id', 'name', 'selections')

    def get_selection(self, market):
        queryset = market.match.selection_set.all()
        return SelectionSerializer(queryset,many=True).data




class MatchSerializer(serializers.ModelSerializer):
    sport  = SportSerializer()
    markets = serializers.SerializerMethodField()

    class Meta:
        model = Matches
        fields = ('id', 'name', 'start_time', 'sport', 'markets' )

    def get_markets(self, match):
        markets = match.sport.market
        markets.match = match
        return MarketSerializer(markets).data


class MatchCreateDataSerializer(serializers.ModelSerializer):
    sport  = SportSerializer()
    markets = MarketSerializer(many=True)

    class Meta:
        model = Matches
        fields = ('id', 'name', 'start_time', 'sport', 'markets')


class MatchKeywordSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Matches
        fields = ('id', 'name', 'start_time', 'url' )

    def get_url(self, match):
        return "http://example.com/api/match/"+str(match.id)



class MatchCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    event = MatchCreateDataSerializer(required=False)
    message_type = serializers.CharField(required=False)

    class Meta:
        model = Matches
        fields = ('id', 'message_type', 'event' )


    def create(self, validated_data):
        event = validated_data.get('event', None)
        market_name = validated_data.get('message_type', None)
        id = validated_data.get('id', None)
        if event:
            market = Market.objects.create(name = market_name, id=id)
            sport_obj = Sport.objects.create(name=event['sport']['name'], market=market)
            markets = event.get('markets', None)
            match_dictionary = {
                                "name":event['name'], "start_time": event['start_time'],
                                "id": event['id'], "sport":sport_obj
                                }
            match_object = Matches.objects.create(**match_dictionary)
            if markets:
                for element in markets:
                    for selection in element['selections']:
                        selections = Selection.objects.create(id=selection['id'], matches=match_object, name=selection['name'],
                                                          odds=selection['odds'])

        return Response(status=status.HTTP_200_OK)


class MatchUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    event = MatchCreateDataSerializer(required=False)
    message_type = serializers.CharField(required=False)

    class Meta:
        model = Matches
        fields = ('id', 'message_type', 'event' )


    def update(self, instance, validated_data):
        event = validated_data.get('event', None)
        market_name = validated_data.get('message_type', None)
        id = validated_data.get('id', None)
        if event:
            market = Market.objects.create(name = market_name, id=id)
            sport_obj = Sport.objects.create(name=event['sport']['name'], market=market)
            markets = event.get('markets', None)
            match_dictionary = {
                                "name":event['name'], "start_time": event['start_time'],
                                "id": event['id'], "sport":sport_obj
                                }
            match_object = Matches.objects.create(**match_dictionary)
            if markets:
                for element in markets:
                    for selection in element['selections']:
                        selections = Selection.objects.create(id=selection['id'], matches=match_object, name=selection['name'],
                                                          odds=selection['odds'])

        return Response(status=status.HTTP_200_OK)