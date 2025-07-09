import bs4
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇
response = requests.get(URL)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, "html.parser")
titles = soup.find_all(name="h3", attrs={"class": "title"})
years = soup.find_all(name="strong")

top_movies = [movie.getText() for movie in reversed(titles)]
movie_years = [year.getText() for year in reversed(years)]
with open("top_movies.txt", "w",encoding= "UTF-8") as file:
    for movie in top_movies:
        file.write(movie + "\n")



