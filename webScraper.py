import requests

i=1
response = requests.get(f"https://j-archive.com/showseason.php?season={i}")

i=2
response = requests.get(f"https://j-archive.com/showseason.php?season={i}")

html_data = response.text
print(html_data)