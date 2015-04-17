with open ('rpi.csv','r') as full_bracket:
	all_teams=full_bracket.read().split("\r")

for index, school in enumerate(all_teams):
	all_teams[index]=school.split(",")

# rpi
# NATIONAL RANKING
# conference w/l
# road record
# win vs ranked

for index in all_teams:
	print index[2],index[3]