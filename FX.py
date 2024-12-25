import mtranslate
from geopy.geocoders import Nominatim
import requests
from bs4 import BeautifulSoup
from autocorrect import Speller


def translate_string(text, srclang, destlang) -> str:
    return mtranslate.translate(text, destlang, srclang)


class FXWeatherInfo:
    def __init__(self, useragent: str, latitude: float, longitude: float):
        global address
        geolocator = Nominatim(user_agent=useragent)
        try:
            address = geolocator.reverse(f"{str(latitude)},{str(longitude)}", language="en").raw
        except:
            raise Exception("Address Exception!", "Please check latitude and longitude")

    address = {}

    def get_temp(self, iscelsius: bool) -> int:
        texted = f"Weather in {address['address'].get('city')}"
        texted = translate_string(texted, "en", "ru")
        speller = Speller()
        texted = speller(texted)
        texted = texted.replace(" ", "_")
        html = requests.get(f"https://rp5.ru/{texted}").content
        bs = BeautifulSoup(html, "html.parser")
        if iscelsius==True:
            return int(bs.select(".t_0")[0].getText().replace(" °C", ""))
        else:
            return int(bs.select(".t_1")[0].getText().replace(" °F", ""))

    def get_feeled_temp(self, iscelsius: bool) -> int:
        texted = f"Weather in {address['address'].get('city')}"
        texted = translate_string(texted, "en", "ru")
        speller = Speller()
        texted = speller(texted)
        texted = texted.replace(" ", "_")
        html = requests.get(f"https://rp5.ru/{texted}").content
        bs = BeautifulSoup(html, "html.parser")
        if iscelsius == True:
            return int(bs.select(".t_0")[3].getText().replace(" °C", ""))
        else:
            return int(bs.select(".t_1")[3].getText().replace(" °F", ""))

    def get_archive_weather(self):
        texted = f"Weather in {address['address'].get('city')}"
        texted = translate_string(texted, "en", "ru")
        speller = Speller()
        texted = speller(texted)
        texted = texted.replace(" ", "_")
        html = requests.get(f"https://rp5.ru/{texted}").content
        bs = BeautifulSoup(html, "html.parser")
        returnedtext = ""
        for i in bs.select(".archiveStr_cell"):
            if returnedtext == "":
                returnedtext = i.getText() + ", "
            else:
                returnedtext = returnedtext + i.getText() + ", "
        returnedtext = returnedtext[3:-1:1]
        returnedtext = returnedtext[0:-1:1]
        return returnedtext



cls = FXWeatherInfo("FX.py", 56.277818, 43.921543)
print(cls.get_weathers())