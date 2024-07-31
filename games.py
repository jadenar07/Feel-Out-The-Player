from bs4 import BeautifulSoup
import requests

from datetime import datetime, timedelta

# Actual time retrival for the 3 days
"""""
today = datetime.today().date()

day1 = today - timedelta(days=1)
day2 = today - timedelta(days=2)

"""""

lst = []
today = "2024-03-31"
day1 = "2024-03-30"
day2 = "2024-03-29"


lst.append(today)
lst.append(day1)
lst.append(day2)


for x in lst:
    url = f"https://www.nba.com/games?date={x}"

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup.find_all('div', class_="GameCardMatchup_wrapper__uUdW8"))
    # print(soup.find('div', class_="GameCardMatchup_wrapper__uUdW8"))
    s = soup.find_all('span', class_="MatchupCardTeamName_teamName__9YaBA")


    l = len(s)
    index = 0
    left = 0
    right = 1

    hm = {}

    while right < l:
        hm[index] = [s[left].text ,s[right].text]
        index += 1
        left += 2
        right += 2

    # print(hm.keys())
    for game in hm.values():
        print(game)

    print("---------------------------------------------------------------------")


