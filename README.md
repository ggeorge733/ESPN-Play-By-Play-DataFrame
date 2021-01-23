# ESPN Play by Play 

On the ESPN website, there is an option to view the play-by-play information for an NBA game (example <a href='https://www.espn.com/nba/playbyplay?gameId=401267371'> here </a>). This allows users to view a summary of each event that occured during game along with the time and score during the event. This script extracts data from a game using BeautifulSoup and RegEx and creates a Pandas dataframe. 

The Play-by-Play data for any game can be extracted by replacing the URL in the "site" variable. 
