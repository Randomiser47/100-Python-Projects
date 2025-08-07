import requests
from bs4 import BeautifulSoup
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = (response.text)
soup = BeautifulSoup(yc_web_page,"html.parser")
articles = soup.find_all(name="a",class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get('href')
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]

max_value = (max(article_upvotes))
i = 0
for numbers in article_upvotes:
    i = i + 1
    if max_value == numbers:
        break
i = i - 1 
print(article_texts[i])
print(article_upvotes[i])
print(article_links[i])

