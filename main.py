from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html", encoding="utf8"), "html.parser")
table = soup.find('table', attrs={'id':'panel__3'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
data = []

for row in rows:
    cols = row.find_all('td')
    date = cols[7]
    if(date.find("div") != None):
        data.append(f"{cols[4].text.strip()}  -  {cols[6].text.strip()} - {date.find("div")["title"]}")

with open("output.txt", "w+",encoding="utf-8") as f:
    for i in data:
        f.write(i+"\n")