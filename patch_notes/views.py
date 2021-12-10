
import requests
from django.http import JsonResponse
from bs4 import BeautifulSoup

def patch_notes(request):

  url = "https://www.leagueoflegends.com/en-gb/news/game-updates/patch-11-24-notes/"

  request = requests.get(url)
  soup = BeautifulSoup(request.content, 'html.parser')

  patch_notes = soup.find(id="patch-notes-container")

  with open('patch_notes/scraper/patch.html', 'w') as outfile:
      outfile.write(patch_notes.prettify())

  with open("patch_notes/scraper/patch.html", "r") as f:
      soup = BeautifulSoup(f, "html.parser")

  return JsonResponse({'patch-notes':f'{soup}'})
