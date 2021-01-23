# ESPN Play by Play DataFrame

### On the ESPN website, there is an option to view the play-by-play information for an NBA game (example <a href='https://www.espn.com/nba/playbyplay?gameId=401267371'> here </a>). This allows users to view a summary of each event that occured during game along with the time and score during the event. This script extracts data from a game using BeautifulSoup and RegEx and creates a Pandas dataframe. 

The Play-by-Play data for any game can be extracted by replacing the URL in the "site" variable. 


<b>Time</b>: The timestamp when the event occurred
<b>Score</b>: The score during the event. The away team is first, followed by the home team
<b>Detail</b>: A description of a specific play/event during the game
### Away: The away team score
### Home: The home team score
### Points: The amount of points scored during the play
### Scorer: The player who scored during the play
### Assist: The player credited with an assist
### Rebound: The player credited with the rebound (also can be credited to either team)
### Steal: The player credited with the steal
### Block: The player credited with the block
