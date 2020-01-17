from dataclasses import dataclass

def config_factory(environment):
        if 'dev' == environment:
            return  DevConfig
        elif 'qa' == environment:
            return QaConfig
        elif 'prod' == environment:
            return ProdConfig
        else:
            raise ValueError("only qa, dev or prod are allow")

@dataclass
class BaseConfig():
    PROJECT_NAME: str
    HOST: str = "0.0.0.0"
    PORT: str = 5001
    API_V1_PREFIX:str = "/v1"
    API_V2_PREFIX:str = "/v2"

class DevConfig(BaseConfig):
    PROJECT_NAME = "fast api example Dev Api"

class QaConfig(BaseConfig):
    PROJECT_NAME: str = "fast api example Qa Api"
    PORT = 5002

class ProdConfig(BaseConfig):
    PROJECT_NAME: str = "fast api example Prod Api"
    PORT=5003

