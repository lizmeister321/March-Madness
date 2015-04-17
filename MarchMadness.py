
with open('bracket15.txt','r') as full_bracket:
 all_teams=full_bracket.read().split('\n')
 all_teams.pop(0)

for index, team in enumerate(all_teams):
 all_teams[index]=team.split('\t')

print len(all_teams)


West=[]
South=[]
East=[]
Midwest=[]


for team in all_teams:
 all_teams.pop(-1)
 if team[2] == 'West':
 	West.append(team[0])
 elif team[2] == 'South':
 	South.append(team[0])
 elif team[2] == 'East':
 	East.append(team[0])
 else:
 	Midwest.append(team[0])


print len(West)
print len(East)
print len(Midwest)
print len(South)

