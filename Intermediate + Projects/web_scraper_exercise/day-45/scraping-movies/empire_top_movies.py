import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

empire_website = (response.text)
soup = BeautifulSoup(empire_website,"html.parser")
all_titles = []
titles = soup.find_all('h3')
counter = 1
list_number = []
for title in titles:
    title_text = title.getText()
    all_titles.append(title_text)
reversed_list = reversed(all_titles)
for items in reversed_list:
    falcon = items+"\n"
    print(falcon)
    with open('100_movies.txt.','a') as file:
        file.write(falcon)
#print(all_titles)
#print(list_number)
