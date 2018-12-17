from django.db import models


class Market(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'miscellaneous'

    def __str__(self):
        return self.name


class Sport(models.Model):
    """
        Sport Details will be shared in market where user can start bidding.
    """
    name = models.CharField(max_length=50)
    market = models.OneToOneField(Market, on_delete=models.PROTECT)

    class Meta:
        app_label = 'miscellaneous'

    def __str__(self):
        return self.name


class Matches(models.Model):
    """
        Match details with sport name.
    """
    id = models.IntegerField(primary_key=True)
    sport = models.ForeignKey(Sport, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()

    class Meta:
        app_label = 'miscellaneous'

    def __str__(self):
        return self.name


class Selection(models.Model):
    """
        Multiple Selection as bidding can be for one match.
    """
    id = models.IntegerField(primary_key=True)
    matches = models.ForeignKey(Matches, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    odds = models.FloatField()

    class Meta:
        app_label = 'miscellaneous'

    def __str__(self):
        return self.name
