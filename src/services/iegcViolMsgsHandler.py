import requests
import datetime as dt
from src.typeDefs.iegcViolMsgsCreationResp import IegcViolMsgsCreationResp


class IegcViolMsgsCreationHandler():
    iegcViolMsgsCreationUrl = ''

    def __init__(self, iegcViolMsgsCreationUrl):
        self.iegcViolMsgsCreationUrl = iegcViolMsgsCreationUrl

    def createIegcViolMsgs(self, reqFile) ->IegcViolMsgsCreationResp:
        """create IEGC Violation Msgs using the api service
        Args:
            reqFile: uploaded file
        Returns:
            IegcViolMsgsCreationResp: Result of the IEGC Violation Msgs creation operation
        """        
        files = {'inpFile': reqFile.read()}
        res = requests.post(self.iegcViolMsgsCreationUrl, files=files)
        
        operationResult: IegcViolMsgsCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create iegc violation messages...'
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