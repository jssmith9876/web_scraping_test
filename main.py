# Tutorial found on:
# https://www.youtube.com/watch?v=ng2o98k983k
from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_scr = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_scr.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = 'https://youtube.com/watch?{}'.format(vid_id)
    except Exception as e:
        yt_link = None

    print(yt_link)
    
    print()

