import requests
from bs4 import BeautifulSoup
import json

url = "https://www.w3schools.com/html/html_tables.asp"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

pagetitle=soup.title.string if soup.title else "No Title"

print(pagetitle)

links_list = []
for link in soup.find_all("a"):
    href=link.get("href")
    if href:
        print(href)
        links_list.append(href)

tabledata=[]
table=soup.find("table")
if table:
    rows=table.find_all("tr")
    for row in rows[1:]:
        cols=row.find_all("td")
        row_data=[col.text.strip() for col in cols]
        print(row_data)
        tabledata.append(row_data)

extracted_data={
    "page_title":pagetitle,
    "total_links":len(links_list),
    "links":links_list,
    "table_data":tabledata
}

with open("extracteddata.json",'w',encoding="utf-8") as file:
    json.dump(extracted_data,file,indent=4)