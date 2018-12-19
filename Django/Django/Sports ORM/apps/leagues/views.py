from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.order_by("-team_name"),
		"players": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt"),
		"baseball_leagues": League.objects.filter(sport = 'Baseball'),
		"womens_leagues":League.objects.filter(name__icontains="Women"),
		"hockey_leagues":League.objects.filter(name__icontains="hockey"),
		"non_football":League.objects.exclude(name__icontains="football"),
		"conference_league":League.objects.filter(name__icontains="conference"),
		"atlantic_region":League.objects.filter(name__icontains="atlantic"),
	}
	return render(request, "leagues/index.html", context)

def level_two(request):
	atlantic = League.objects.get(name= "Atlantic Soccer Conference")
	context = {
		"atlantic_soccer_conference": Team.objects.filter(league = atlantic),
		"boston_penguins": Player.objects.filter(curr_team__location="Boston").filter(curr_team__team_name = "Penguins"),
		"icbc": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"acaf": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football").filter(last_name__icontains ="lopez"),
		"football_players":Player.objects.filter(curr_team__league__sport__icontains='football').all(),
		"team_sophia": Team.objects.filter(curr_players__first_name__icontains='sophia'),
		"sophia_leagues": League.objects.filter(teams__curr_players__first_name__icontains = "sophia"),
		"non_wr": Player.objects.filter(last_name__icontains="flores").exclude(curr_team__team_name__icontains="Roughriders")

	}
	return render (request, "leagues/level_two.html", context)

def level_three(request):
	context = {
		"sam_evans": Team.objects.filter(all_players__first_name__icontains='sam').all(),
		"mtc": Player.objects.filter(all_teams__team_name__istartswith="tiger").all(),
		"non_vikings": Player.objects.filter(all_teams__team_name__icontains="vikings").all(),
		"team_jacob": Team.objects.exclude(team_name="Oregon Colts").filter(all_players__last_name__icontains="gray")

	}
	return render (request, "leagues/level_three.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")