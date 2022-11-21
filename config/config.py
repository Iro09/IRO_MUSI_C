import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "29106416"))
API_HASH = getenv("API_HASH", "280934993af1eb0355ba5d028df87e05")

BOT_TOKEN = getenv("BOT_TOKEN", "5742058322:AAHhVIN1zqXKMpIwvj1HEv2D5W4vZAj2vDI")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Pikku:pikachu01@cluster0.vcfnxij.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001772857132"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𓆩 ꪀꪖꪀᥴꪗ ✘ ꪑꪊ𝘴𝓲ᥴ 𓆪")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5518757491").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Iro09/IRO_MUSI_C")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/iro_bot_support")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/iro_x_support")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "AQAuUbRAR2KVF9VU61Husx2rXhLLjclQ8IpIWW6HRyRfh-OvRxKVJMJQ6Oy9BFjpk0tijFh6T5g9R-SllZjUd8loIbkkmOvlBZzUJ4Q3pUJrDum-WbWXiJHi0a1vfSjYbNR6cFVi78ZKxHfIKWydfinq6kY1KA5hdQ4R2zNP5q_r1JouOEUJxHmvk7_D_zz6UXlk5uZih0VwFjzgW77b-_jcswwQC-310ZCPYpJI7zux2sVYQqOt13QeGTQl1OWXOBlbjfugwo1Kzvf5DpT15-4kTnKN69CI58Yw70BmLgwKVmOp7SPmMyOaHeIllfFqhdnquJHWRIX7K34ogQFyMjUaAAAAAVLMFsEA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "anonxlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/b4260864a06100776da30.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/b4260864a06100776da30.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/24360a3112a467dfbc6c5.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/21901d94941bc664b688b.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/d35f8a58f3faeb861c548.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/e683ca1f9d1f091bc7f1d.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6b2b3bcac4d7a635e47ad.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/0f258bdf2c9739c2c2b76.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/b0956550f8296d47d1850.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/d871673b643c900327369.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/8fea1d5e62505e1ab8beb.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/124638d9d2deac51d736d.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/a1fd4c178b86cdda914e9.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/e683ca1f9d1f091bc7f1d.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/b4260864a06100776da30.jpg"
