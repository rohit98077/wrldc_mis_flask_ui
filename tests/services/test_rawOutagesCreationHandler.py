import unittest
from src.services.rawOutagesCreationHandler import RawOutagesCreationHandler
import datetime as dt
from src.appConfig import getConfig


class TestCreateRawOutagesService(unittest.TestCase):
    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that creates raw outages data using it's api service
        """
        startDate = dt.datetime.now()
        endDate = startDate

        outagesCreator = RawOutagesCreationHandler(
            self.appConfig['rawOutagesCreationServiceUrl'])
        resp = outagesCreator.createRawOutages(startDate, endDate)
        self.assertTrue(resp['isSuccess'])
        self.assertTrue(resp['status'] == 200)
        self.assertTrue('message' in resp)
