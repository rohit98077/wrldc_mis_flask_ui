import requests
import datetime as dt
from src.typeDefs.highVoltageNodeCreationResp import HighVoltageNodeCreationResp

class HighVoltageNodeCreationHandler():
    highVoltageNodeCreationUrl = ''

    def __init__(self, highVoltageNodeCreationUrl):
        self.highVoltageNodeCreationUrl = highVoltageNodeCreationUrl

    def createHighVoltageNode(self, reqFile) ->HighVoltageNodeCreationResp:
        """create High Voltage Node data using the api service
        Args:
            reqFile: uploaded file
        Returns:
            HighVoltageNodeCreationResp: Result of the High Voltage Node data creation operation
        """        
        files = {'inpFile': reqFile.read()}
        res = requests.post(self.highVoltageNodeCreationUrl, files=files)
        
        operationResult: HighVoltageNodeCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create High Voltage Node data...'
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