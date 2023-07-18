'''
Cuando abrimos cualquier cuenta de GitHub, vemos una imagen de perfil, el nombre del usuario y una breve descripción  del usuario en la seccion de perfil. Aquí aprendera a raspar  su imagen de perfil de GitHub 
pip install beautifulsoup4
 pip3 install requests

'''
import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/kalliche"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt":"Avatar"})["src"]
print(profile_picture)