import requests
import bs4
res= requests.get('https://finance.naver.com/marketindex/').text
#print(res)
text= bs4.BeautifulSoup(res, 'html.parser')
usd = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(usd.text)