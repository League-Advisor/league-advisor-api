
import requests
from django.http import JsonResponse
from bs4 import BeautifulSoup

def patch_notes(request):

    # NOTE: GET LATEST PATCH VERSION
    current_versions = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()

    version_list = current_versions[0].split(".")

    # NOTE: GET THE CORRESPONDING URL
    url = f"https://www.leagueoflegends.com/en-gb/news/game-updates/patch-{version_list[0]}-{version_list[1]}-notes/"

    # NOTE: SCRAPE LATEST PATCH NOTES AND SEND THEM AS A RESPONSE
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')

    patch_notes = soup.find(id="patch-notes-container")

    with open('patch_notes/scraper/patch.html', 'w') as outfile:
        outfile.write(patch_notes.prettify())

    with open("patch_notes/scraper/patch.html", "r") as f:
        soup = BeautifulSoup(f, "html.parser")

    return JsonResponse({'patch-notes':f'{soup}'})
