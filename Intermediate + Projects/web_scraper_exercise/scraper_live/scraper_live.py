from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_live_website = response.text
soup = BeautifulSoup(yc_live_website,"html.parser")

articles_links = soup.find_all('a')
titles = []
links = []

article_titles = soup.find_all(name = "td", class_ ="title")
for td in article_titles:
    span = td.find("span", class_="titleline")
    if span:
        a_tag = span.find("a")
        titles.append(a_tag.getText())
        links.append(a_tag.get("href"))

article_upvotes =[int(score.getText().split()[0]) for score in  soup.find_all(name="span",class_="score")]

max_upvotes = (max(article_upvotes))
index_number = article_upvotes.index(max_upvotes) 
print(titles[index_number])
print(links[index_number])
print(article_upvotes[index_number])
