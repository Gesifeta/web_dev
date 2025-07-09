import requests
import bs4

year = input("Which year do you want to travel to YYY-MM-DD: ")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}
music_data = requests.get(url ="https://www.billboard.com/charts/hot-100/"+year,headers=headers).text
soup = bs4.BeautifulSoup(music_data, "html.parser")
chart_titles = soup.select("li ul li h3")
titles =[title.getText().strip() for title in chart_titles]

print(titles)