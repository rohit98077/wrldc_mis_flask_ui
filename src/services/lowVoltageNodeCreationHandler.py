import requests
import datetime as dt
from src.typeDefs.lowVoltageNodeCreationResp import LowVoltageNodeCreationResp

class LowVoltageNodeCreationHandler():
    lowVoltageNodeCreationUrl = ''

    def __init__(self, lowVoltageNodeCreationUrl):
        self.lowVoltageNodeCreationUrl = lowVoltageNodeCreationUrl

    def createLowVoltageNode(self, reqFile) ->LowVoltageNodeCreationResp:
        """create Low Voltage Node data using the api service
        Args:
            reqFile: uploaded file
        Returns:
            LowVoltageNodeCreationResp: Result of the Low Voltage Node Creation operation
        """        
        files = {'inpFile': reqFile.read()}
        res = requests.post(self.lowVoltageNodeCreationUrl, files=files)
        
        operationResult: LowVoltageNodeCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create Low Voltage Node data...'
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