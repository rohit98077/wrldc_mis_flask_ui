import unittest
from src.services.rawPairAnglesCreationHandler import RawPairAnglesCreationHandler
import datetime as dt
from src.appConfig import getConfig


class TestCreateRawPairAnglesService(unittest.TestCase):
    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that creates raw pair angles data using it's api service
        """
        startDate = dt.datetime.now() - dt.timedelta(days=1)
        endDate = startDate

        pairAnglesCreator = RawPairAnglesCreationHandler(
            self.appConfig['rawPairAnglesCreationServiceUrl'])
        resp = pairAnglesCreator.createRawPairAngles(startDate, endDate)
        self.assertTrue(resp['isSuccess'])
        self.assertTrue(resp['status'] == 200)
        self.assertTrue('message' in resp)
