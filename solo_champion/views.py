from django.http import  JsonResponse
import requests
from bs4 import BeautifulSoup
from static.items import items_list
def get_items(request):
	champion_name = request.GET.get('champion_name')
	url = f"https://rankedboost.com/league-of-legends/build/{champion_name}/"
	res = requests.get(url)
	soup = BeautifulSoup(res.content, 'html.parser') 
	with open("solo_champion/scraper/string_file.txt", "w+") as f:
		f.write(str(soup))
	with open("solo_champion/scraper/html.html", "w+") as f:    
		f.write(soup.prettify())
	with open("solo_champion/scraper/html.html", "r") as f:
		soup = BeautifulSoup(f, "html.parser")
	solo_items = []	
	for link in soup.find_all("img"):
		item = link.get("title")
		if item in items_list:
			solo_items.append(item)
	settied_items = []
	for i in solo_items:
		if i not in settied_items:
			settied_items.append(i)
	return JsonResponse({champion_name:settied_items})
