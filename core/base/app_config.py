import base64
import json
import os

from core.singleton import Singleton


class AppSetting(metaclass=Singleton):
    """
    Setting of App level
    Initializes when the app startup
    """
    APP_NAME: str = "Default"
    APP_VERSION: str = "0.0.1"
    APP_VERSION_PATH: str = "/api"
    DEBUG = False
    PORT = 9000
    SECURITY_KEY: str = "test"

    PG_CONF: dict
    REDIS_CONF: dict

    def __init__(self):
        app_setting_str = os.getenv("APP_SETTINGS") or 'e30='

        app_setting: dict = json.loads(base64.b64decode(
            app_setting_str.encode()).decode())
        self.REDIS_CONF: dict = app_setting.get("REDIS_CONF")
        self.PG_CONF: dict = app_setting.get("PG_CONF")

        app_conf = app_setting.get("APP_CONF")
        self.DEBUG = app_conf.get("APP_MODE") == "debug"
        self.SECURITY_KEY = app_conf.get("TOKEN") or self.SECURITY_KEY
        self.PORT = app_conf.get("PORT") or self.PORT
