from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
import requests
from bs4 import BeautifulSoup
# from league_advisor.string_assets.menu_strings import strings
# from league_advisor.string_assets.colors import color
from django.http import HttpRequest



def get_items(request):
	items_list = ['Abyssal Mask', 'Aegis of the Legion', 'Aether Wisp', 'Amplifying Tome', "Anathema's Chains", "Archangel's Staff", 'Ardent Censer', 'B. F. Sword', "Bami's Cinder", 'Bandleglass Mirror', "Banshee's Veil", "Berserker's Greaves", 'Black Cleaver', 'Black Mist Scythe', 'Blade of The Ruined King', 'Blasting Wand', 'Blighting Jewel', 'Bloodthirster', 'Boots', 'Boots of Swiftness', 'Bramble Vest', 'Broken Stopwatch', 'Broken Stopwatch', 'Bulwark of the Mountain', "Caulfield's Warhammer", 'Chain Vest', 'Chempunk Chainsword', 'Chemtech Putrifier', 'Cloak of Agility', 'Cloth Armor', 'Commencing Stopwatch', 'Control Ward', 'Corrupting Potion', 'Cosmic Drive', 'Crystalline Bracer', 'Cull', 'Dagger', 'Dark Seal', "Dead Man's Plate", "Death's Dance", 'Demonic Embrace', 'Divine Sunderer', "Doran's Blade", "Doran's Ring", "Doran's Shield", 'Duskblade of Draktharr', 'Eclipse', 'Edge of Night', 'Elixir of Iron', 'Elixir of Sorcery', 'Elixir of Wrath', 'Emberknife', 'Essence Reaver', 'Everfrost', "Executioner's Calling", 'Eye of the Herald', 'Faerie Charm', 'Farsight Alteration', 'Fiendish Codex', 'Forbidden Idol', 'Force of Nature', 'Frostfang', 'Frostfire Gauntlet', 'Frozen Heart', 'Galeforce', 'Gargoyle Stoneplate', "Giant's Belt", 'Glacial Buckler', 'Goredrinker', 'Guardian Angel', "Guardian's Blade", "Guardian's Hammer", "Guardian's Horn", "Guardian's Orb", "Guinsoo's Rageblade", 'Hailblade', 'Harrowing Crescent', 'Health Potion', 'Hearthbound Axe', 'Hexdrinker', 'Hextech Alternator', 'Hextech Rocketbelt', 'Horizon Focus', 'Hullbreaker', 'Immortal Shieldbow', 'Imperial Mandate', 'Infinity Edge', 'Ionian Boots of Lucidity', 'Ironspike Whip', "Kalista's Black Spear", 'Kindlegem', 'Kircheis Shard', "Knight's Vow", 'Kraken Slayer', 'Last Whisper', 'Leeching Leer', "Liandry's Anguish", 'Lich Bane', 'Locket of the Iron Solari', 'Long Sword', "Lord Dominik's Regards", 'Lost Chapter', "Luden's Tempest", 'Manamune', 'Maw of Malmortius', "Mejai's Soulstealer", 'Mercurial Scimitar', "Mercury's Treads", "Mikael's Blessing", 'Minion Dematerializer', 'Mobility Boots', 'Moonstone Renewer', 'Morellonomicon', 'Mortal Reminder', 'Muramana', "Nashor's Tooth", 'Navori Quickblades', 'Needlessly Large Rod', 'Negatron Cloak', 'Night Harvester', 'Noonquiver', 'Null-Magic Mantle', 'Oblivion Orb', 'Oracle Lens', 'Pauldrons of Whiterock', 'Perfectly Timed Stopwatch', 'Phage', 'Phantom Dancer', 'Pickaxe', 'Plated Steelcaps', 'Poro-Snax', "Prowler's Claw", 'Quicksilver Sash', "Rabadon's Deathcap", 'Rageknife', "Randuin's Omen", 'Rapid Firecannon', 'Ravenous Hydra', 'Recurve Bow', 'Redemption', 'Refillable Potion', 'Rejuvenation Bead', 'Relic Shield', 'Riftmaker', 'Ruby Crystal', "Runaan's Hurricane", 'Runesteel Spaulders', "Rylai's Crystal Scepter", 'Sapphire Crystal', 'Scarecrow Effigy', "Seeker's Armguard", "Seraph's Embrace", "Serpent's Fang", 'Serrated Dirk', "Serylda's Grudge", 'Shard of True Ice', 'Sheen', "Shurelya's Battlesong", 'Silvermere Dawn', 'Slightly Magical Footwear', "Sorcerer's Shoes", 'Spectral Sickle', "Spectre's Cowl", "Spellthief's Edge", 'Spirit Visage', 'Staff of Flowing Water', 'Stealth Ward', 'Steel Shoulderguards', "Sterak's Gage", 'Stopwatch', 'Stormrazor', 'Stridebreaker', 'Sunfire Aegis', "Targon's Buckler", 'Tear of the Goddess', 'The Collector', 'The Golden Spatula', 'Thornmail', 'Tiamat', 'Titanic Hydra', 'Total Biscuit of Everlasting Will', 'Trinity Force', 'Turbo Chemtank', 'Umbral Glaive', 'Vampiric Scepter', 'Verdant Barrier', 'Vigilant Wardstone', 'Void Staff', "Warden's Mail", "Warmog's Armor", 'Watchful Wardstone', 'Winged Moonplate', "Wit's End", "Youmuu's Ghostblade", 'Your Cut', 'Zeal', "Zeke's Convergence", "Zhonya's Hourglass"]


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
