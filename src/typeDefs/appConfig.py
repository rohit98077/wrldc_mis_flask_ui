from typing import TypedDict

class IAppConfig(TypedDict):
    flaskSecret:str
    flaskPort:str
    rawOutagesCreationServiceUrl: str
    rawPairAnglesCreationServiceUrl:str
    weeklyRepCreationServiceUrl:str