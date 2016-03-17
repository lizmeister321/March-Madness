
##THE BRACKET-O-RANDO-MATIC 1600! BETTER THAN LAST YEAR'S EFFORT!##


from random import *

with open('bracket16.txt','r') as full_bracket:
 all_teams=full_bracket.read().split('\r')

for index, team in enumerate(all_teams):
 all_teams[index]=team.split('\t')


headers = all_teams.pop(0)

west = []
south = []
midwest = []
east = []




finals = []

for team in all_teams:
	if team[2] == 'East':
		east.append(team)
	elif team[2] == 'West':
		west.append(team)
	elif team[2] == 'Midwest':
		midwest.append(team)
	else:
		south.append(team)


# print randrange(0, 16,1)

def unique_list_gen(length, max_len):
	index_tally = 0
	index = []
	randomized = randrange(1,max_len,1)
	index.append(randomized)
	while index_tally < length-1:
		control = 'n'
		while control == 'n':
			randomized = randrange(1,max_len,1)
			if randomized not in index:
				index.append(randomized)
				control = 'y'
			else:
				pass
		index_tally += 1
	return index



def pick_8(region):
	output = []
	for item in unique_list_gen(8,16):
		for index, team in enumerate(region):
			if int(team[1]) == item:
				output.append(team[0])
			else:
				pass
	return output


def pick_4(region):
	output = []
	for item in unique_list_gen(4,8):
		output.append(region[item])
	return output


west_round3 = pick_8(west)
east_round3 = pick_8(east)
south_round3 = pick_8(south)
midwest_round3 = pick_8(midwest)


west_sweet16 = pick_4(west_round3)
east_sweet16 = pick_4(east_round3)
south_sweet16 = pick_4(south_round3)
midwest_sweet16 = pick_4(midwest_round3)


# west_elite = []
# east_elite = []
# south_elite= []
# midwest_elite = []

# west_finalfour = []
# east_finalfour = []
# south_finalfour = []
# midwest_finalfour = []

# print west_sweet16

