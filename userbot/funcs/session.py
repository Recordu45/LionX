import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config
from .client import LionXClient

__version__ = "2.10.6"

loop = None


session = StringSession(str(Config.STRING_SESSION))
session2 = StringSession(str(Config.STRING_SESSION2))
session3 = StringSession(str(Config.STRING_SESSION3))
session4 = StringSession(str(Config.STRING_SESSION4))
session5 = StringSession(str(Config.STRING_SESSION5))




if Config.STRING_SESSION:
    bot1 = LionXClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    bot1 = None

if Config.STRING_SESSION2:
    bot2 = LionXClient(
        session=session2,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    bot2 = None

if Config.STRING_SESSION3:
    bot3 = LionXClient(
        session=session3,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    bot3 = None

if Config.STRING_SESSION4:
    bot4 = LionXClient(
        session=session4,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    bot4 = None

if Config.STRING_SESSION5:
    bot5 = LionXClient(
        session=session5,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    bot5 = None

lionub = [bot, bot2, bot3, bot4, bot5]

lionub.tgbot = tgbot = LionXClient(
    session="LionTgXBot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.TG_BOT_TOKEN)
