<<<<<<< HEAD
with open('bracket15.txt','r') as full_bracket:
 all_teams=full_bracket.read().split('\n')
 all_teams.pop(0)
=======
with open ('rpi.csv','r') as full_bracket:
	all_teams=full_bracket.read().split("\r")
>>>>>>> ac6e164cfe1d19354913f9cb6d83c6732d56caa7

for index, school in enumerate(all_teams):
	all_teams[index]=school.split(",")

<<<<<<< HEAD
for index, team in enumerate(all_teams):
 all_teams[index]=team.split('\t')



West=[]
South=[]
East=[]
Midwest=[]


for team in all_teams:
 all_teans.pop(1)
 if team[2] == 'West':
 West=West.append(team[0])
 elif team[2] == 'South':
 South=South.append(team[0])
 elif team[2] == 'East':
 East=East.append(team[0])
 else:
 Midwest=Midwest.append(team[0])

print length(West)
=======
# rpi
# NATIONAL RANKING
# conference w/l
# road record
# win vs ranked

for index in all_teams:
	print index[2],index[3]
>>>>>>> ac6e164cfe1d19354913f9cb6d83c6732d56caa7
