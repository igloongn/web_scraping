from bs4 import BeautifulSoup as bs
import requests as req
import csv


def fine(unknown):
    data = unknown.prettify()
    return data

url = 'https://coreyms.com/'
parser = 'lxml'
res = req.get(url)
res=res.text
soup = bs(res, parser)
# article = soup.article 
# print(fine(article))

#CSV
csv_file = open('ms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['header', 'summary', 'video_link'])


for article in soup.find_all('article'):
    print()
    print()

    headline = article.a.text
    print(headline)
    print()
    print()
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    print()

    try:
        vid_src = article.find('iframe', class_= 'youtube-player')

        vid_id = vid_src['src']
        vid_id = vid_id.split('/')[4].split('?')[0]
        vid_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        vid_link = None

    print(vid_link)
    print()
    csv_writer.writerow([headline, summary, vid_link])
csv_file.close()