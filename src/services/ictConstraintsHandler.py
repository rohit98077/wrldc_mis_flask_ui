import requests
import datetime as dt
from src.typeDefs.ictConstraintsCreationResp import IctConstraintsCreationResp

class IctConstraintsCreationHandler():
    ictConstrainstsCreationUrl = ''

    def __init__(self, ictConstrainstsCreationUrl):
        self.ictConstrainstsCreationUrl = ictConstrainstsCreationUrl

    def createIctConstraints(self, reqFile) ->IctConstraintsCreationResp:
        """create ict constraints data using the api service
        Args:
            reqFile: uploaded file
        Returns:
            IctConstraintsCreationResp: Result of the ict constraints data creation operation
        """        
        files = {'inpFile': reqFile.read()}
        res = requests.post(self.ictConstrainstsCreationUrl, files=files)
        
        operationResult: IctConstraintsCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create ict constraints data...'
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