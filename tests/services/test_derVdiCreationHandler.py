import unittest
from src.services.derVdiCreationHandler import DerivedVdiCreationHandler
import datetime as dt
from src.appConfig import getConfig


class TestCreateDerVdiService(unittest.TestCase):
    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that creates derived weekly VDI using it's api service
        """
        startDate = dt.datetime.now() - dt.timedelta(days=8)
        endDate = startDate

        derVdiCreator = DerivedVdiCreationHandler(
            self.appConfig['derivedVdiCreationServiceUrl'])
        resp = derVdiCreator.createDerivedVdi(startDate, endDate)
        self.assertTrue(resp['isSuccess'])
        self.assertTrue(resp['status'] == 200)
        self.assertTrue('message' in resp)
