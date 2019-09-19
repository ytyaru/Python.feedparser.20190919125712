import feedparser
import datetime
import sys

if len(sys.argv) < 2:
    raise Error('第1引数にRSSのURLを指定してください。')
    exit()
rss = sys.argv[1]
entries = feedparser.parse(rss).entries
print(len(entries))
for entry in entries:
    print(datetime.datetime
        .strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z')
        .strftime('%Y-%m-%dT%H:%M:%SZ%z'))
    print(entry.link)
    print(entry.title)
    if 'content' in entry : print(entry.content)
    print()

