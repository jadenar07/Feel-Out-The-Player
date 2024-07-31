from bs4 import BeautifulSoup
import requests
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster

tms = teams.get_teams()

def get_team_player_ids(team_id):
    for team in tms:
        # if team.get('id') == team_id:
        roster = commonteamroster.CommonTeamRoster(team_id=team_id).get_data_frames()[0]

        player_ids = roster['PLAYER_ID'].tolist()

        return player_ids


players = get_team_player_ids(1610612763)

def fetch_player_images(roster):
    lst = []
    for player in roster:
        url = f"https://www.nba.com/player/{player}"
        p = requests.get(url)

        pp = BeautifulSoup(p.content, 'html.parser')

        image = pp.find('img', class_="PlayerImage_image__wH_YX PlayerSummary_playerImage__sysif")

        if image:
            lst.append(image['src'])
    return lst

print(fetch_player_images(players))

