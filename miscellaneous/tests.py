__author__ = 'Mushahid'

import unittest
import datetime
from miscellaneous.models import Matches, Market, Sport


class MatchTesting(unittest.TestCase):
    """
        Add the unit test to check match object creating wtih all attribute.
    """

    def test_match(self):
        start_time = datetime.datetime.now()
        market = Market.objects.create(name="New Event")
        sport = Sport.objects.create(name="Football", market=market)
        match_one = Matches.objects.create(start_time=start_time, name="Football Cup", sport=sport)

        self.assertEqual(Market.objects.count(), 1)
        self.assertEqual(Sport.objects.count(), 1)
        self.assertEqual(Matches.objects.count(), 1)


if __name__ == '__main__':
    unittest.main()

