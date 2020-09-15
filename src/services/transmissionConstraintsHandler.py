import requests
import datetime as dt
from src.typeDefs.transmissionConstraintsCreationResp import TransmissionConstraintsCreationResp

class TransmissionConstraintsCreationHandler():
    transmissionConstrainstsCreationUrl = ''

    def __init__(self, transmissionConstrainstsCreationUrl):
        self.transmissionConstrainstsCreationUrl = transmissionConstrainstsCreationUrl

    def createTransmissionConstraints(self, reqFile) ->TransmissionConstraintsCreationResp:
        """create transmission constraints data using the api service
        Args:
            reqFile: uploaded file
        Returns:
            TransmissionConstraintsCreationResp: Result of the transmission constraints data creation operation
        """        
        files = {'inpFile': reqFile.read()}
        res = requests.post(self.transmissionConstrainstsCreationUrl, files=files)
        
        operationResult: TransmissionConstraintsCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create transmission constraints data...'
        }

        if res.status_code == requests.codes['ok']:
            resJSON = res.json()
            operationResult['isSuccess'] = True
            operationResult['message'] = resJSON['message']
        else:
            operationResult['isSuccess'] = False
            try:
                resJSON = res.json()
                print(resJSON['message'])
                operationResult['message'] = resJSON['message']
            except ValueError:
                operationResult['message'] = res.text
                # print(res.text)
        return operationResult