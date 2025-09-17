from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6965488457"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")
API_ID = int(environ.get('API_ID', '22141398'))
API_HASH = environ.get('API_HASH', '0c8f8bd171e05e42d6f6e5a6f4305389')
BOT_TOKEN = str(getenv("BOT_TOKEN", "8489824766:AAGywkup5LBgGBFp6oN1LZe8puq6n732JGM"))
FORCE_SUB = os.environ.get("FORCE_SUB", "1002200226545") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://mmmmmehar191:P75xf2nybiVeqUuJ@cluster0.1t94pie.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
