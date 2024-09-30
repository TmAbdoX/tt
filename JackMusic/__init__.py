from JackMusic.core.bot import Alina
from JackMusic.core.dir import dirr
from JackMusic.core.git import git
from JackMusic.core.userbot import Userbot
from JackMusic.misc import dbb, heroku
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Alina()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
