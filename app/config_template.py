# config_template.py
MOVIEPILOT_USERNAME = 'your_moviepilot_username'
MOVIEPILOT_PASSWORD = 'your_moviepilot_password'
IMDB_USERNAME = 'your_imdb_username'
IMDB_PASSWORD = 'your_imdb_password'


#links
MOVIEPILOT_BASE_URL = "https://www.moviepilot.de/"
MOVIEPILOT_RATED_MOVIES= f"https://www.moviepilot.de/users/{MOVIEPILOT_USERNAME}/rated/movies"
MOVIEPILOT_RATED_MOVIES_BASE_URL = f"https://www.moviepilot.de/users/{MOVIEPILOT_USERNAME}/rated/movies?page=" #Needs only page number
#A 100 Movies
#tbody

#href="/users/themoviemonster/rated/movies?page=2" for new pages
#https://www.moviepilot.de/users/themoviemonster/rated/movies?page=2
MOVIEPILOT_MOVIE_MAX_PAGES= 5
#https://www.moviepilot.de/users/{MOVIEPILOT_USERNAME}/rated/movies?page={}

MOVIEPILOT_RATED_SERIES=""

if __name__ == "__main__":
    pass
