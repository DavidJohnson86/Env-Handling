from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import logging
import logging.config
logger = logging.getLogger(__name__)

load_dotenv()

class Environment(Enum):
    LOCAL = "LOCAL"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"
    STAGE = "STAGE"


class BaseConfiguration(BaseSettings):
    """Base configuration object based on pydantic.BaseSettings"""

    environment: Environment = Environment.LOCAL
    model_config = SettingsConfigDict(
        env_prefix="",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_file=".env",
        env_file_encoding="utf-8",
    )
    
class OracleConfiguration(BaseSettings):
    connection_url: str = ""

class FTSEConfiguration(BaseSettings):
    # TODO Create interface for General Vendor Settings
    user_name: str = "FTSE"
    password: str = ""
    protocol: str = "SFTP"
    
    
class VendorConfiguration(BaseSettings):
    ftse_configuration : FTSEConfiguration = FTSEConfiguration()
    # List vendor configs here
    
class ServiceConfiguration(BaseConfiguration):
    log_level: int = logging.INFO
    oracle: OracleConfiguration = OracleConfiguration()
    vendor : VendorConfiguration = VendorConfiguration()

configuration: ServiceConfiguration = ServiceConfiguration()

logging_config = {
    "version": 1,
    "formatters": {"f": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"}},
    "handlers": {"h": {"class": "logging.StreamHandler", "formatter": "f",
                       "level": configuration.log_level}},
    "root": {
        "handlers": ["h"],
        "level": configuration.log_level,
    },
}

logging.config.dictConfig(logging_config)
    
if __name__ == "__main__":
    # Ways to Refence for env vars
    # Never print a password this is just a representation
    print(f"FTSE Password: {configuration.vendor.ftse_configuration.password}")
    print(f"Oralce Conecction URL: {configuration.oracle.connection_url}")
    