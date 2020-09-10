import unittest
from src.services.rawVoltCreationHandler import RawVoltageCreationHandler
import datetime as dt
from src.appConfig import getConfig


class TestCreateRawVoltService(unittest.TestCase):
    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that creates raw voltage using it's api service
        """
        startDate = dt.datetime.now() - dt.timedelta(days=1)
        endDate = startDate

        rawVoltCreator = RawVoltageCreationHandler(
            self.appConfig['rawVoltageCreationServiceUrl'])
        resp = rawVoltCreator.createRawVoltage(startDate, endDate)
        self.assertTrue(resp['isSuccess'])
        self.assertTrue(resp['status'] == 200)
        self.assertTrue('message' in resp)
