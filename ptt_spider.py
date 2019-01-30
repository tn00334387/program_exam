import sys
import requests

#if sys.argv[1] is None:
#    print "Please execute the spider with url input as \n python ptt_spider.py <URL>"
#    sys.exit(0)

res = requests.get(sys.argv[1])

ptt_contain = {'Time': "", 'Author': "", 'Title': "", 'Text': "", 'Board': ""} 

author_start = res.text.find('<span class="article-meta-value">') + 33
author_end = res.text.find('</span></div>',author_start)

board_start = res.text.find('<span class="article-meta-value">',author_end) + 33
board_end = res.text.find('</span></div>',board_start)

title_start = res.text.find('<span class="article-meta-value">',board_end) + 33
title_end = res.text.find('</span></div>',title_start)

time_start = res.text.find('<span class="article-meta-value">',title_end) + 33
time_end = res.text.find('</span></div>',time_start)

text_start = time_end + 13
text_end = res.text.find('<span class="f2">',text_start)

ptt_contain['Board'] = res.text[board_start:board_end]
ptt_contain['Author'] = res.text[author_start:author_end]
ptt_contain['Time'] = res.text[time_start:time_end]
ptt_contain['Title'] = res.text[title_start:title_end]
ptt_contain['Text'] = res.text[text_start:text_end]

for key, value in ptt_contain.iteritems():
    print key , ":" , value

