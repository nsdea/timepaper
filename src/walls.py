"""This file can be used to download wallpapers from the web using the dict below!
You don't need to run this script every time, just when you want to download new wallpapers.

This is just a helper/tool script:
if you want to, you can just add files manually and name them the hour they should start (file extensions will be ignored!).
"""

wallpapers = {

# The wallpapers will enable when the hour of the day (0-23) is (or is above) the specified number! 
# Lowest numbers/hours first.

# int:HOUR -> str:WALLPAPER_URL

    6:  'https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/56/Three_biomes_concept_art.jpg/revision/latest?cb=20211024124434',
    9:  'https://static.wikia.nocookie.net/minecraft_gamepedia/images/4/4e/Birch_forest_concept_art.jpg/revision/latest?cb=20211024124422',
    18: 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/a9/Mangrove_biome_concept.jpg/revision/latest?cb=20211024124404',
    21: 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/29/Swamp_night_concept_art.jpg/revision/latest?cb=20211024124412'

}

# ===========================================================================================================================================

import urllib.request
from configuration import *

for wall in list(wallpapers.keys()):
    target = IMAGES + str(wall) + '.png'
    print(target)
    urllib.request.urlretrieve(wallpapers[wall], target)