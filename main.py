import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://projetos.digitalinnovation.one/blog")
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all(class_="post")

all_posts = []
for post in posts:
    info = post.find(class_='post-content')
    title = info.h2.a.text
    preview = info.p.text
    date = info.footer.time['datetime']
    img = post.find(class_='wp-post-image')['src']
    author = post.find(class_='post-author').text

    all_posts.append({
        'title': title,
        'preview': preview,
        'date': date,
        'author': author[5:],
        'img': img
    })

with open('posts.json', 'w') as json_file:
    json.dump(all_posts, json_file, indent=3, ensure_asciii=False)
