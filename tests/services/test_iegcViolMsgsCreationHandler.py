import unittest
from src.services.iegcViolMsgsHandler import IegcViolMsgsCreationHandler
import datetime as dt
from src.appConfig import getConfig
import os


class TestCreateIegcViolMsgsService(unittest.TestCase):
    def setUp(self):
        self.appConfig = getConfig()

    def test_run(self) -> None:
        """tests the function that creates iegc violation messages using it's api service
        """
        iegcViolMsgsCreator = IegcViolMsgsCreationHandler(
            self.appConfig['iegcViolMsgsCreationServiceUrl'])
        resp = iegcViolMsgsCreator.createIegcViolMsgs(
            open(os.path.join('input_data', 'Violation.xlsx')))
        self.assertTrue(resp['isSuccess'])
        self.assertTrue(resp['status'] == 200)
        self.assertTrue('message' in resp)
