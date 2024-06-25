import selenium as se
from bs4 import BeautifulSoup as BS
import requests as re
import pandas as pd
import config_template
from moviepilot_scraper import MoviepilotScraper

def main():
    M_scraper = MoviepilotScraper()
    M_scraper.__init__()

    try:
        movie_ratings = M_scraper.scrape_all_movies()
        #series_ratings = scraper.scrape_all_pages(base_url_series, page_limit)
        print("All Data in movie_ratings:")
        print(movie_ratings)

        #all_ratings = movie_ratings #+ series_ratings

        #for title, rating in all_ratings:
        #    print(f"{title}: {rating}")
    finally:
        M_scraper.logout()

if __name__ == "__main__":
    main()