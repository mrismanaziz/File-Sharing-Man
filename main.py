import sys

from bot import Bot
from config import ADMINS, LOGGER, OWNER_ID
from requests import get

try:
    Bot().run()
    blacklistman = get(
        "https://raw.githubusercontent.com/mrismanaziz/Reforestation/master/manblacklist.json"
    ).json()
    if OWNER_ID and ADMINS in blacklistman:
        LOGGER.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, BOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @mrismanaziz"
        )
        sys.exit(1)
except Exception as e:
    LOGGER.info(str(e), exc_info=True)
    sys.exit(1)
