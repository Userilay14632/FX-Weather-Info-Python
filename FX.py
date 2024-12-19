import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

class FXWeatherInfo:
    def __init__(self, latitude: str, longitude: str, user_agent: str):
        geolocator = Nominatim(user_agent=user_agent)
        result = geolocator.reverse(f"{latitude},{longitude}")
        global address
        address = result.get("address")
    def get_temp(self) -> str:
        global address
        html = requests.get(f"https://google.com/search?q=weather+at+{address}").content
        soup = BeautifulSoup(html, "html.parser")
        return soup.select("#wob_tm")[0].getText() + "°"
    def get_weather(self) -> str:
        global address
        html = requests.get(f"https://google.com/search?q=weather+at+{address}").content
        soup = BeautifulSoup(html, "html.parser")
        return soup.select("#wob_dc")[0].getText()
    def get_day_of_week_and_time(self, is_use_pm=True) -> str:
        global address
        html = requests.get(f"https://google.com/search?q=weather+at+{address}").content
        soup = BeautifulSoup(html, "html.parser")
        return soup.select("#wob_dts")[0].getText()
    def get_humidity(self) -> str:
        global address
        html = requests.get(f"https://google.com/search?q=weather+at+{address}").content
        soup = BeautifulSoup(html, "html.parser")
        return soup.select("#wob_hm")[0].getText()
    def get_wind(self) -> str:
        global address
        html = requests.get(f"https://google.com/search?q=weather+at+{address}").content
        soup = BeautifulSoup(html, "html.parser")
        return soup.select("#wob_ws")[0].getText()
    def get_min_temp(self) -> str:
        global address
        json = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?q={address['address']['state']}").json()
        return json['main'].get("min_temp")
    address = None

cls = FXWeatherInfo()