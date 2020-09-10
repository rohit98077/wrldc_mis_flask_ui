import unittest
from src.services.derVoltCreationHandler import DerivedVoltageCreationHandler
import datetime as dt
from src.appConfig import getConfig


class TestCreateDerVoltService(unittest.TestCase):
    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that creates derived voltage using it's api service
        """
        startDate = dt.datetime.now() - dt.timedelta(days=1)
        endDate = startDate

        derVoltCreator = DerivedVoltageCreationHandler(
            self.appConfig['derivedVoltageCreationServiceUrl'])
        resp = derVoltCreator.createDerivedVoltage(startDate, endDate)
        self.assertTrue(resp['isSuccess'])
        self.assertTrue(resp['status'] == 200)
        self.assertTrue('message' in resp)
