import requests, bs4, re
import pandas as pd

#use requests to retrieve site
site = requests.get('https://www.espn.com/nba/playbyplay?gameId=401267290')

#beautiful soup converts site into text of all html code
soup = bs4.BeautifulSoup(site.text, 'html.parser')


#html of info for full game in "gamepackage-qtrs-wrap"
main = soup.find('div', id  = "gamepackage-qtrs-wrap")

#print(main.text)  

timestamp = main.find_all('td', class_ = 'time-stamp') #finds all instances of time stamps (ex. "12:00")

time = [] #empty list too add info in 


for t in timestamp: #cycles through each instance, converts to text and adds it to "time" list
    stamp = t.text
    time.append(stamp) #adds each value to "time" list

combscore = main.find_all('td', class_ = 'combined-score') #returns score (ex. 2-2), away team first 

cscore = []

for c in combscore:
    coscore = c.text
    cscore.append(coscore)

game_details = main.find_all('td', class_ = 'game-details') #provides summary of event during each timestamp

game_det = []

for g in game_details:
    game = g.text
    game_det.append(game)

table = {} #dictionary to add lists, use [''] to add lists
table['Time'] = time
table['Score'] = cscore
table['Detail'] = game_det

df = pd.DataFrame(table)

df['Away'] = df['Score'].str.split("-").str[0] #splits score by two numbers, 0 for first number and 1 for second
df['Home'] = df['Score'].str.split("-").str[1]
df['Away'] = pd.to_numeric(df['Away']) #converts both to integers
df['Home'] = pd.to_numeric(df['Home'])

points = df['Away'] + df['Home']
df['Points'] = points.diff().fillna(0)
#add away and home score, then subtracts from previous row to get change in points
#fillna changes first value from NaN to 0

df['Scorer'] = df['Detail'].str.extract(r'(.+) makes') #extracts name before 'makes' to get player who scored

df['Assist'] = df['Detail'].str.extract(r'\((.+) assists\)') #refer to https://regex101.com/r/L3rtse/1, get name between "(" and "assists"

df['Rebound'] = df['Detail'].str.extract(r'(.+) (.+) rebound')[0] #takes everything before rebound. first (.+) is name or team, second (.+) is team or offensive/defensive

df['Steal'] = df['Detail'].str.extract(r'\((.+) steals') #finds name between "(" and steals

df['Block'] = df['Detail'].str.extract(r'(.+) blocks') #finds name before "blocks"


print(df.head(20))


