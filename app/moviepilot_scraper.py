from pickle import NONE
import selenium as se
from bs4 import BeautifulSoup as BS
import requests as re
import pandas as pd
import config_template
import config

def scrape_page(page_number:int):
    URL = f"{config_template.MOVIEPILOT_RATED_MOVIES_BASE_URL}{page_number}"

    return NONE

if __name__ == "__main__":
    pass