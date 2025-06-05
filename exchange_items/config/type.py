import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class FlaskConfig:
    secretKey: str


@dataclass
class SQLAlchemyConfig:
    sqlalchemyEcho: bool


@dataclass
class DBConfig:
    hostPort: str
    username: str
    password: str
    database: str
    maxIdleConn: int
    maxOpenConn: int
    maxConnLifetime: datetime.timedelta


@dataclass
class ServiceConfig:
    enableLogin: bool
    enablePubsub: bool
    enableJob: bool
    fernetKey: str
    googleClientId: str
    googleClientSecret: str
    oauth2Callback: str
    gcpResourcePrefix: str
    backgroundJobFailureWaitTime: int
    emailSvcEndpoint: str
    logSinkAdditionalIncludeFilters: str
    topicName: str
    enablePubsubProvisionInApp: bool
    enableLogsinkProvisionInApp: bool
    envURLList: Optional[str]


@dataclass
class Config:
    flask: FlaskConfig
    sqlalchemy: SQLAlchemyConfig
    db: DBConfig
    service: ServiceConfig
