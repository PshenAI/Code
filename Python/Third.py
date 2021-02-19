
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('6d00d1d4e704068d70191bad2673e0cc')
mgr = owm.weather_manager()

place = input('Where are you: ')

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(place)
w = observation.weather

print(w)