# ESPN Play by Play 

On the ESPN website, there is an option to view the play-by-play (ex <a href='https://www.espn.com/nba/playbyplay?gameId=401267371'> here </a>) information for an NBA game. This allows users to view a summary of each event that occured during game along with the time and score during the event. This script extracts data from a game using BeautifulSoup and RegEx and creates a Pandas dataframe. 

Replacing the url in the "site" variable with the Play-By-Play site for any NBA (ex. https://www.espn.com/nba/playbyplay?gameId=401267371)
