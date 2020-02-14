from configparser import ConfigParser, BasicInterpolation
import os


class Config:
    """Interact with configuration variables."""

    configParser = ConfigParser(interpolation=BasicInterpolation())
    config_file_path = 'C:\\CDP_Selenium\\tests\\configuration\\config.ini'
    #
    @classmethod
    def initialize(cls):
        """Start config by reading config.ini."""
        cls.configParser.read(cls.config_file_path)

    @classmethod
    def credentials(cls, key):
        """Get credentials value from config.ini."""
        return cls.configParser.get('credentials', key, vars=os.environ)


Config.initialize()
print(Config.config_file_path)
print(Config.configParser.sections())
print(Config.credentials('email'))