import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 360))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6532412571))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/mamakli06/mamaklimusic1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kumsaldestekkanal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kumsalmuzikk")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAHGTCYAM-ipSOFeP3_ALTHOmsGFdbDX8jW2LZEXwkcsHdqrr_dQ3iTiy7bRNN42UJynk-4UBFMLtRAUAhM3CEs-8tI2ObX7faMW5AJ8hJUfAn9M9W-Vu9FVO7-TkgDtg5KSVVWVj4iakROvw_MAVoQUq3KsNntxBxeUtQXrKKWUBAnj36_NakS_ypkVq9IdJUszLe3wsqhTPtsKbgxLbxni7Mo2xBJ418WTG6HgI-ZFt2iXtrlqAxFgKwLQrPYymNBaz6bVWhmJaB632Obw47pFVboFf5M0iP5YkVCcIJObtTjTB2KlHKwPpHxcUynzQo2okgTQTL6rd584T1VoGGnSp4tXDgAAAAGxQGFHAA")
STRING2 = getenv("STRING_SESSION2", "AgFipAAATCKHJVqUy-oQ4SaOi9KX7y4JquMaacNOqD56pFcUhdI4_d2b1Ct7TdvMffEdKFsRBo7_1c1vu2VucbJyb_V3kmgGajPjOLgh2sQrEAZ9Zl-SUxMMrcJK4kG5X0QrOVze3amlT2zd2nQ0pcSHZMyzZ9S0SrPBcrRQg-qx-VQFA86u_jDYV-nrzFcjgESbrQ_uAQWl0FszXI7dUzu_E21YsBMKCcQ9OcBrOgtBOR5XaPDjSm1D-nsclWUu9aEOURO304QwCV53V_8CyDBFSap3ZOjYzfcjciytSRqc_eS3FTOs_HrNI8SDizZ6ExgQNGxD_ch8xJW9O9TaiPGDro-c_QAAAAG8nzf6AA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
   "START_IMG_URL", "https://telegra.ph/Jww-06-18"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/Jww-06-18"
)
PLAYLIST_IMG_URL = "https://telegra.ph/Jww-06-18"
STATS_IMG_URL = "https://telegra.ph/Jww-06-18"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Jww-06-18"
TELEGRAM_VIDEO_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
STREAM_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
