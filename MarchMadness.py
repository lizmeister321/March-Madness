with open('bracket15.txt','r') as full_bracket:
	all_teams=full_bracket.read().split('\n')
	all_teams.pop(0)


for index, team in enumerate(all_teams):
	all_teams[index]=team.split('\t')


West=[]
South=[]
East=[]
Midwest=[]


for team in all_teams:
	if team[2] == 'West':
		West=West.append(team[0])
	elif team[2] == 'South':
		South=South.append(team[0])
	elif team[2] == 'East':
		East=East.append(team[0])
	else:
		Midwest=Midwest.append(team[0])

print length(West)
