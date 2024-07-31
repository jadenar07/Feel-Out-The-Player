from bs4 import BeautifulSoup
import requests
from nba_api.stats.static import teams

tms = teams.get_teams()

for tm in tms:
    url = f"https://www.nba.com/team/{tm.get('id')}"
    p = requests.get(url)
    s = BeautifulSoup(p.content, 'html.parser')

    logo_div = s.find('div', class_='TeamHeader_logoBlock__WjNZB')
    logo_img = logo_div.find('img') if logo_div else None

    if logo_img:
        print(f"{tm.get('full_name')} : {logo_img['src']}")
    else:
        print(f"Logo not found for team: {tm.get('full_name')}")
# lol pls commit