import os

from core.base.app_config import AppSetting

UTF8 = "utf-8"
PROJECT_DIR = os.path.dirname(__file__).replace("/core", "").replace(
    r"\\core", "")

APP_CONF = AppSetting()

__all__ = [
    "UTF8",
    "PROJECT_DIR",

    "AppSetting",
    "APP_CONF",
]