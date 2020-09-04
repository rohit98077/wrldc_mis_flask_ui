import requests
import datetime as dt
from src.typeDefs.rawPairAnglesCreationResp import RawPairAnglesCreationResp


class RawPairAnglesCreationHandler():
    rawPairAnglesCreationUrl = ''

    def __init__(self, rawPairAnglesCreationUrl):
        self.rawPairAnglesCreationUrl = rawPairAnglesCreationUrl

    def createRawPairAngles(self, startDate: dt.datetime, endDate: dt.datetime) -> RawPairAnglesCreationResp:
        """create raw pair angles using the api service

        Args:
            startDate (dt.datetime): start date
            endDate (dt.datetime): end date

        Returns:
            RawPairAnglesCreationResp: Result of the raw pair angles creation operation
        """
        createRawPairAnglesPayload = {
            "startDate": dt.datetime.strftime(startDate, '%Y-%m-%d'),
            "endDate": dt.datetime.strftime(endDate, '%Y-%m-%d')
        }
        res = requests.post(self.rawPairAnglesCreationUrl,
                            json=createRawPairAnglesPayload)

        operationResult: RawPairAnglesCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create raw pair angles...'
        }

        if res.status_code == requests.codes['ok']:
            resJSON = res.json()
            operationResult['isSuccess'] = True
            operationResult['message'] = resJSON['message']
        else:
            operationResult['isSuccess'] = False
            try:
                resJSON = res.json()
                operationResult['message'] = resJSON['message']
            except ValueError:
                operationResult['message'] = res.text
        return operationResult
