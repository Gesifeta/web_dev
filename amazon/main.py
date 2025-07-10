import smtplib
import requests
import bs4
import os

from api import gmail

pot_url ="https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CYMYK6?th=1"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}

pot_response = requests.get(pot_url,headers=headers)
pot_response.raise_for_status()
text = pot_response.content.decode("utf-8")
soup = bs4.BeautifulSoup(text, "html.parser")



price = soup.find(name="span", id_="_price")
print(price)
