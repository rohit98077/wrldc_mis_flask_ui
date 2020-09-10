import unittest
from src.services.derFreqCreationHandler import DerivedFrequencyCreationHandler
import datetime as dt
from src.appConfig import getConfig


class TestCreateDerFreqService(unittest.TestCase):
    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that creates derived freq using it's api service
        """
        startDate = dt.datetime.now() - dt.timedelta(days=1)
        endDate = startDate

        derFreqCreator = DerivedFrequencyCreationHandler(
            self.appConfig['derivedFrequencyCreationServiceUrl'])
        resp = derFreqCreator.createDerivedFrequency(startDate, endDate)
        self.assertTrue(resp['isSuccess'])
        self.assertTrue(resp['status'] == 200)
        self.assertTrue('message' in resp)
