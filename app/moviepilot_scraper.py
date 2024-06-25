from pickle import NONE
import selenium
from bs4 import BeautifulSoup
import requests
import pandas as pd
#import config_template
import config
import ujson
import os
import time

class MoviepilotScraper:
    def __init__(self, 
                 username=config.MOVIEPILOT_USERNAME, 
                 password=config.MOVIEPILOT_PASSWORD):
        self.session = requests.Session()
        self.main_url = config.MOVIEPILOT_BASE_URL
        self.base_url_movies = config.MOVIEPILOT_RATED_MOVIES
        self.movies_url_part = config.MOVIEPILOT_RATED_MOVIES_BASE_URL

        self.base_url_series = config.MOVIEPILOT_RATED_SERIES
        
        
        self.username = username
        self.password = password
        
        if username and password:
            self.login()

    def login(self):
        login_payload = {
            'username': self.username,
            'password': self.password,
        }

        headers = {
            'authority': 'm.moviepilot.de',
            'method': 'POST',
            'path': '/api/session',
            'scheme': 'https',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://m.moviepilot.de',
            'Referer': 'https://m.moviepilot.de/',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            # Add any cookies or additional headers if needed
        }

        response = self.session.post(self.main_url, data=ujson.dumps(login_payload), headers=headers)
        print(f"Login Response: {response}")
        if response.status_code != 200 or "login failed" in response.text.lower():
            raise Exception("Login failed")

        
    def logout(self):
        headers = {
            'authority': 'm.moviepilot.de',
            'method': 'DELETE',
            'path': '/api/session',
            'scheme': 'https',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Origin': 'https://m.moviepilot.de',
            'Referer': 'https://m.moviepilot.de/',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            # Add any cookies or additional headers if needed
        }

        response = self.session.delete(self.main_url, headers=headers)
        print(f"Logout Response: {response}")
        if response.status_code != 200:
            raise Exception("Logout failed")


    def scrape_all_movies(self)->pd:
        response = self.session.get(self.base_url_movies)
        soup = BeautifulSoup(response.content, 'html.parser')
        with open(".\\data\\moviepilot_movies.html", 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        #print(soup)
        a_tag = soup.find('a', class_='pagination--last')

        all_data = []

        if a_tag:
            href_value = a_tag.get('href')
            print(href_value)
            num_pages = int(href_value.split('=')[-1])
            print(f"num_pages {num_pages}")
            time.sleep(2)  # 2-second delay

            # Scrape data from all pages
           
            for page in range(1, 1):#num_pages + 1):
                df = self.scrape_page(page)
                if df is not None:
                    all_data.append(df)
                # Introduce a delay to avoid overloading the server
                time.sleep(2)  # 2-second delay

        return all_data


    #    if response.status_code == 200:
    #        soup = BeautifulSoup(response.content, 'html.parser')
    #        ratings = []
    #        for item in soup.select('.some-css-selector'):  # Adjust the selector based on actual HTML structure
    #            title = item.select_one('.title-selector').text.strip()
    #            rating = item.select_one('.rating-selector').text.strip()
    #            ratings.append((title, rating))
    #        return ratings
    #    else:
    #        print(f"Failed to retrieve page {url}")
    #        return []


    def scrape_movie_page(self, page_number:int)->pd:
        if page_number == 1:
            URL = f"{self.base_url_movies}"
        else:
            URL = f"{self.movies_url_part}{page_number}"
        
        response = self.session.get(URL)

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table(s) on the page
        tables = soup.find_all('table')

        if tables:
            table = tables[0]
            df = pd.read_html(str(table))[0]
            return df

        return None



#    def getting_all_movies():
#
#        URL = f"{config_template.MOVIEPILOT_RATED_MOVIES}"
#        response = re.get(URL)
#
#        soup = BS(response.content, 'html.parser')
#
#        last_page = soup.find('a', {'title': 'Letzte'})
#
#        num_pages = int(last_page['href'].split('=')[-1]) if last_page else 1
#
#        # Scrape data from all pages
#        all_data = []
#        for page in range(1, num_pages + 1):
#            df = scrape_page(page)
#            if df is not None:
#                all_data.append(df)
#            # Introduce a delay to avoid overloading the server
#            time.sleep(2)  # 2-second delay
#
#        # Combine all data into a single DataFrame
#        combined_df = pd.concat(all_data, ignore_index=True)
#
#        # Convert the DataFrame to JSON
#        data_json = combined_df.to_json(orient='records', indent=2)
#
#        # Save the JSON to a file or print it
#        with open(f"{config_template.data_path}+moviepilot_movies.json", 'w') as f:
#            f.write(data_json)
#
#        print(data_json)
#
#def clear_all_temp_json():
#    try:
#        os.remove(f"{config_template.data_path}+moviepilot_movies.json")
#
#    except OSError:
#        pass
#
#    try:
#        os.remove(f"{config_template.data_path}+moviepilot_series.json")
#        
#    except OSError:
#        pass
#


if __name__ == "__main__":
    pass