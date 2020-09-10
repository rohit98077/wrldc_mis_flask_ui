import unittest
from src.services.rawFreqCreationHandler import RawFrequencyCreationHandler
import datetime as dt
from src.appConfig import getConfig


class TestCreateRawFreqService(unittest.TestCase):
    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that creates raw freq using it's api service
        """
        startDate = dt.datetime.now() - dt.timedelta(days=1)
        endDate = startDate

        rawFreqCreator = RawFrequencyCreationHandler(
            self.appConfig['rawFrequencyCreationServiceUrl'])
        resp = rawFreqCreator.createRawFrequency(startDate, endDate)
        self.assertTrue(resp['isSuccess'])
        self.assertTrue(resp['status'] == 200)
        self.assertTrue('message' in resp)
