# ForeignKey Relationships

Question | Expected Output
--- | ---
1. Find all teams in the Atlantic Soccer Conference | Minneapolis Wizards, Pittsburgh Bruins, Cleveland Dolphins, Toronto Pirates, Golden State Raptors
---	atlantic = League.objects.get(name= "Atlantic Soccer Conference")
	context = {
		"atlantic_soccer_conference": Team.objects.filter(league = atlantic)
	}


2. Find all (current) players on the Boston Penguins | Landon Hernandez, Wyatt Bennett, David Sanchez
---"boston_penguins": Player.objects.filter(curr_team__location="Boston")    .filter(curr_team__team_name = "Penguins")


3. Find all (current) players in the International Collegiate Baseball Conference | Michael Flores, Abigail Foster, Ryan Phillips, Elijah Powell, Isaac Perry, Charlotte Jones, Sophia Rivera, Isabella Griffin, Landon Cooper, Elijah James, Abigail Davis, Wyatt Alexander, Abigail Richardson, Jacob Jenkins, Landon Gray, Levi Miller, Joshua Long, Nathan Mitchell, James Ramirez, Samuel Evans, John Edwards, Henry Martin, Andrew Adams, Joshua White, Alexander Flores, Abigail Hernandez, Caleb Parker, Joshua Smith, Jack Phillips
---"icbc": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference")


4. Find all (current) players in the American Conference of Amateur Football with last name "Lopez" | Levi Lopez, Isabella Lopez
---"acaf": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football").filter(last_name__icontains       ="lopez"),


5. Find all football players | Nathan Bryant, Wyatt Bell, Lucas Martin, Luke Lopez, Dylan Rodriguez, Luke Bell, James Ross, Benjamin King, Caleb Martinez, Jack Young, Anthony Martinez, Jaxon Gonzales, Emily Sanchez, Jaxon Torres, Liam Watson, James Smith, Dylan Garcia, Joshua Cooper, Aiden Rivera, Benjamin Alexander, Ava Henderson, Joshua Hayes, Landon Mitchell, Charles Collins, Nathan Brooks, Isabella Bennett, Lucas Perry, Charles Campbell, Alexander Parker, Benjamin Perry, Levi Lopez, Charlotte Ross, Oliver Kelly, Daniel Martinez, Ryan Peterson, Isabella Lopez, Charlotte Harris, Caleb Collins, Ryan Gonzales, Joseph Roberts, David Watson, Abigail Long, Landon James, Daniel Davis, Charlotte Brown, Logan King, Luke Clark, Isabella Lewis, Jacob Gray, Liam Robinson, Aiden Hernandez, Christian Wood, Joshua Parker, Ethan Sanchez, Noah Brooks, Charles Campbell, Mason Henderson, Nathan Flores, Jackson Perry, Noah Taylor, Levi Howard, Jayden Perez, Elijah Richardson, Emily Jackson, Olivia Young, Abigail Torres, Christopher Sanders
---"football_players":Player.objects.filter(curr_team__league__sport__icontains='football').all()


6. Find all teams with a (current) player named "Sophia" | Mexico City Cave Spiders, Houston Hornets, Wisconsin Devils
---"team_sophia": Team.objects.filter(curr_players__first_name__icontains='sophia')


7. Find all leagues with a (current) player named "Sophia" | International Collegiate Baseball Conference, Atlantic Federation of Basketball Athletics, Atlantic Amateur Field Hockey League
---"sophia_leagues": League.objects.filter(teams__curr_players__first_name__icontains = "sophia")


8. Find everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders | Michael Flores, Alexander Flores, Nathan Flores
---"non_wr": Player.objects.filter(last_name__icontains="flores").exclude(curr_team__team_name__icontains="Roughriders")
    ---don't inlude washington