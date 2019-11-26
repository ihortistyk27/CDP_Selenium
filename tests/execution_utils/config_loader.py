from configparser import ConfigParser, BasicInterpolation
import os


class Config:
    """Interact with configuration variables."""

    configParser = ConfigParser(interpolation=BasicInterpolation())
    config_file_path = (os.path.join(os.getcwd(), 'configuration/config.ini'))

    @classmethod
    def initialize(cls, config_file):
        """Start config by reading config.ini."""
        cls.configParser.read(cls.config_file_path)

    @classmethod
    def url(cls, key):
        """Get url value from config.ini."""
        return cls.configParser.get('url', key)

    @classmethod
    def credentials(cls, key):
        """Get credentials value from config.ini."""
        return cls.configParser.get("credentials", key, vars=os.environ)
