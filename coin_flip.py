import random

num_flips = int(raw_input("How many flips?"))

def coinToss(number):
    recordList, heads, tails = [], 0, 0 # multiple assignment
    for i in range(number): # do this 'number' amount of times
         flip = random.randint(0, 1)
         if (flip == 0):
              print("Heads")
              recordList.append("Heads")
         else:
              print("Tails")
              recordList.append("Tails")
    print(str(recordList))
    print(str(recordList.count("Heads")) + str(recordList.count("Tails")))


coinToss(num_flips)