import pandas as pd
from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard


# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]

# json
career.get_json()

# dictionary
c = career.get_dict()

