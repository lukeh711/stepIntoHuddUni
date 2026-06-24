import requests
from bs4 import BeautifulSoup

response = requests.get(f"https://j-archive.com")
html_data = response.text
soup = BeautifulSoup(html_data, "lxml")

title = soup.title.text
linkEndParts = [a["href"] for a in soup.find_all("a", href=True)]

print(f"Title: {title}, links: {linkEndParts}")

for linkEndPart in linkEndParts:
    response2 = requests.get(f"https://j-archive.com/{linkEndPart}")
    html_data2 = response2.text
    soup2 = BeautifulSoup(html_data2, "lxml")
    linkEndParts2 = [a["href"] for a in soup2.find_all("a", href=True)]
    #print(f"{linkEndParts2}")

    cluelist = []
    for linkEndPart2 in linkEndParts2:
        response3 = requests.get(f"https://j-archive.com/{linkEndPart2}")
        html_data3 = response3.text
        soup3 = BeautifulSoup(html_data3, "lxml")
        clues = soup3.find_all(class_="clue_text")
        for clue in clues:
            cluelist.append(clue.get_text(strip=True))

print(cluelist)