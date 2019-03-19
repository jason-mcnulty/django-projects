
# https://stackoverflow.com/questions/53187546/beautifulsoup-get-text-create-dictionary


from bs4 import BeautifulSoup, NavigableString
import requests




START_URL = 'https://vappsavpn01-int.internal.das/dana-na/healthcheck/healthcheck.cgi?status=all'


page = requests.get(START_URL, verify=False)

soup = BeautifulSoup(page.text, 'html.parser')








papers = []
for paper in soup.findAll("br"):
    info = [desc.strip() for desc in paper.descendants if type(desc) == NavigableString]
    papers.append({'CPU-UTILIZATION': info[1], 'SSL-CONNECTION-COUNT': info[1], 'USER-COUNT': info[1]})

print(papers[1])
