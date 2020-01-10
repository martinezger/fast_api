from dataclasses import dataclass


@dataclass
class DevConfig():
    PROJECT_NAME: str = "fast api example"
    API_V1_PREFIX: str = "/v1"
    API_V2_PREFIX: str = "/v2"
