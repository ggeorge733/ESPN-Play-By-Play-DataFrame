# ESPN Play-By-Play DataFrame

On the ESPN website, there is an option to view the play-by-play information for an NBA game (example <a href='https://www.espn.com/nba/playbyplay?gameId=401267371'> here</a>). This allows users to view a summary of each event that occured during a game along with the time and score during the event. This script extracts data from a game using BeautifulSoup and RegEx and creates a Pandas dataframe. 

The Play-By-Play data for any game can be extracted by replacing the URL in the "site" variable.

DataFrame columns:\
<b>Time</b>: The timestamp when the event occurred\
<b>Score</b>: The score during the event. The away team is first, followed by the home team\
<b>Detail</b>: A description of a specific play/event during the game\
<b>Quarter</b>: Quarter event takes place. Overtime(s) are 5+\
<b>Away</b>: The away team score\
<b>Home</b>: The home team score\
<b>Points</b>: The amount of points scored during the play\
<b>Scorer</b>: The player who scored during the play\
<b>Assist</b>: The player credited with an assist\
<b>Rebound</b>: The player credited with the rebound (also can be credited to either team)\
<b>Steal</b>: The player credited with the steal\
<b>Block</b>: The player credited with the block
